# Module-level setup and teardown.
def setup():
    push_exception_handler(handler=lambda *args, **kwds: None, reraise_exceptions=True)
