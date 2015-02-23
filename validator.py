from CSS3 import requests
import sublime
import sublime_plugin
import threading


bad_lines = {}
semicolon_errors = {
    "en": "attempt to find a semi-colon",
    "fr": "impossible de trouver un point-virgule",
    "it": "provato a trovare un punto e virgola",
    "ko": "속성 앞에 세미콜론을 찾으려고 시도하였습니다",
    "ja": "プロパティ名の前にセミコロン(;)",
    "es": "Tentativa de encontrar un punto y coma",
    "zh-cn": "试图寻找属性名前面的冒号",
    "nl": "poging een puntkomma",
    "de": "Versuche ein Semikolon",
    "pl": "próba znalezienia rednika",
}
settings = {}


class Css3Validator(sublime_plugin.TextCommand):

    """This abstract class contains the core functions for submitting
    CSS code to the W3C validator and flagging errors with gutter marks.
    """

    def validate(self, texts):
        """Submit the user's code to the W3C Validator."""
        global settings
        settings = sublime.load_settings("CSS3.sublime-settings")
        timeout = settings.get("validator_timeout", 10)

        threads = []
        for text in texts:
            thread = W3cValidatorCall(text, timeout)
            threads.append(thread)
            thread.start()

        self.handle_threads(threads)

    # This is based on MIT-licensed code from github.com/wbond/sublime_prefixr
    def handle_threads(self, threads, has_errors=False, i=0, direction=1):
        """Wait for a the API call(s) to finish and mark the bad lines.

        Keyword arguments:
        threads    -- list of threads (alive or dead)
        has_errors -- True if validator found at least one error
                      (default False)
        i          -- position of the activity indicator (default 0)
        direction  -- direction of the activity indicator
                      (-1 left, 1 right)
        """
        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue

            if not thread.results["validity"]:
                has_errors = True
                lang = settings.get("validator_language", "en")
                zoom = settings.get("zoom_to_error", False)
                self.mark_errors(thread.results["errors"], lang, zoom)

        if next_threads:
            before, after, i, direction = self.activity_indicator(i, direction)
            indicator = "Validator [{}={}]".format(" " * before, " " * after)
            self.view.set_status("Validator Running", indicator)
            func = lambda: self.handle_threads(next_threads, has_errors, i,
                                               direction)
            sublime.set_timeout(func, 100)
            return

        self.view.erase_status("Validator Running")

        if not has_errors:
            self.view.erase_regions("mark")
            self.show_congrats()

    def mark_errors(self, errors, lang="en", zoom=False):
        """Mark the line numbers returned by the validator.

        errors -- dictionary of errors returned by the validation server
                  call
        lang   -- the language of the error messages (default "en")
        zoom   -- scroll viewport to the first error (default False)
        """
        bad_regions = []
        for err in errors:
            try:
                lineno = err["line"]
            except KeyError as kerr:
                print("errors:", errors)
                print(kerr)
                continue
            msg = err["message"].rstrip(": ")
            if msg.startswith(semicolon_errors[lang]):
                # Missing semicolons are reported as an error on the # following
                # line.
                lineno -= 1
            bad_lines[lineno] = msg

            # Skip the leading whitespace and mark the rest of the line as bad.
            # This fixes a bug where inserting newlines in the leading
            # whitespace causes the gutter mark to be on a different line than
            # the text where the error really is.
            line_start = self.view.text_point(lineno - 1, 0)
            err_region = self.view.find(r"\S.*$", line_start)
            bad_regions.append(err_region)

        # Mark the gutters.
        self.view.add_regions("mark", bad_regions, "invalid.illegal.css", "dot",
                              sublime.HIDDEN | sublime.PERSISTENT)

        if zoom and bad_regions:
            self.view.show(bad_regions[0], show_surrounds=True)

    def activity_indicator(self, i, direction):
        """Show that the validator is working by animating the status
        bar.

        i         -- the previous position of the '=' indicator
        direction -- the previous direction of the '=' indicator
                     (left or right)
        """
        before = i % 8
        after = 7 - before
        if after == 0:
            direction = -1
        elif before == 0:
            direction = 1
        i += direction
        return before, after, i, direction

    def show_congrats(self):
        """Open an output panel with a success message when there are no
        errors.
        """
        window = self.view.window()
        panel = window.create_output_panel("css3_validator")
        congrats = "Congratulations! No Error Found."
        panel.run_command("append", {"characters": congrats})
        window.run_command("show_panel", {"panel": "output.css3_validator"})


