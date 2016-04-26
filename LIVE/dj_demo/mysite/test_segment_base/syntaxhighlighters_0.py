#==============================================================================
# Python syntax highlighter
#==============================================================================
def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return "(?P<%s>" % name + "|".join(alternates) + ")"
