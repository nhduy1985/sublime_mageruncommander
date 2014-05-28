import sublime
import sublime_plugin
from MagerunCommander.MagerunBase import *

class MagerunDebugHintOnCommand(MagerunBase, sublime_plugin.TextCommand):
    def run(self, edit):
        self.callMagerun('dev:template-hints --on 1','Turn ON template hints')

class MagerunDebugHintOffCommand(MagerunBase, sublime_plugin.TextCommand):
    def run(self, edit):
        self.callMagerun('dev:template-hints --off 1','Turn OFF template hints')

class MagerunDebugHintOnStoreCommand(MagerunBase, sublime_plugin.TextCommand):
    def run(self, edit):
        options = []
        storeOptions = ['store', {
            'caption': 'Store ID',
            'default_value': '1',
            'accepts_value': True,
            'prepend_base_dir': False,
            'arg_prefix': False
        }]
        options.append(storeOptions)
        self.collect_data('dev:template-hints --on', options, 'Turn ON template hints. Please wait...')

class MagerunDebugHintOffStoreCommand(MagerunBase, sublime_plugin.TextCommand):
    def run(self, edit):
        options = []
        storeOptions = ['store', {
            'caption': 'Store ID',
            'default_value': '1',
            'accepts_value': True,
            'prepend_base_dir': False,
            'arg_prefix': False
        }]
        options.append(storeOptions)
        self.collect_data('dev:template-hints --off', options, 'Turn OFF template hints. Please wait...')