import sublime
import sublime_plugin
import urllib


class GoogleFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        window.show_input_panel("Font Query:", "", self.font_prompt, None, None)

    def font_prompt(self, input_string):
        font_string = input_string.strip()
        if font_string == "":
            print("the user entered nothing")
            return

        try:
            font_family, font_weights = font_string.split(":")
        except ValueError:
            font_family, font_weights = font_string, ""

        font_family = "+".join(font_family.split())   # replace whitespace with '+'
        font_weights = font_weights.replace(" ", "")  # remove all whitespace

        try:
            url = "http://fonts.googleapis.com/css?family=" + font_family + ":" + font_weights
            # set user agent to recent version of Chrome 36 so Google Fonts will
            # return woff2 format with fallback to woff
            headers = {
                "Accept-Charset": "UTF-8",
                "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36")
            }
            req = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(req)
            css = response.read().decode()  # decode bytes as UTF-8
        except urllib.error.HTTPError as http_err:
            print(http_err)
            err_msg = ("ERROR: Google Fonts could not find that font.\n\nThis usually means you "
                       "mistyped the font name, or the weights are wrong. To see which weights are "
                       "available for that font, visit:\n\thttps://www.google.com/fonts\n\nHere's "
                       "an example of a correct font query:\n\tNoto Sans:400,400i,700,700i")
            sublime.error_message(err_msg)
            return
        except urllib.error.URLError as url_err:
            print(url_err)
            sublime.error_message("ERROR: could not establish a network connection")
            return
        except UnicodeError as unicode_err:
            print(unicode_err)
            sublime.status_message("ERROR: failed to decode the page returned by Google")
            return

        self.view.run_command("google_font_insert", {"css_text": css})


class GoogleFontInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        region = self.view.sel()[0]
        self.view.replace(edit, region, "")
        insert_point = region.begin()
        self.view.insert(edit, insert_point, args["css_text"])


# TODO
# add loading animation so the user knows it's working
