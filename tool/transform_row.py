import sublime_plugin


class TransformRowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the first selected region
        reg = self.view.sel()[0]

        # convert the region to a string
        line = self.view.substr(reg)

        # split the string on '|'. strip off all whitespace. filter non-unique
        # strings.
        values = set((s.strip() for s in line.split("|") if s.strip() != ""))

        # reverse sort and rejoin with '|'
        values = sorted(values, reverse=True)
        transformed = "|".join(values)
        transformed = r'\b(?:' + transformed + r')\b'

        self.view.replace(edit, reg, transformed)
