import sublime
import sublime_plugin


class PrintScopeNameCommand(sublime_plugin.EventListener):
   def on_selection_modified(self, view):
      sublime.status_message(view.scope_name(view.sel()[0].a))
