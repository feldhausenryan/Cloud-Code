#    CONFIGWIDGET_CLASS = BreakpointConfigPage
    def __init__(self, parent=None):
        BreakpointWidget.__init__(self, parent=parent)
        SpyderPluginMixin.__init__(self, parent)
        # Initialize plugin
        self.initialize_plugin()
        self.set_data()
