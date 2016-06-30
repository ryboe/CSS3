import sublime_plugin


class ReversePipeJoinMultilineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """
        BEFORE
            blue
            red
            green
            purple
            orange
            yellow
        AFTER
            yellow|
            red|
            purple|
            orange|
            green|
            blue
        """
        if len(self.view.sel()) < 1:
            # no text is selected
            return

        # get the first region
        reg = self.view.sel()[0]

        # convert region to string
        selection = self.view.substr(reg).strip()

        values = selection.split("|")
        values = strip_whitespace(values)

        # remove duplicates and reverse sort
        values = sorted(set(values), reverse=True)

        self.view.replace(edit, reg, "|\n".join(values))


class ReversePipeJoinCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """
        >>> ReversePipeJoinCommand().run('blue|red|green|purple|orange|yellow')
        'yellow|red|purple|orange|green|blue'
        """
        if len(self.view.sel()) < 1:
            # no text is selected
            return

        # get the first region
        reg = self.view.sel()[0]

        # convert region to string
        selection = self.view.substr(reg).strip()

        values = selection.split("|")
        values = strip_whitespace(values)

        # remove duplicates and reverse sort
        values = sorted(set(values), reverse=True)

        self.view.replace(edit, reg, "|".join(values))


def strip_whitespace(values):
    """Strip leading and trailing whitespace from each string in a list of
    strings. If the string only contains whitespace, filter it out.
    """
    return [v.strip() for v in values if v.strip()]
