# TODO: This is also a handy utility that could probaby be used elsewhere
def config_parser(filename, callback):
    """This is a very simplified config file parser that can update a config
    file in-place so that order and comments are preserved.
    The callback should be a function that takes a section, option, value,
    line number, and raw line as its input (the current config section the
    parser is in, the current option, its value, the line number of the config
    file, and the actual line string the parser is on).
    The callback function is called for each line of the file.  For multi-line
    option values the function is still called once for each line of the
    option, so the callback needs to know how to handle these if it desires to.
    A line in which section, option, and value are None is either a comment or
    a blank line.
    The return value of the callback function should be the raw line to output
    or an iterable of lines to output.  In most cases the callback function
    will just return the same line that was passed in.
    """
    config = open(filename).readlines()
    new_config = []
    current_section = None
    current_option = None
    updated = False
    for lineno, line in enumerate(config):
        match = ConfigParser.SECTCRE.match(line)
        if match:
            current_section = match.group('header')
            current_option = None
            section, option, value = current_section, None, None
        else:
            if re.match(r'^\s*#', line) or not line.strip():
                section, option, value = None, None, None
            elif re.match(r'^\s+', line):
                # A new line in the current option
                section, option, value = (current_section, current_option,
                                          line.strip())
            else:
                option, value = (item.strip() for item in line.split('=', 1))
                section = current_section
                current_option = option
        lines = callback(section, option, value, lineno, line)
        if lines != line:
            updated = True
        if isinstance(lines, basestring):
            new_config.append(lines)
        else:
            new_config.extend(lines)
    if updated:
        open(filename, 'w').writelines(new_config)
