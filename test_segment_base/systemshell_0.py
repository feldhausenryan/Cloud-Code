#===============================================================================
#    Input/Output
#===============================================================================
    def transcode(self, bytes):
        if os.name == 'nt':
            return encoding.transcode(str(bytes.data()), 'cp850')
        else:
            return ExternalShellBase.transcode(self, bytes)
