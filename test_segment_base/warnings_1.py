# Helper for _processoptions()
def _setoption(arg):
    import re
    parts = arg.split(':')
    if len(parts) > 5:
        raise _OptionError("too many fields (max 5): %r" % (arg,))
    while len(parts) < 5:
        parts.append('')
    action, message, category, module, lineno = [s.strip()
                                                 for s in parts]
    action = _getaction(action)
    message = re.escape(message)
    category = _getcategory(category)
    module = re.escape(module)
    if module:
        module = module + '$'
    if lineno:
        try:
            lineno = int(lineno)
            if lineno < 0:
                raise ValueError
        except (ValueError, OverflowError):
            raise _OptionError("invalid lineno %r" % (lineno,))
    else:
        lineno = 0
    filterwarnings(action, message, category, module, lineno)
