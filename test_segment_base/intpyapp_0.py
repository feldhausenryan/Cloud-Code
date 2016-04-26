# todo - _SetupSharedMenu should be moved to a framework class.
def _SetupSharedMenu_(self):
        sharedMenu = self.GetSharedMenu()
        from pywin.framework import toolmenu
        toolmenu.SetToolsMenu(sharedMenu)
        from pywin.framework import help
        help.SetHelpMenuOtherHelp(sharedMenu)
