# This is a slightly modified version of the function above.  This
# version does the proper alighnment of labels with their fields.  It
# should probably eventually replace make_form_entry altogether.
#
# The one annoying bug is that the text entry field should be
# expandable while still aligning the colons.  This doesn't work yet.
#
def make_labeled_form_entry(parent, label, entrywidth=20, entryheight=1,
                            labelwidth=0, borderwidth=None,
                            takefocus=None):
    """Subroutine to create a form entry.
    Create:
    - a horizontally filling and expanding frame, containing:
      - a label on the left, and
      - a text entry on the right.
    Return the entry widget and the frame widget.
    """
    if label and label[-1] != ':': label = label + ':'
    frame = Frame(parent)
    label = Label(frame, text=label, width=labelwidth, anchor=E)
    label.pack(side=LEFT)
    if entryheight == 1:
        if borderwidth is None:
            entry = Entry(frame, relief=SUNKEN, width=entrywidth)
        else:
            entry = Entry(frame, relief=SUNKEN, width=entrywidth,
                          borderwidth=borderwidth)
        entry.pack(side=RIGHT, expand=1, fill=X)
        frame.pack(fill=X)
    else:
        entry = make_text_box(frame, entrywidth, entryheight, 1, 1,
                              takefocus=takefocus)
        frame.pack(fill=BOTH, expand=1)
    return entry, frame, label
