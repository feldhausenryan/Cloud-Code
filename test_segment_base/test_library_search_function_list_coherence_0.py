# Module-level setup and teardown.
def setup():
    # If a trait exception occurs, fail the test.
    push_exception_handler( handler = lambda o,t,ov,nv: None,
                            reraise_exceptions = True,
                            main = True,
                          )
