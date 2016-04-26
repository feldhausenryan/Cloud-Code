#==============================================================================
# Dependency management
#==============================================================================
def get_changeset(path, rev=None):
    """Return Mercurial repository *path* revision number"""
    args = ['hg', 'parent']
    if rev is not None:
        args += ['--rev', str(rev)]
    process = Popen(args, stdout=PIPE, stderr=PIPE, cwd=path, shell=True)
    try:
        return process.stdout.read().splitlines()[0].split()[1]
    except IndexError:
        raise RuntimeError(process.stderr.read())
