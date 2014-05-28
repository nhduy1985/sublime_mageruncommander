import sublime
import sublime_plugin
from MagerunCommander.MagerunBase import *

class MagerunModuleListCommand(MagerunBase, sublime_plugin.TextCommand):
    def run(self, edit):
        self.callMagerun('dev:module:list','List modules')

class MagerunModuleCreateCommand(MagerunBase, sublime_plugin.TextCommand):
    def run(self, edit):
        options = []
        vendorNamespace = ['vendorNamespace', {
            'caption': 'Vendor Namespace',
            'default_value': 'Namespace',
            'accepts_value': True,
            'prepend_base_dir': False,
            'arg_prefix': False
        }]
        moduleName = ['moduleName', {
            'caption': 'Module Name',
            'default_value': 'Module',
            'accepts_value': True,
            'prepend_base_dir': False,
            'arg_prefix': False
        }]
        blocks = ['add-blocks', {
            'caption': 'Create block classes (yes/no)',
            'default_value': 'no',
            'accepts_value': False,
            'prepend_base_dir': False,
            'true_value': 'yes'
        }]
        helpers = ['add-helpers', {
            'caption': 'Create helper classes (yes/no)',
            'default_value': 'no',
            'accepts_value': False,
            'prepend_base_dir': False,
            'true_value': 'yes'
        }]
        models = ['add-models', {
            'caption': 'Create model classes (yes/no)',
            'default_value': 'no',
            'accepts_value': False,
            'prepend_base_dir': False,
            'true_value': 'yes'
        }]
        options.append(vendorNamespace)
        options.append(moduleName)
        options.append(blocks)
        options.append(helpers)
        options.append(models)
        self.collect_data('dev:module:create', options, 'Creating a new module. Please wait...')