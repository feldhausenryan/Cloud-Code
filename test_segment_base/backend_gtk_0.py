# ref gtk+/gtk/gtkwidget.h
def GTK_WIDGET_DRAWABLE(w):
    flags = w.flags();
    return flags & gtk.VISIBLE != 0 and flags & gtk.MAPPED != 0
