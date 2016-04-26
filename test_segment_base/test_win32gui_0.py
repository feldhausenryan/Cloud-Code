# theoretically should be in pywin32_testutil, but this is the only place
# that currently needs such a function...
def ob2bytes(ob):
    if sys.version_info < (3,0):
        return str(buffer(ob))
    # py3k.
    return bytes(ob)
