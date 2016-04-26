# a map from key -> value, converter
defaultParams = {
    'backend'           : ['Agg', validate_backend], # agg is certainly present
    'backend_fallback'  : [True, validate_bool], # agg is certainly present
    'backend.qt4'       : ['PyQt4', validate_qt4],
    'toolbar'           : ['toolbar2', validate_toolbar],
    'datapath'          : [None, validate_path_exists],   # handled by _get_data_path_cached
    'interactive'       : [False, validate_bool],
    'timezone'          : ['UTC', str],
    # the verbosity setting
    'verbose.level'     : ['silent', validate_verbose],
    'verbose.fileo'     : ['sys.stdout', str],
    # line props
    'lines.linewidth'       : [1.0, validate_float],     # line width in points
    'lines.linestyle'       : ['-', str],                # solid line
    'lines.color'           : ['b', validate_color],     # blue
    'lines.marker'          : ['None', str],     # black
    'lines.markeredgewidth' : [0.5, validate_float],
    'lines.markersize'      : [6, validate_float],       # markersize, in points
    'lines.antialiased'     : [True, validate_bool],     # antialised (no jaggies)
    'lines.dash_joinstyle'  : ['round', validate_joinstyle],
    'lines.solid_joinstyle' : ['round', validate_joinstyle],
    'lines.dash_capstyle'   : ['butt', validate_capstyle],
    'lines.solid_capstyle'  : ['projecting', validate_capstyle],
    # patch props
    'patch.linewidth'   : [1.0, validate_float], # line width in points
    'patch.edgecolor'   : ['k', validate_color], # black
    'patch.facecolor'   : ['b', validate_color], # blue
    'patch.antialiased' : [True, validate_bool], # antialised (no jaggies)
    # font props
    'font.family'       : ['sans-serif', str],       # used by text object
    'font.style'        : ['normal', str],           #
    'font.variant'      : ['normal', str],           #
    'font.stretch'      : ['normal', str],           #
    'font.weight'       : ['normal', str],           #
    'font.size'         : [12, validate_float],      # Base font size in points
    'font.serif'        : [['Bitstream Vera Serif', 'DejaVu Serif',
                            'New Century Schoolbook', 'Century Schoolbook L',
                            'Utopia', 'ITC Bookman', 'Bookman',
                            'Nimbus Roman No9 L','Times New Roman',
                            'Times','Palatino','Charter','serif'],
                           validate_stringlist],
    'font.sans-serif'   : [['Bitstream Vera Sans', 'DejaVu Sans',
                            'Lucida Grande', 'Verdana', 'Geneva', 'Lucid',
                            'Arial', 'Helvetica', 'Avant Garde', 'sans-serif'],
                           validate_stringlist],
    'font.cursive'      : [['Apple Chancery','Textile','Zapf Chancery',
                           'Sand','cursive'], validate_stringlist],
    'font.fantasy'      : [['Comic Sans MS','Chicago','Charcoal','Impact'
                           'Western','fantasy'], validate_stringlist],
    'font.monospace'    : [['Bitstream Vera Sans Mono', 'DejaVu Sans Mono',
                            'Andale Mono', 'Nimbus Mono L', 'Courier New',
                            'Courier','Fixed', 'Terminal','monospace'],
                           validate_stringlist],
    # text props
    'text.color'          : ['k', validate_color],     # black
    'text.usetex'         : [False, validate_bool],
    'text.latex.unicode'  : [False, validate_bool],
    'text.latex.preamble' : [[''], validate_stringlist],
    'text.latex.preview' : [False, validate_bool],
    'text.dvipnghack'     : [None, validate_bool_maybe_none],
    'text.hinting'        : [True, validate_hinting],
    'text.hinting_factor' : [8, validate_int],
    'text.antialiased'    : [True, validate_bool],
    # The following are deprecated and replaced by, e.g., 'font.style'
    #'text.fontstyle'      : ['normal', str],
    #'text.fontangle'      : ['normal', str],
    #'text.fontvariant'    : ['normal', str],
    #'text.fontweight'     : ['normal', str],
    #'text.fontsize'       : ['medium', validate_fontsize],
    'mathtext.cal'        : ['cursive', validate_font_properties],
    'mathtext.rm'         : ['serif', validate_font_properties],
    'mathtext.tt'         : ['monospace', validate_font_properties],
    'mathtext.it'         : ['serif:italic', validate_font_properties],
    'mathtext.bf'         : ['serif:bold', validate_font_properties],
    'mathtext.sf'         : ['sans\-serif', validate_font_properties],
    'mathtext.fontset'    : ['cm', validate_fontset],
    'mathtext.default'    : ['it', validate_mathtext_default],
    'mathtext.fallback_to_cm' : [True, validate_bool],
    'image.aspect'        : ['equal', validate_aspect],  # equal, auto, a number
    'image.interpolation' : ['bilinear', str],
    'image.cmap'          : ['jet', str],        # one of gray, jet, etc
    'image.lut'           : [256, validate_int],  # lookup table
    'image.origin'        : ['upper', str],  # lookup table
    'image.resample'      : [False, validate_bool],
    'contour.negative_linestyle' : ['dashed', validate_negative_linestyle_legacy],
    # axes props
    'axes.axisbelow'        : [False, validate_bool],
    'axes.hold'             : [True, validate_bool],
    'axes.facecolor'        : ['w', validate_color],    # background color; white
    'axes.edgecolor'        : ['k', validate_color],    # edge color; black
    'axes.linewidth'        : [1.0, validate_float],    # edge linewidth
    'axes.titlesize'        : ['large', validate_fontsize], # fontsize of the axes title
    'axes.grid'             : [False, validate_bool],   # display grid or not
    'axes.labelsize'        : ['medium', validate_fontsize], # fontsize of the x any y labels
    'axes.labelweight'      : ['normal', str], # fontsize of the x any y labels
    'axes.labelcolor'       : ['k', validate_color],    # color of axis label
    'axes.formatter.limits' : [[-7, 7], validate_nseq_int(2)],
                               # use scientific notation if log10
                               # of the axis range is smaller than the
                               # first or larger than the second
    'axes.formatter.use_locale' : [False, validate_bool],
                               # Use the current locale to format ticks
    'axes.formatter.use_mathtext' : [False, validate_bool],
    'axes.unicode_minus'        : [True, validate_bool],
    'axes.color_cycle'      : [['b','g','r','c','m','y','k'],
                                    validate_colorlist], # cycle of plot
                                                         # line colors
    'polaraxes.grid'        : [True, validate_bool],   # display polar grid or not
    'axes3d.grid'           : [True, validate_bool],   # display 3d grid
    #legend properties
    'legend.fancybox'         : [False,validate_bool],
    'legend.loc'         : ['upper right',validate_legend_loc], # at some point, this should be changed to 'best'
    'legend.isaxes'      : [True,validate_bool],  # this option is internally ignored - it never served any useful purpose
    'legend.numpoints'   : [2, validate_int],     # the number of points in the legend line
    'legend.fontsize'    : ['large', validate_fontsize],
    'legend.markerscale' : [1.0, validate_float], # the relative size of legend markers vs. original
    'legend.shadow'        : [False, validate_bool],
    'legend.frameon'     : [True, validate_bool], # whether or not to draw a frame around legend
    # the following dimensions are in fraction of the font size
    'legend.borderpad'   : [0.4, validate_float], # units are fontsize
    'legend.labelspacing'      : [0.5, validate_float], # the vertical space between the legend entries
    'legend.handlelength'     : [2., validate_float], # the length of the legend lines
    'legend.handleheight'     : [0.7, validate_float], # the length of the legend lines
    'legend.handletextpad' : [.8, validate_float], # the space between the legend line and legend text
    'legend.borderaxespad'       : [0.5, validate_float], # the border between the axes and legend edge
    'legend.columnspacing'       : [2., validate_float], # the border between the axes and legend edge
    'legend.markerscale' : [1.0, validate_float], # the relative size of legend markers vs. original
    'legend.shadow'        : [False, validate_bool],
    # tick properties
    'xtick.major.size' : [4, validate_float],      # major xtick size in points
    'xtick.minor.size' : [2, validate_float],      # minor xtick size in points
    'xtick.major.width': [0.5, validate_float],      # major xtick width in points
    'xtick.minor.width': [0.5, validate_float],      # minor xtick width in points
    'xtick.major.pad'  : [4, validate_float],      # distance to label in points
    'xtick.minor.pad'  : [4, validate_float],      # distance to label in points
    'xtick.color'      : ['k', validate_color],    # color of the xtick labels
    'xtick.labelsize'  : ['medium', validate_fontsize], # fontsize of the xtick labels
    'xtick.direction'  : ['in', str],            # direction of xticks
    'ytick.major.size' : [4, validate_float],      # major ytick size in points
    'ytick.minor.size' : [2, validate_float],      # minor ytick size in points
    'ytick.major.width': [0.5, validate_float],      # major ytick width in points
    'ytick.minor.width': [0.5, validate_float],      # minor ytick width in points
    'ytick.major.pad'  : [4, validate_float],      # distance to label in points
    'ytick.minor.pad'  : [4, validate_float],      # distance to label in points
    'ytick.color'      : ['k', validate_color],    # color of the ytick labels
    'ytick.labelsize'  : ['medium', validate_fontsize], # fontsize of the ytick labels
    'ytick.direction'  : ['in', str],            # direction of yticks
    'grid.color'       : ['k', validate_color],       # grid color
    'grid.linestyle'   : [':', str],       # dotted
    'grid.linewidth'   : [0.5, validate_float],     # in points
    'grid.alpha'       : [1.0, validate_float],
    # figure props
    # figure size in inches: width by height
    'figure.figsize'    : [ [8.0,6.0], validate_nseq_float(2)],
    'figure.dpi'        : [ 80, validate_float],   # DPI
    'figure.facecolor'  : [ '0.75', validate_color], # facecolor; scalar gray
    'figure.edgecolor'  : [ 'w', validate_color],  # edgecolor; white
    'figure.autolayout' : [ False, validate_bool],
    'figure.subplot.left'   : [0.125, ValidateInterval(0, 1, closedmin=True, closedmax=True)],
    'figure.subplot.right'  : [0.9, ValidateInterval(0, 1, closedmin=True, closedmax=True)],
    'figure.subplot.bottom' : [0.1, ValidateInterval(0, 1, closedmin=True, closedmax=True)],
    'figure.subplot.top'    : [0.9, ValidateInterval(0, 1, closedmin=True, closedmax=True)],
    'figure.subplot.wspace' : [0.2, ValidateInterval(0, 1, closedmin=True, closedmax=False)],
    'figure.subplot.hspace' : [0.2, ValidateInterval(0, 1, closedmin=True, closedmax=False)],
    'savefig.dpi'         : [100, validate_float],   # DPI
    'savefig.facecolor'   : ['w', validate_color],  # facecolor; white
    'savefig.edgecolor'   : ['w', validate_color],  # edgecolor; white
    'savefig.orientation' : ['portrait', validate_orientation],  # edgecolor; white
    'savefig.extension'   : ['png', deprecate_savefig_extension], # what to add to extensionless filenames
    'savefig.format'      : ['png', update_savefig_format], # value checked by backend at runtime
    'savefig.bbox'        : [None, validate_bbox], # options are 'tight', or 'standard'. 'standard' validates to None.
    'savefig.pad_inches'  : [0.1, validate_float],
    'tk.window_focus'    : [False, validate_bool],  # Maintain shell focus for TkAgg
    'tk.pythoninspect'   : [False, validate_tkpythoninspect],  # obsolete
    'ps.papersize'       : ['letter', validate_ps_papersize], # Set the papersize/type
    'ps.useafm'          : [False, validate_bool],  # Set PYTHONINSPECT
    'ps.usedistiller'    : [False, validate_ps_distiller], # use ghostscript or xpdf to distill ps output
    'ps.distiller.res'   : [6000, validate_int],     # dpi
    'ps.fonttype'        : [3, validate_fonttype], # 3 (Type3) or 42 (Truetype)
    'pdf.compression'    : [6, validate_int],        # compression level from 0 to 9; 0 to disable
    'pdf.inheritcolor'   : [False, validate_bool],   # ignore any color-setting commands from the frontend
    'pdf.use14corefonts' : [False, validate_bool],  # use only the 14 PDF core fonts
                                                    # embedded in every PDF viewing application
    'pdf.fonttype'      : [3, validate_fonttype],  # 3 (Type3) or 42 (Truetype)
    'pgf.debug'         : [False, validate_bool],  # output debug information
    'pgf.texsystem'     : ['xelatex', validate_pgf_texsystem], # choose latex application for creating pdf files (xelatex/lualatex)
    'pgf.rcfonts'       : [True, validate_bool],   # use matplotlib rc settings for font configuration
    'pgf.preamble'      : [[''], validate_stringlist], # provide a custom preamble for the latex process
    'svg.image_inline'  : [True, validate_bool],    # write raster image data directly into the svg file
    'svg.image_noscale' : [False, validate_bool],  # suppress scaling of raster data embedded in SVG
    'svg.embed_char_paths' : [True, deprecate_svg_embed_char_paths],  # True to save all characters as paths in the SVG
    'svg.fonttype' : ['path', validate_svg_fonttype],
    'docstring.hardcopy' : [False, validate_bool],  # set this when you want to generate hardcopy docstring
    'plugins.directory' : ['.matplotlib_plugins', str], # where plugin directory is locate
    'path.simplify' : [True, validate_bool],
    'path.simplify_threshold' : [1.0 / 9.0, ValidateInterval(0.0, 1.0)],
    'path.snap' : [True, validate_bool],
    'agg.path.chunksize' : [0, validate_int],       # 0 to disable chunking;
                                                    # recommend about 20000 to
                                                    # enable. Experimental.
    # key-mappings (multi-character mappings should be a list/tuple)
    'keymap.fullscreen' : [('f', 'ctrl+f'), validate_stringlist],
    'keymap.home' : [['h', 'r', 'home'], validate_stringlist],
    'keymap.back' : [['left', 'c', 'backspace'], validate_stringlist],
    'keymap.forward' : [['right', 'v'], validate_stringlist],
    'keymap.pan' : ['p', validate_stringlist],
    'keymap.zoom' : ['o', validate_stringlist],
    'keymap.save' : [('s', 'ctrl+s'), validate_stringlist],
    'keymap.quit' : [('ctrl+w', ), validate_stringlist],
    'keymap.grid' : ['g', validate_stringlist],
    'keymap.yscale' : ['l', validate_stringlist],
    'keymap.xscale' : [['k', 'L'], validate_stringlist],
    'keymap.all_axes' : ['a', validate_stringlist],
    # sample data
    'examples.directory' : ['', str],
    # Animation settings
    'animation.writer' : ['ffmpeg', validate_movie_writer],
    'animation.codec' : ['mpeg4', str],
    'animation.bitrate' : [-1, validate_int],
    'animation.frame_format' : ['png', validate_movie_frame_fmt], # Controls image format when frames are written to disk
    'animation.ffmpeg_path' : ['ffmpeg', str], # Path to FFMPEG binary. If just binary name, subprocess uses $PATH.
    'animation.ffmpeg_args' : ['', validate_stringlist], # Additional arguments for ffmpeg movie writer (using pipes)
    'animation.mencoder_path' : ['mencoder', str], # Path to FFMPEG binary. If just binary name, subprocess uses $PATH.
    'animation.mencoder_args' : ['', validate_stringlist], # Additional arguments for mencoder movie writer (using pipes)
