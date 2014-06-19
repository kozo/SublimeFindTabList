import sublime, sublime_plugin
import os
import sys

class FindTabListCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        def on_done(index):
            window = sublime.active_window()
            tabs = window.views_in_group(window.active_group())
            window.focus_view(tabs[index])
        
        window = sublime.active_window()
        tabs = window.views_in_group(window.active_group())
        tabNames = []
        for item in tabs:
            if item.name() != "Find Results":
                # print(item.name())
                tabNames.append(os.path.basename(item.file_name()))

        window.show_quick_panel(tabNames, on_done)
