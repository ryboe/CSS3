from CSS3.completions import properties as p
from CSS3.completions import selectors as s
from CSS3.completions import values as v
import re
import sublime
import sublime_plugin

# TODO: do i need this? probably
property_name_rx = re.compile(r"(?:-webkit-|-ms-|-moz-)?(?P<prop_name>[a-zA-Z-]+)\s*:")


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
            locations (list: int): The integer positions of cursors.

        Returns:
            A list of (<label>, <completion>) tuples or None. <label> is what
            will appear in the completions menu. <completion> is the snippet
            that will be inserted.
        """
        if len(locations) > 1:
            # If there's multiple cursors, we can't offer completions.
            #     body {
            #         foo: |<- cursor
            #         bar: |<- second cursor
            #     }
            #
            # Which values do we offer? foo's or bar's?
            return []

        # The start position of the prefix determines which completions are
        # offered.
        #         |--prefix--|
        # start ->text-decorat|<- current cursor location
        start = locations[0] - len(prefix)
        current_scopes = view.scope_name(start).split()

        # TODO
        # SELECTORS
        # if view.match_selector(start, "meta.selector.css"):
        #     pass

        # FUNCTIONS
        if view.match_selector(start, "source.css meta.function"):
            return get_function_completions(start, current_scopes)

        # AT-RULES
        if view.match_selector(start, "source.css -meta.at-rule"):
            return s.at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        if view.match_selector(start, "meta.at-rule.media.block.css, meta.at-rule.supports.block.css"):
            return s.nestable_at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        # AT-RULE BLOCKS
        if view.match_selector(start, "source.css meta.at-rule"):
            if view.match_selector(start, "meta.at-rule.keyframes.block.css -meta.keyframes-declaration-list.css"):
                # @keyframes selector
                return s.keyframes_selector, sublime.INHIBIT_WORD_COMPLETIONS

            if view.match_selector(start, "meta.at-rule.font-face.block.css"):
                # @font-face
                if view.match_selector(start, "source.css -meta.descriptor.font-face"):
                    return p.font_face_descriptors, sublime.INHIBIT_WORD_COMPLETIONS
                return get_descriptor_completions(current_scopes, descriptors_for="font-face")

            if view.match_selector(start, "meta.at-rule.font-feature-values.block.css"):
                # @font-feature-values
                if view.match_selector(start, "-meta.font-feature-type-block.css"):
                    return s.font_feature_types, sublime.INHIBIT_WORD_COMPLETIONS
                return []

            if view.match_selector(start, "meta.at-rule.viewport.block.css"):
                # @viewport
                if view.match_selector(start, "source.css -meta.descriptor.viewport"):
                    return p.viewport_descriptors, sublime.INHIBIT_WORD_COMPLETIONS
                return get_descriptor_completions(current_scopes, descriptors_for="viewport")

            if view.match_selector(start, "meta.at-rule.page.block.css -meta.page-margin-box.css"):
                # @top-right, etc.
                return s.page_margin_boxes, sublime.INHIBIT_WORD_COMPLETIONS

            if view.match_selector(start, "meta.at-rule.page.css -meta.at-rule.page.block.css"):
                # @page :left, etc.
                return s.at_page_selectors

            if view.match_selector(start, "meta.at-rule.charset.css"):
                # @charset
                return [('"UTF-8";',)], sublime.INHIBIT_WORD_COMPLETIONS

            if view.match_selector(start, "meta.at-rule.counter-style.block.css"):
                # @counter-style
                if view.match_selector(start, "-meta.descriptor.counter-style"):
                    return p.counter_style_descriptors, sublime.INHIBIT_WORD_COMPLETIONS
                return get_descriptor_completions(current_scopes, descriptors_for="counter-style")

            if view.match_selector(start, "meta.at-rule.color-profile.block.css"):
                if view.match_selector(start, "-meta.descriptor.color-profile"):
                    # @color-profile decriptor names
                    return p.color_profile_descriptors, sublime.INHIBIT_WORD_COMPLETIONS

                # @color-profile descriptor values
                return get_descriptor_completions(current_scopes, descriptors_for="color-profile")


def get_descriptor_completions(current_scopes, descriptors_for):
    completions = []

    descriptor_name = get_name(current_scopes, prefix="meta.descriptor.{}".format(descriptors_for))
    if descriptor_name:
        # There is a separate completions dictionary for every @-rule.
        completions_dict = v.at_rule_to_completions_dict[descriptors_for]
        completions = completions_dict.get(descriptor_name, []) + [v.var]

        if descriptor_name in v.allow_word_completions:
            return completions

    return completions, sublime.INHIBIT_WORD_COMPLETIONS


def get_function_completions(current_scopes):
    completions = []

    func_name = get_name(current_scopes, prefix="meta.function")
    if func_name:
        # Handle the case where the ::attr() pseudo-element and attr() function
        # have the same name.
        if func_name == "attr" and any("pseudo-element" in s for s in current_scopes):
            func_name = "::attr"

        # Append the var() completion to every set of completions.
        completions = v.func_name_to_completions.get(func_name, []) + [v.var]

        if func_name in v.allow_word_completions:
            # If the function takes an identifier as an argument, the
            # identifier will be in the local symbol index. Therefore,
            # we don't want to inhibit word completions.
            return completions

    return completions, sublime.INHIBIT_WORD_COMPLETIONS


def get_name(scopes, prefix):
    """
    Scans a list of scopes and returns the name of the function or descriptor
    with the given prefix. If there are multiple matches, only the name from the
    highest-precedence (rightmost) scope will be returned. If there are no
    scopes with the given prefix, an empty string is returned.

    Args:
        scopes (list: str): e.g. ['source.css', 'foo.bar.baz.css']
        prefix (str): e.g. 'foo.bar'

    Returns:
        The

    >>> scopes = ['source.css', 'meta.function.foo.css']
    >>> get_name(scopes, prefix='meta.function')
    'foo'
    >>> scopes = ['source.css', 'meta.descriptor.color-profile.bar.css']
    >>> get_name(scopes, prefix='meta.descriptor.color-profile')
    'bar'
    >>> scopes = ['source.css', 'meta.function.baz.css']
    >>> get_name(scopes, prefix='meta.descriptor.color-profile')
    ''
    """
    name_index = -2
    for scope in reversed(scopes):
        if scope.startswith(prefix):
            # ['meta', 'function', 'foo', 'css'] -> 'foo'
            return scope.split(".")[name_index]

    return ""

    # PROPERTY NAME COMPLETIONS

    # PROPERTY VALUE COMPLETIONS

    # SELECTOR COMPLETIONS

    # PSEUDO-CLASS FUNCTION COMPLETIONS

    # PSEUDO-ELEMENT FUNCTION COMPLETIONS

    # FUNCTION COMPLETIONS

    # if view.match_selector(start, "meta.property-value"):
    #     # value completions
    #     # TODO: look up completions for the given property. get the
    #     # property name from the scope!
    #     region = view.line(point)
    #     line = view.substr(region).strip()
    #     matches = property_name_rx.search(line)
    #     if matches is not None:
    #         prop_name = matches.group("prop_name")
    #         if prop_name in properties.value_for_name:
    #             return properties.value_for_name[prop_name] + values.all_values, INHIBIT_BOTH

    #     return []

    # if view.match_selector(start, "meta.property-list.css"):
    #     # property names
    #     return properties.names, INHIBIT_BOTH
