import sublime
import sublime_plugin
import urllib


class Css3HexConvertCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        window.show_input_panel("RGB:", "", self.validate_and_convert, None, None)

    def validate_and_convert(self, input_string):
        input_string = "".join(input_string.split())  # remove all whitespace
        if input_string == "":
            print("the user entered nothing")
            return

        colors = input_string.split(",")
        if len(colors) != 3:
            sublime.error_message("ERROR: You entered {} colors. Three colors are required (red, "
                                  "green, blue).\n\nHere's an example of a correct RGB value:\n\t"
                                  "255, 255, 255".format(len(colors)))
            return

        color_values = []
        try:
            for color in colors:
                color_value = int(color)
                if not (0 <= color_value <= 255):
                    raise ValueError(color)
                color_values.append(color_value)
        except ValueError as rgb_err:
            sublime.error_message("ERROR: {} is outside the range 0-255".format(rgb_err))
            return

        hex_string = self.convert(color_values)

        self.view.run_command("css3_hex_insert", {"hex": hex_string})

    def convert(self, rgb):
        if all(c % 17 == 0 for c in rgb):
            # return the three character hex notation, ex: #abc instead of #aabbcc
            return "#" + "".join("{:x}".format(c)[0] for c in rgb)
        return "#" + "".join("{:x}".format(c) for c in rgb)


class Css3HexInsertCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        print("called")
        for region in self.view.sel():
            self.view.replace(edit, region, "")
            insert_point = region.begin()
            self.view.insert(edit, insert_point, args["hex"])

