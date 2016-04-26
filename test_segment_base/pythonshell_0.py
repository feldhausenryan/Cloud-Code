#===============================================================================
#    Input/Output
#===============================================================================
    def write_error(self):
        if os.name == 'nt':
            #---This is apparently necessary only on Windows (not sure though):
            #   emptying standard output buffer before writing error output
            self.process.setReadChannel(QProcess.StandardOutput)
            if self.process.waitForReadyRead(1):
                self.write_output()
        self.shell.write_error(self.get_stderr())
        QApplication.processEvents()
