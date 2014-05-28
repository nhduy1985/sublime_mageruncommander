import sublime, sublime_plugin, os
from .MagerunShellCall import MagerunShellCall

class MagerunBase(sublime_plugin.TextCommand):
    def run(self,edit):
        self.callMagerun('dev:module:list','List modules')

    def callMagerun(self,command,message):
        print(message)
        base_dir = self._getBaseDir()

        thread = MagerunShellCall(command, base_dir, self)
        thread.start()

    def _getBaseDir(self):
        temp = self._checkProjectSettings()
        if not temp:
            temp = self._checkCrawlUp()
        if not temp:
            temp = self._checkCrawlDown()
        if not temp:
            return None

        return temp

    """Checks if the base_dir is in the project file"""
    def _checkProjectSettings(self):
        project_data = self.view.window().project_data()

        if 'settings' in project_data:
            for setting in project_data['settings']:
                if 'magerunCommand' in setting:
                    return setting.get('magerunCommand')

        return False
    def _checkCrawlUp(self):
        view_name = self.view.file_name()
        if view_name:
            dir_name = os.path.dirname(view_name)
            found_root = False
            reached_end = False
            while not found_root and not reached_end:
                for file in os.listdir(dir_name):
                    if file == "app" and os.path.isdir(dir_name + "/" + file):
                        #found an app dir
                        if os.path.exists(dir_name + '/n98-magerun.phar'):
                            return dir_name
                            found_root = True
                #travers up
                old_dir = dir_name
                dir_name = os.path.dirname(dir_name)
                if dir_name == old_dir:
                    reached_end = True

        return False

    """As a last resort, crawl down the tree for each of the folders to find app/console"""
    def _checkCrawlDown(self):
        folders = self.view.window().folders()
        base = ''

        if folders:
            for folder in folders:
                for root, dirs, files in os.walk(folder):
                    if 'app' in dirs and os.path.exists(root + '/n98-magerun.phar'):
                        base = root
                        break
                if base:
                    break
        return base

    """Display the results in an Sublime output box"""
    def _output(self, value):
        output = self.view.window().create_output_panel("variable_get")
        output.run_command('erase_view')
        output.run_command('append', {'characters': value})
        self.view.window().run_command("show_panel", {"panel": "output.variable_get"})

    ''' Collect User Data '''
    def collect_data(self, cmd, data, status_msg = ''):
        self.key, self.value = data.pop(0)
        self.data = data
        self.status_msg = status_msg
        self.command = cmd
        self.view.window().show_input_panel(self.value['caption'], self.value['default_value'], self.on_done, None, None)

    def on_done(self, text):
        if text:
            if not 'arg_prefix' in self.value or ('arg_prefix' in self.value and self.value['arg_prefix'] == True):
                arg_prefix = True
            else:
                arg_prefix = False

            if self.value['accepts_value']:
                if arg_prefix:
                    self.command += ' --' + self.key
                if 'prepend_base_dir' in self.value and self.value['prepend_base_dir']:
                    text = '"' + os.path.join(self.base_dir, text) + '"'

                if arg_prefix:
                    self.command += "="
                else:
                    self.command += " "

                if 'quotes' in self.value and self.value['quotes'] == True:
                    self.command += '"' + text + '"'
                else:
                    self.command += text
            else:
                if text == self.value['true_value']:
                    self.command += ' --' + self.key

        if len(self.data):
            self.collect_data(self.command, self.data, self.status_msg)
        else:
            self.callMagerun(self.command, self.status_msg)
