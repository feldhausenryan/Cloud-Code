# A version with the condition set to true, common case just to attach a message
# to a skip decorator
def skip(msg=None):
    """Decorator factory - mark a test function for skipping from test suite.
    Parameters
    ----------
      msg : string
        Optional message to be added.
    Returns
    -------
       decorator : function
         Decorator, which, when applied to a function, causes SkipTest
         to be raised, with the optional message added.
      """
    return skipif(True,msg)
