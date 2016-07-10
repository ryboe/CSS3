from CSS3.completions import at_rules
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
        if (
            view.match_selector(start, "source.css -meta.at-rule -meta.property-list.css") and
            view.match_selector(start - 1, "punctuation.definition.keyword.css")
        ):
            return at_rules.at_rules, sublime.INHIBIT_WORD_COMPLETIONS

        # NESTED AT-RULES
        if view.match_selector(start, "source.css meta.at-rule"):
            return at_rules.get_completions(view, start)

        # PROPERTY NAMES.
        # When we're inside a property list or a page margin box, the
        # meta.property-value-pair.css scope is triggered when the ':'is typed.
        # If that scope is not present, the user is typing a property name, not
        # a value.
        if (
            view.match_selector(start, "source.css meta.property-list.css -meta.property-value-pair") or
            view.match_selector(start, "source.css meta.page-margin-box.css -meta.property-value-pair")
        ):
            return properties.names, sublime.INHIBIT_WORD_COMPLETIONS

        # PROPERTY VALUES
        if view.match_selector(start, "source.css meta.property-value-pair"):
            return properties.get_values(current_scopes)

        # SELECTORS
        if view.match_selector(start, "meta.selector.css"):
            return selectors.get_completions(view, start)
