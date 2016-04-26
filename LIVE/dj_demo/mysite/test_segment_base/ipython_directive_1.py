# Enable as a proper Sphinx directive
def setup(app):
    setup.app = app
    app.add_directive('ipython', IpythonDirective)
    app.add_config_value('ipython_savefig_dir', None, True)
    app.add_config_value('ipython_rgxin',
                         re.compile('In \[(\d+)\]:\s?(.*)\s*'), True)
    app.add_config_value('ipython_rgxout',
                         re.compile('Out\[(\d+)\]:\s?(.*)\s*'), True)
    app.add_config_value('ipython_promptin', 'In [%d]:', True)
    app.add_config_value('ipython_promptout', 'Out[%d]:', True)
