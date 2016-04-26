# python_build: (Boolean) if true, we're either building Python or
# building an extension with an un-installed Python, so we use
# different (hard-wired) directories.
# Setup.local is available for Makefile builds including VPATH builds,
# Setup.dist is available on Windows
def _python_build():
    for fn in ("Setup.dist", "Setup.local"):
        if os.path.isfile(os.path.join(project_base, "Modules", fn)):
            return True
    return False
