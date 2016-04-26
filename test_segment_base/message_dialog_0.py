# Convenience functions.
def information(parent, message, title='Information'):
    """ Convenience function to show an information message dialog. """
    dialog = MessageDialog(
        parent=parent, message=message, title=title, severity='information'
    )
    dialog.open()
    return
