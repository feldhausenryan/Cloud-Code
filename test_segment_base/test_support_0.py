# Use the following check to guard CPython's implementation-specific tests --
# or to run them only on the implementation(s) guarded by the arguments.
def check_impl_detail(**guards):
    """This function returns True or False depending on the host platform.
       Examples:
          if check_impl_detail():               # only on CPython (default)
          if check_impl_detail(jython=True):    # only on Jython
          if check_impl_detail(cpython=False):  # everywhere except on CPython
    """
    guards, default = _parse_guards(guards)
    return guards.get(platform.python_implementation().lower(), default)
