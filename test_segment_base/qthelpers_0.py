#===============================================================================
# Ready-to-use open/save dialogs
#===============================================================================
def exec_image_save_dialog(data, parent, basedir='', app_name=None):
    """
    Executes an image save dialog box (QFileDialog.getSaveFileName)
        * data: image pixel array data
        * parent: parent widget (None means no parent)
        * basedir: base directory ('' means current directory)
        * app_name (opt.): application name (used as a title for an eventual 
          error message box in case something goes wrong when saving image)
    Returns filename if dialog is accepted, None otherwise
    """
    saved_in, saved_out, saved_err = sys.stdin, sys.stdout, sys.stderr
    sys.stdout = None
    filename, _filter = getsavefilename(parent, _("Save as"), basedir,
                            io.iohandler.get_filters('save', dtype=data.dtype))
    sys.stdin, sys.stdout, sys.stderr = saved_in, saved_out, saved_err
    if filename:
        filename = to_text_string(filename)
        try:
            io.imwrite(filename, data)
            return filename
        except Exception as msg:
            import traceback
            traceback.print_exc()
            QMessageBox.critical(parent,
                 _('Error') if app_name is None else app_name,
                 (_("%s could not be written:") % osp.basename(filename))+\
                 "\n"+str(msg))
            return
