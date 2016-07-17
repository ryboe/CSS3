from CSS3.completions import at_rules
from CSS3.completions import descriptors
from CSS3.completions import functions
from CSS3.completions import properties
from CSS3.completions import selectors
from CSS3.completions import util
import sublime
import sublime_plugin


class CSS3Completions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        """Populate the completions menu based on the current cursor location.

        Args:
            view (sublime.View): A Sublime API object that contains the
                match_selector() method for detecting if the current scope has
                completions, and the substr() method for getting text from the
                document.
            prefix (str): The first part of the text that triggered the
                completions menu, e.g. "tex" for "text-decoration".
            locations (list: int): The current integer positions of the cursors.

        Returns:
            [(<label>, <completion), ...], inhibit_flag

            <label> is what will appear in the completions menu. <completion> is
            the snippet that will be inserted. inhibit_flag controls whether
            "word completions" are offered as well. "Word completions" are
            a list of every word in the current file greater than four
            characters long.
        """

        # If there's multiple cursors, we can't offer completions.
        #     body {
        #         foo: |<- cursor
        #         bar: |<- second cursor
        #     }
        # Which values do we offer? foo's or bar's?
        if len(locations) > 1:
            return [], sublime.INHIBIT_WORD_COMPLETIONS

        if view.match_selector(locations[0], "comment.block.css"):
            return []

        # start determines which completions are offered.
        #         |--prefix--|
        # start ->text-decorat|<- current cursor location
        start = locations[0] - len(prefix)

        # INSIDE FUNCTIONS
        if view.match_selector(start, "source.css meta.function."):
            return handle_function_completions(view, start)

        # PROPERTY VALUES
        if view.match_selector(start - 1, "source.css meta.property-value."):
            # The current character position could be at the semicolon, which
            # is one character past the "meta.property-value." content scope:
            #     text-decoration: |;
            #                     ^ meta.property-value.text-decoration.css
            # So we need to step back one character (start - 1).
            return handle_property_value_completions(view, start - 1)

        # PROPERTY NAMES
        if view.match_selector(start, "meta.property-list.css -meta.property-value."):
            return properties.names, sublime.INHIBIT_WORD_COMPLETIONS

        if view.match_selector(start, "meta.at-rule.page.css -meta.at-rule.page.block.css"):
            return selectors.at_page, sublime.INHIBIT_WORD_COMPLETIONS

        # @-RULES
        if view.substr(start - 1) == "@":
            return handle_at_rule_completions(view, start)

        # DESCRIPTOR VALUES
        if view.match_selector(start - 1, "source.css meta.descriptor."):
            return handle_descriptor_value_completions(view, start - 1)

        # @FONT-FACE DESCRIPTOR NAMES
        if view.match_selector(start, "meta.at-rule.font-face.block.css -meta.descriptor.font-face."):
            return descriptors.font_face, sublime.INHIBIT_WORD_COMPLETIONS

        # @VIEWPORT DESCRIPTOR NAMES
        if view.match_selector(start, "meta.at-rule.viewport.block.css -meta.descriptor.viewport."):
            return descriptors.viewport, sublime.INHIBIT_WORD_COMPLETIONS

        # @COUNTER-STYLE DESCRIPTOR NAMES
        if view.match_selector(start, "meta.at-rule.counter-style.block.css -meta.descriptor.counter-style."):
            return descriptors.counter_style, sublime.INHIBIT_WORD_COMPLETIONS

        # @COLOR-PROFILE DESCRIPTOR NAMES
        if view.match_selector(start, "meta.at-rule.color-profile.block.css -meta.descriptor.color-profile."):
            return descriptors.color_profile, sublime.INHIBIT_WORD_COMPLETIONS

        # KEYFRAMES SELECTOR
        # Special case: Keyframes selectors are not scoped with "meta.selector.css"
        if view.match_selector(start, "meta.keyframes-block.css -meta.property-list.css"):
            return selectors.keyframes, sublime.INHIBIT_WORD_COMPLETIONS

        # SELECTORS
        if view.match_selector(start, "meta.selector.css"):
            return handle_selector_completions(view, start)


def handle_at_rule_completions(view, location):
    if view.match_selector(location, "meta.at-rule.page.block.css"):
        return at_rules.page_margin_boxes, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.at-rule.font-feature-values.block.css -meta.font-feature-type-block.css"):
        return at_rules.font_feature_types, sublime.INHIBIT_WORD_COMPLETIONS

    if at_rules.supports_nested(view, location):
        return at_rules.nestable, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "source.css -meta.at-rule."):
        return at_rules.all_rules, sublime.INHIBIT_WORD_COMPLETIONS

    return [], sublime.INHIBIT_WORD_COMPLETIONS


def handle_descriptor_value_completions(view, location):
    scopes = util.get_scopes(view, location)

    # >>> scopes = ["source.css", "meta.descriptor.viewport.zoom.css"]
    # >>> util.get_scope_that_starts_with(scopes, starts_with="meta.descriptor.")
    # 'meta.descriptor.viewport.zoom.css'
    scope = util.get_scope_that_starts_with(scopes, starts_with="meta.descriptor.")

    # "meta.descriptor.viewport.zoom.css" ->
    # ['meta', 'descriptor', 'viewport', 'zoom', 'css']
    #                         type        name
    type_index, name_index = 2, 3
    descriptor_type, descriptor_name = scope.split(".")[type_index:name_index+1]

    return descriptors.get_values(descriptor_type, descriptor_name)


def handle_function_completions(view, location):
    scopes = util.get_scopes(view, location)

    # >>> scopes = ["source.css", "meta.function.ca.c.css"]
    # >>> util.get_scope_that_starts_with(scopes, starts_with="meta.function.")
    # 'meta.function.calc.css'
    scope = util.get_scope_that_starts_with(scopes, starts_with="meta.function.")

    # "meta.function.calc.css" ->
    # ["meta", "function", "calc", "css"]
    #                      name
    name_index = -2
    func_name = scope.split(".")[name_index]

    return functions.get_values(func_name)


def handle_property_value_completions(view, location):
    scopes = util.get_scopes(view, location)

    # >>> scopes = ["source.css", "meta.property-value.width.css"]
    # >>> util.get_scope_that_starts_with(scopes, starts_with="meta.property-value.")
    # 'meta.property-value.width.css'
    scope = util.get_scope_that_starts_with(scopes, starts_with="meta.property-value.")

    # "meta.property-value.width.css" ->
    # ['meta', 'property-value', 'width', 'css']
    #                            name
    name_index = -2
    property_name = scope.split(".")[name_index]

    return properties.get_values(property_name)


def handle_selector_completions(view, location):
    if view.match_selector(location - 1, "punctuation.definition.entity.pseudo-element.css"):
        return selectors.pseudo_elements, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location - 1, "punctuation.definition.entity.pseudo-class.css"):
        return selectors.pseudo_classes, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.at-rule.keyframes.block.css -meta.property-list.css"):
        return selectors.keyframes, sublime.INHIBIT_WORD_COMPLETIONS

    # If we're not in a class, id, pseudo-class, or pseudo-element, offer HTML
    # tags as completions.
    if view.match_selector(location, "source.css -entity.other.attribute-name."):
        return selectors.html_tags
