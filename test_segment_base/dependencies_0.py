# fail after some time:
def wait_and_fail(t):
    import time
    time.sleep(t)
    return 1/0
