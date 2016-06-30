from CSS3.completions import properties
from CSS3.completions import values
import re
import sublime
import sublime_plugin


INHIBIT_DEFAULTS = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS
property_name_rx = re.compile(r"(?P<prop_name>[-a-z0-9]+):")


class CSS3Completions(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
<<<<<<< HEAD
        trigger_start = locations[0] - len(prefix)

        # Completions is a list of (<trigger>, <completion>) tuples.
        # Completions are only offered for properties and values.
        if view.match_selector(trigger_start, "meta.property-name.css"):
            return properties.names, INHIBIT_DEFAULTS
        elif view.match_selector(trigger_start, "meta.value.css"):
            line = view.substr(view.line(trigger_start)).strip()
            matches = property_name_rx.search(line)
            if matches is not None:
                prop_name = matches.group("prop_name")
                if prop_name in properties.value_for_name:
                    return properties.value_for_name[prop_name] + values.all_values, INHIBIT_DEFAULTS
=======
        """Offer completions if they are available for the given cursor
        locations.

        view (sublime.View)   - sublime API object that contains the
                                match_selector() for detecting the current scope
                                and substr() for getting
        prefix (str)          - the first part of the text that triggered the
                                completion, e.g. "tex" for "text-decoration".
        locations (list: int) - the character position of each cursor
        """

        # Each location is the position of a cursor.
        for loc in locations:
            #                 |--prefix--|
            # trigger_start ->text-decorat|<- current cursor location
            trigger_start = loc - len(prefix)

            # Completions is a list of (<label>, <completion>) tuples.
            if view.match_selector(trigger_start, "meta.property-name.css"):

                return properties.names, INHIBIT_DEFAULTS

            if view.match_selector(trigger_start, "meta.value.css"):
                line = view.substr(view.line(trigger_start)).strip()
                matches = property_name_rx.search(line)
                if matches is not None:
                    prop_name = matches.group("prop_name")
                    if prop_name in properties.value_for_name:
                        return properties.value_for_name[prop_name] + values.all_values, INHIBIT_DEFAULTS
>>>>>>> new


# TODO
#   add completions for the scopes inside functions
