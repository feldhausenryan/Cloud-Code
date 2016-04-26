#===============================================================================
#    Misc.
#===============================================================================
    def set_current_working_directory(self):
        """Set current working directory"""
        cwd = self.shell.get_cwd()
        self.emit(SIGNAL('redirect_stdio(bool)'), False)
        directory = getexistingdirectory(self, _("Select directory"), cwd)
        if directory:
            self.shell.set_cwd(directory)
        self.emit(SIGNAL('redirect_stdio(bool)'), True)
