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
            locations (list: int): The integer positions of the cursors.

        Returns:
            [(<label>, <completion), ...], inhibit_flag

            <label> is what will appear in the completions menu. <completion> is
            the snippet that will be inserted. inhibit_flag controls whether
            "word completions" are offered as well. "Word completions" are
            a list of every word in the current file greater than four
            characters long.
        """
        if len(locations) > 1:
            # If there's multiple cursors, we can't offer completions.
            #     body {
            #         foo: |<- cursor
            #         bar: |<- second cursor
            #     }
            # Which values do we offer? foo's or bar's?
            return [], sublime.INHIBIT_WORD_COMPLETIONS

        if view.match_selector(locations[0], "comment.block.css"):
            return []

        # start determines which completions are offered.
        #         |--prefix--|
        # start ->text-decorat|<- current cursor location
        start = locations[0] - len(prefix)
        current_scopes = util.get_scopes(view, start)

        # INSIDE FUNCTIONS
        if view.match_selector(start, "source.css meta.function."):
            return functions.get_completions(current_scopes)

        # PROPERTY VALUES
        if view.match_selector(start - 1, "source.css meta.property-value."):
            # The current character position could be at the semicolon, which
            # is one character past the "meta.property-value." content scope:
            #     text-decoration: |;
            #                     ^ meta.property-value.text-decoration.css
            # So we need to step back one character (start - 1).
            scopes = util.get_scopes(view, start - 1)
            return properties.get_values(scopes)

        # PROPERTY NAMES
        if view.match_selector(start, "meta.property-list.css -meta.property-value."):
            return properties.names, sublime.INHIBIT_WORD_COMPLETIONS

        # @-RULES
        if view.substr(start - 1) == "@":
            return get_at_rule_completions(view, start)

        # @COLOR-PROFILE DESCRIPTOR VALUES
        if view.match_selector(start - 1, "source.css meta.descriptor."):
            return descriptors.get_values(current_scopes, descriptors_for="color-profile")

        # @COLOR-PROFILE DESCRIPTOR NAMES
        if view.match_selector(start, "meta.at-rule.color-profile.block.css -meta.descriptor.color-profile."):
            return descriptors.color_profile, sublime.INHIBIT_WORD_COMPLETIONS


def get_at_rule_completions(view, location):
    if view.match_selector(location, "meta.at-rule.page.block.css"):
        return at_rules.page_margin_boxes, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.font-feature-type-block.css"):
        return at_rules.font_feature_types, sublime.INHIBIT_WORD_COMPLETIONS

    if at_rules.supports_nested(view, location):
        return at_rules.nestable, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "source.css -meta.at-rule."):
        return at_rules.all_rules, sublime.INHIBIT_WORD_COMPLETIONS

    return [], sublime.INHIBIT_WORD_COMPLETIONS









    # TODO: delete this
        # TOP-LEVEL AT-RULES
        # When the user starts typing an @-rule, it will first match as a
        # selector. The @-rule scope isn't applied until the entire @-rule name,
        # e.g. "@media", is typed. To distinguish @-rules from selectors, we
        # also check if the start location is preceded by an '@' symbol.

        # TODO: delete below
        # if (
        #     view.match_selector(start, "source.css -meta.at-rule. -meta.property-list.css") and
        #     view.substr(start - 1) == "@"
        # ):
        # if view.substr(start - 1) == "@":
        #     return at_rules.all_at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        # NESTABLE AT-RULES
        # Only @media and @supports can have @-rules nested inside them. To
        # prevent the completions menu from offering @-rules that don't make
        # sense in a nested context, we only offer the subset of nestable
        # @-rules here.
        # if (
        #     view.match_selector(start, "source.css meta.at-rule.") and
        #     view.substr(start - 1) == "@" and
        #     at_rules.supports_nested_at_rules(view, start)
        # ):
        #     return at_rules.nestable_at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        # if view.match_selector(start, "source.css meta.at-rule."):
        #     completions, inhibit_flag = at_rules.get_completions(view, start)
        #     if completions:
        #         return completions, inhibit_flag
        # elif view.match_selector(start, "meta.selector.css"):
        #     return selectors.get_completions(view, start)
