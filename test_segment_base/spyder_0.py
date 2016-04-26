#==============================================================================
# Spyder's main window widgets utilities
#==============================================================================
def get_focus_python_shell():
    """Extract and return Python shell from widget
    Return None if *widget* is not a Python shell (e.g. IPython kernel)"""
    widget = QApplication.focusWidget()
    from spyderlib.widgets.shell import PythonShellWidget
    from spyderlib.widgets.externalshell.pythonshell import ExternalPythonShell
    if isinstance(widget, PythonShellWidget):
        return widget
    elif isinstance(widget, ExternalPythonShell):
        return widget.shell
