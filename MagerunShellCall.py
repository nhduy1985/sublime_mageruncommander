import threading, subprocess, os

class MagerunShellCall(threading.Thread):
    def __init__(self, command, base_dir, mrBase, timeout = 0):
        self.command = command
        self.timeout = timeout
        self.result = None
        self.base_dir = base_dir
        self.mrBase = mrBase
        threading.Thread.__init__(self)
    def run(self):
        args = 'php "' + self.base_dir + '/n98-magerun.phar" ' + self.command
        print(args)
        result, e = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, cwd=self.base_dir).communicate(timeout=self.timeout)
        if e:
            sublime.top(e)
            thread._Thread__stop()
            return
        else:
            if not result:
                result = "Something went wrong with the command - " + self.command
                sublime.error_message(result)
                thread._Thread__stop()
                return

            if isinstance(result, bytes):
                result = result.decode('utf-8')
            self.mrBase._output(result)
            thread._Thread__stop()
            return