#===============================================================================
#    Globals explorer
#===============================================================================
    def toggle_globals_explorer(self, state):
        if self.stand_alone is not None:
            self.splitter.setSizes([1, 1 if state else 0])
            self.namespacebrowser_button.setChecked(state)
            if state and self.namespacebrowser is not None:
                self.namespacebrowser.refresh_table()
