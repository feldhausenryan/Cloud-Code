# default values to some settings in case the user does not have these
defaultValues = {
    # export options
    'export_DPI': 100,
    'export_DPI_PDF': 150,
    'export_color': True,
    'export_antialias': True,
    'export_quality': 85,
    'export_background': '#ffffff00',
    'export_SVG_text_as_text': False,
    # plot options
    'plot_updatepolicy': -1, # update on document changed
    'plot_antialias': True,
    'plot_numthreads': 2,
    # recent files list
    'main_recentfiles': [],
    # default stylesheet
    'stylesheet_default': '',
    # default custom definitons
    'custom_default': '',
    # colors (isdefault, 'notdefaultcolor')
    'color_page': (True, 'white'),
    'color_error': (True, 'red'),
    'color_command': (True, 'blue'),
    'color_cntrlline': (True, 'blue'),
    'color_cntrlcorner': (True, 'black'),
    # further ui options
    'toolbar_size': 24,
    # if set to true, do UI formatting in US/English
    'ui_english': False,
    # use cwd as starting directory
    'dirname_usecwd': False,
    # ask tutorial before?
    'ask_tutorial': False,
    # log picked points to clipboard or to console
    'picker_to_clipboard': False,
    'picker_to_console': True
    }
