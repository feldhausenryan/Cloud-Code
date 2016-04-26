# Define callable which returns the 'klass' value (i.e. the editor to use in
# the EditorFactory.
def history_editor(*args, **traits):
    return toolkit_object('history_editor:_HistoryEditor')(*args, **traits)
