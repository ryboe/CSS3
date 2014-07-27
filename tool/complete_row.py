import sublime
import sublime_plugin

class CompleteRowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # get the first selected region
        reg = self.view.sel()[0]

        # convert the region to a string
        line = self.view.substr(reg)

        # split the string on '|'. strip off all outer whitespace. filter
        # empty and non-unique strings. sort.
        values = set((s.strip() for s in line.split("|") if s.strip() != ""))
        predefined = set(("calc", "integer", "length", "number"))

        transformed = []
        for v in values:
            if v in predefined:
                transformed.append(v)
            else:
                transformed.append("(\"" + v + "\",)")

        transformed.sort()
        final = ", ".join(transformed)

        self.view.replace(edit, reg, final)
