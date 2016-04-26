# Module-level setup and teardown.
def setup_module():
    push_exception_handler(handler=lambda *args, **kwds: None, reraise_exceptions=True)
