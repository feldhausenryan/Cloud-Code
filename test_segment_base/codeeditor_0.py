#===============================================================================
#    Qt Event handlers
#===============================================================================
    def setup_context_menu(self):
        """Setup context menu"""
        self.undo_action = create_action(self, _("Undo"),
                           shortcut=keybinding('Undo'),
                           icon=get_icon('undo.png'), triggered=self.undo)
        self.redo_action = create_action(self, _("Redo"),
                           shortcut=keybinding('Redo'),
                           icon=get_icon('redo.png'), triggered=self.redo)
        self.cut_action = create_action(self, _("Cut"),
                           shortcut=keybinding('Cut'),
                           icon=get_icon('editcut.png'), triggered=self.cut)
        self.copy_action = create_action(self, _("Copy"),
                           shortcut=keybinding('Copy'),
                           icon=get_icon('editcopy.png'), triggered=self.copy)
        paste_action = create_action(self, _("Paste"),
                           shortcut=keybinding('Paste'),
                           icon=get_icon('editpaste.png'), triggered=self.paste)
        self.delete_action = create_action(self, _("Delete"),
                           shortcut=keybinding('Delete'),
                           icon=get_icon('editdelete.png'),
                           triggered=self.delete)
        selectall_action = create_action(self, _("Select All"),
                           shortcut=keybinding('SelectAll'),
                           icon=get_icon('selectall.png'),
                           triggered=self.selectAll)
        toggle_comment_action = create_action(self,
                           _("Comment")+"/"+_("Uncomment"),
                           icon=get_icon("comment.png"),
                           triggered=self.toggle_comment)
        self.gotodef_action = create_action(self, _("Go to definition"),
                                   triggered=self.go_to_definition_from_cursor)
        run_selected_action = create_action(self,
                                        _("Run &selection or current block"),
                                        icon='run_selection.png',
                                        triggered=lambda: self.emit(
                                           SIGNAL('triggers_run_selection()')))
        self.menu = QMenu(self)
        add_actions(self.menu, (self.undo_action, self.redo_action, None,
                                self.cut_action, self.copy_action,
                                paste_action, self.delete_action,
                                None, selectall_action, None,
                                toggle_comment_action, None,
                                run_selected_action,
                                self.gotodef_action))
        # Read-only context-menu
        self.readonly_menu = QMenu(self)
        add_actions(self.readonly_menu,
                    (self.copy_action, None, selectall_action))
