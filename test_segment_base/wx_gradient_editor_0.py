##########################################################################
# Test application.
##########################################################################
def main():
    from traitsui_gradient_editor import make_test_table
    table, ctf, otf = make_test_table(lut=False)
    # the actual gradient editor code.
    def on_color_table_changed():
        """If we had a vtk window running, update it here"""
        print("Update Render Window")
    app = wx.PySimpleApp()
    editor = wxGradientEditor(table,
                              on_color_table_changed,
                              colors=['rgb', 'a', 'h', 's', 'v'],
                              )
    editor.Show()
    app.MainLoop()
