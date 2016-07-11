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
            locations (list: int): The integer positions of cursors.

        Returns:
            A list of (<label>, <completion>) tuples or None, and a flag that
            determines whether word completions are offered. <label> is what
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
            return [], sublime.INHIBIT_WORD_COMPLETIONS

        if view.match_selector(locations[0], "comment.block.css"):
            return []

        # The start position of the prefix determines which completions are
        # offered.
        #         |--prefix--|
        # start ->text-decorat|<- current cursor location
        start = locations[0] - len(prefix)
        current_scopes = util.get_current_scopes(view, start)

        # INSIDE FUNCTIONS
        if view.match_selector(start, "source.css meta.function"):
            return functions.get_completions(current_scopes)

        # TOP-LEVEL AT-RULES
        # When the user starts typing an @-rule, it will first match as a
        # selector. The @-rule scope isn't applied until the entire @-rule name
        # is typed. To distinguish @-rules from selectors, we check if the
        # start location is preceded by an '@' symbol.
        if (
            view.match_selector(start, "source.css -meta.at-rule -meta.property-list.css") and
            view.substr(start - 1) == "@"
        ):
            return at_rules.all_at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        # NESTABLE AT-RULES
        if (
            view.match_selector(start, "source.css meta.at-rule") and
            view.substr(start - 1) == "@" and
            at_rules.supports_nested_at_rules(view, start)
        ):
            return at_rules.nestable_at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        # PROPERTY VALUES
        if view.match_selector(start, "source.css meta.property-value-pair"):
            return properties.get_values(current_scopes)

        # PROPERTY NAMES
        # When we're inside a property list or a page margin box, the
        # meta.property-value-pair.css scope is triggered when the ':' is typed.
        # If that scope is not present, the user is typing a property name, not
        # a value.
        if (
            view.match_selector(start, "source.css meta.property-list.css -meta.property-value-pair") or
            view.match_selector(start, "source.css meta.page-margin-box.css -meta.property-value-pair")
        ):
            return properties.names, sublime.INHIBIT_WORD_COMPLETIONS

        # @keyframes selector
        if view.match_selector(start, "meta.at-rule.keyframes.block.css -meta.keyframes-declaration-list.css"):
            return selectors.keyframes, sublime.INHIBIT_WORD_COMPLETIONS

        # @keyframes properties and values
        if view.match_selector(start, "meta.keyframes-declaration-list.css"):
            if view.match_selector(start, "source.css -meta.property-value-pair"):
                return properties.names, sublime.INHIBIT_WORD_COMPLETIONS
            return properties.get_values(current_scopes)

        # @font-face
        if view.match_selector(start, "meta.at-rule.font-face.block.css"):
            if view.match_selector(start, "source.css -meta.descriptor.font-face"):
                return descriptors.font_face, sublime.INHIBIT_WORD_COMPLETIONS
            return descriptors.get_values(current_scopes, descriptors_for="font-face")

        # @font-feature-values
        if view.match_selector(start, "meta.at-rule.font-feature-values.block.css"):
            if view.match_selector(start, "-meta.font-feature-type-block.css"):
                return at_rules.font_feature_types, sublime.INHIBIT_WORD_COMPLETIONS
            return []

        # @viewport
        if view.match_selector(start, "meta.at-rule.viewport.block.css"):
            if view.match_selector(start, "source.css -meta.descriptor.viewport"):
                return descriptors.viewport, sublime.INHIBIT_WORD_COMPLETIONS
            return descriptors.get_values(current_scopes, descriptors_for="viewport")

        # @top-right, etc.
        if view.match_selector(start, "meta.at-rule.page.block.css -meta.page-margin-box.css"):
            return at_rules.page_margin_boxes, sublime.INHIBIT_WORD_COMPLETIONS

        # @page :left, etc.
        if view.match_selector(start, "meta.at-rule.page.css -meta.at-rule.page.block.css"):
            return selectors.at_page

        # @charset
        if view.match_selector(start, "meta.at-rule.charset.css"):
            return [('"UTF-8";',)], sublime.INHIBIT_WORD_COMPLETIONS

        # @counter-style
        if view.match_selector(start, "meta.at-rule.counter-style.block.css"):
            if view.match_selector(start, "-meta.descriptor.counter-style"):
                return descriptors.counter_style, sublime.INHIBIT_WORD_COMPLETIONS
            return descriptors.get_values(current_scopes, descriptors_for="counter-style")

        # @color-profile
        if view.match_selector(start, "meta.at-rule.color-profile.block.css"):
            if view.match_selector(start, "-meta.descriptor.color-profile"):
                return descriptors.color_profile, sublime.INHIBIT_WORD_COMPLETIONS

            return descriptors.get_values(current_scopes, descriptors_for="color-profile")

        # SELECTORS
        if view.match_selector(start, "meta.selector.css"):
            return selectors.get_completions(view, start)