class Css3ValidateAll(Css3Validator):

    """Submit the entire file to the W3C Validator."""

    def run(self, edit):
        """A wrapper around the validate() call required by the Sublime
        API.
        """
        region = sublime.Region(0, self.view.size())
        full_css = self.view.substr(region)
        self.validate((full_css,))  # validate() expects an iterable of texts
        # from the selection


class W3cValidatorCall(threading.Thread):

    """A thread for making calls to the W3C validation service."""

    def __init__(self, text, timeout=10):
        """Initialize the thread that will make the request to the W3C
        Validator.

        text    -- the code to validate
        timeout -- number of seconds before giving up (default 10)
        """
        super().__init__(self)
        self.text = text
        self.timeout = timeout
        self.results = None

    def run(self):
        lang = settings.get("validator_language", "en")
        files = {
            "text": (None, self.text, "text/css"),
            "output": (None, "json"),
            "profile": (None, "css3"),
            "lang": (None, lang),
            "warning": (None, "no"),
        }
        headers = {
            "Accept-Charset": "utf-8",
            "User-Agent": "sublime text css3 package"
        }

        W3C_URL = "http://jigsaw.w3.org/css-validator/validator"
        try:
            resp = requests.post(W3C_URL, files=files, headers=headers, timeout=self.timeout)
            results = resp.json(encoding="UTF-8")
            self.results = results["cssvalidation"]
        except requests.exceptions.ConnectionError as conn_err:
            print(conn_err)
            sublime.error_message("ERROR: network connection failed")
        except requests.exceptions.HTTPError as http_err:
            print("W3C validation server returned an invalid HTTP response")
            print(http_err)
            sublime.error_message("ERROR: W3C Validation server returned an invalid response")
        except requests.exceptions.Timeout as timeout_err:
            print("connection to validation server timed out after {} seconds".format(self.timeout))
            print(timeout_err)
            sublime.error_message("ERROR: connection to W3C validation server timed out after {} "
                                  "seconds. You can adjust the timeout in the package settings."
                                  "".format(self.timeout))


class Css3ClearGutterMarks(sublime_plugin.TextCommand):

    """Manually clear all validation errors from the gutter."""

    def run(self, edit):
        self.view.erase_regions("mark")
        self.view.erase_status("Validation Error")
        global bad_lines
        bad_lines = {}


class Css3Events(sublime_plugin.EventListener):

    def on_pre_save_async(self, view):
        """Clear validation errors from the gutter when the user saves.

        The user can disable this in the package settings.
        """
        global settings
        settings = sublime.load_settings("CSS3.sublime-settings")
        if settings.get("clear_errors_on_save", True):
            view.run_command("css3_clear_gutter_marks")

    def on_selection_modified_async(self, view):
        """Display validation error messages in the status bar.

        The message is displayed when the line with the error is
        selected.
        """
        lines = regions_to_lines(view, view.sel(), max_lines=3)
        errors = [bad_lines[line] for line in lines if line in bad_lines]
        if errors:
            messages = ("({0}) {1}".format(i, err) for i, err in enumerate(errors, start=1))
            view.set_status("Validation Error", " ".join(messages))
            return

        view.erase_status("Validation Error")


def regions_to_lines(view, sel, max_lines=-1):
    """Convert a set of regions to line numbers (which start at 1)."""
    # Pass a view object so we can use its lines() and rowcol() methods.
    line_nums = []
    for reg in view.sel():
        lines = view.lines(reg)
        for line in lines:
            row, _ = view.rowcol(line.begin())
            line_nums.append(row + 1)
            if max_lines != -1 and len(line_nums) >= max_lines:
                return line_nums

    return line_nums


# TODO
# rate limit requests
#   it's polite
#   mutex as static or class variable?
#   Queue?
#   use context manager?

# LOW PRIORITY
# css3_validate_selection command
#   validate only the selected text
# restrict scope of CSS3 palette commands to just CSS and html files
#   can't be done. sublime-commands files currently ignore the "context" field
#     would look like "context": [{"key": "selector", "operator": "equal", "operand": "source.css"}]
# remove marks when the line is modified
#   requires expensive on_modified_async() (called almost every keystroke)
