import pprint  # DEBUG
import json
import sublime
import sublime_plugin
import urllib
import threading
import time

# TODO: can i delete these now?
# make sublime.Region hashable so regions can be stored in a set
sublime.Region.__eq__   = lambda self, other: self.begin() == other.begin() and self.end() == other.end()
sublime.Region.__hash__ = lambda self: hash((self.begin(), self.end()))


w3c_url     = "http://jigsaw.w3.org/css-validator/validator?"
bad_lines   = {}


class Css3Validator(sublime_plugin.TextCommand):
    def validate(self, texts):
        # TODO: user can set the timeout in the settings
        # timeout = settings.get("timeout")
        threads = []
        for text in texts:
            thread = W3cValidatorCall(text)
            threads.append(thread)
            thread.start()

        self.handle_threads(threads)

    # code from github.com/wbond/sublime_prefixr
    # the i and direction params are for the status bar animation
    def handle_threads(self, threads, has_errors=False, i=0, direction=1):
        next_threads = []
        for thread in threads:
            if thread.is_alive():
                next_threads.append(thread)
                continue
            # DEBUG: purposefully using != instead of `is not` because i'm not sure if the None
            # object in the thread is the same None that is in the main thread
            assert thread.results != None, "the thread is supposed to be finished but it has no results"

            if not thread.results["validity"]:
                has_errors  = True
                bad_regions = []
                for err in thread.results["errors"]:
                    line = err["line"]
                    msg  = err["message"].rstrip(": ")
                    if msg.startswith("attempt to find a semi-colon"):
                        # missing semicolons are reported as an error on the following line
                        line -= 1
                    bad_lines[line] = msg
                    line_start = self.view.text_point(line - 1, 0)
                    bad_regions.append(self.view.line(line_start))  # add the entire line

                # mark the gutters
                self.view.add_regions("mark", bad_regions, "invalid.illegal.css", "dot",
                                      sublime.PERSISTENT)

        if next_threads:
            # This animates a little activity indicator in the status area
            before = i % 8
            after  = 7 - before
            if after == 0:
                direction = -1
            elif before == 0:
                direction = 1
            i += direction
            self.view.set_status("Validator Running", "Validator [{}={}]".format(" " * before, " " * after))

            sublime.set_timeout(lambda: self.handle_threads(next_threads, has_errors, i, direction), 100)
            return

        self.view.erase_status("Validator Running")

        if not has_errors:
            self.view.erase_regions("mark")
            window   = self.view.window()
            panel    = window.create_output_panel("css3_validator")
            congrats = "Congratulations! No Error Found."
            panel.run_command("append", {"characters": congrats})
            window.run_command("show_panel", {"panel": "output.css3_validator"})


class Css3ValidateAll(Css3Validator):
    def run(self, edit):
        region   = sublime.Region(0, self.view.size())
        full_css = self.view.substr(region)
        self.validate((full_css,))  # validate() expects an iterable of texts from the selection


# TODO: write this
# class Css3ValidateSelection(Css3Validator):
#     def run(self, edit):
#         sel = self.view.sel()
#         # verify that the selections list isn't empty, and that each region isn't empty


class W3cValidatorCall(threading.Thread):
    def __init__(self, text, timeout=10):
        super().__init__(self)
        self.text    = text
        self.timeout = timeout
        self.results = None

    def run(self):
        params = {"text": self.text, "output": "json", "profile": "css3", "warning": "no"}
        encoded_params = urllib.parse.urlencode(params)

        # set the Accept-Charset header to UTF-8 just in case. below it is assumed
        # the response is UTF-8
        headers = {"Accept-Charset": "utf-8", "User-Agent": "Sublime Text CSS3 Package"}
        req = urllib.request.Request(w3c_url + encoded_params, headers=headers, method="GET")

        try:
            response = urllib.request.urlopen(req, timeout=self.timeout)

            # can't json.load(response) directly. must decode to string first.
            data = json.loads(response.read().decode("UTF-8"), encoding="UTF-8")
            self.results = data["cssvalidation"]
            return
        except urllib.error.URLError as url_err:
            print(url_err)
            sublime.error_message("ERROR: network connection failed")
        except (UnicodeError, ValueError) as err:
            print(err)
            sublime.error_message("ERROR: failed to decode the response from the validation server")


class Css3ClearGutterMarks(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.erase_regions("mark")
        self.view.erase_status("Validation Error")
        global bad_lines
        bad_lines = {}


class Css3ShowError(sublime_plugin.EventListener):
    def on_modified_async(self, view):
        unsaved = view.get_regions("unsaved")
        for sel in view.sel():
            unsaved.extend(view.lines(sel))
        marked  = view.get_regions("mark")
        # DEBUG
        print("unsaved:", unsaved)
        print("marked: ", marked)

    def on_selection_modified_async(self, view):
        lines  = selection_to_lines(view, view.sel(), max_lines=3)
        errors = [bad_lines[line] for line in lines if line in bad_lines]
        if errors:
            messages = []
            for i, err in enumerate(errors, start=1):
                messages.append("({0}) {1}".format(i, err))
            view.set_status("Validation Error", " ".join(messages))
            return

        view.erase_status("Validation Error")


def selection_to_lines(view, sel, max_lines=-1):
    # pass a view objects so we can use its lines() and rowcol() methods
    line_nums = []
    for reg in view.sel():
        # get all the lines intersecting the region in the selection
        lines = view.lines(reg)

        # convert the line regions to line numbers (ints)
        for line in lines:
            row, _ = view.rowcol(line.begin())
            line_nums.append(row + 1)
            if max_lines != -1 and len(line_nums) >= max_lines:
                return line_nums

    return line_nums


# TODO
# css3_validate_selection command
# add docstrings to each function
# restrict scope of CSS3 commands to just CSS and html files
# test to see if async is necessary by putting time.sleep(5) everywhere
# remove marks when the line is modified
# rate limit requests
#   mutex as static or class variable?
#   context manager?
# make gutter marks persistent
# add language setting for error messages (currently can set lang param to en, fr, it, ko, ja, es, zh-cn, nl, de, it, pl)
#   settings = sublime.load_settings("CSS3.sublime-settings")
#   settings.get("language") or something like that
#   let the user set the timeout for the validation call in the settings
# show loading animation while it's working
# validate selection only
# refactor to move stuff to functions
# refactor to split into separate modules


# on_selection
#   bad_lines is a set of integers (line numbers)
#   get line numbers of selection
#   if line numbers of selection are in bad_lines
#     view.set_status("Validation Error", "; ".join(errors))
#   else
#     view.erase_status("Validation Error")
