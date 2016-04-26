# Note that UnixCCompiler._compile appeared in Python 2.3
def UnixCCompiler__compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
    """Compile a single source files with a Unix-style compiler."""
    # HP ad-hoc fix, see ticket 1383
    ccomp = self.compiler_so
    if ccomp[0] == 'aCC':
        # remove flags that will trigger ANSI-C mode for aCC
        if '-Ae' in ccomp:
            ccomp.remove('-Ae')
        if '-Aa' in ccomp:
            ccomp.remove('-Aa')
        # add flags for (almost) sane C++ handling
        ccomp += ['-AA']
        self.compiler_so = ccomp
    display = '%s: %s' % (os.path.basename(self.compiler_so[0]),src)
    try:
        self.spawn(self.compiler_so + cc_args + [src, '-o', obj] +
                   extra_postargs, display = display)
    except DistutilsExecError:
        msg = str(get_exception())
        raise CompileError(msg)
