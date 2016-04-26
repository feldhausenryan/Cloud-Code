# Tests are built around these assumed context defaults.
# test_main() restores the original context.
def init():
    global ORIGINAL_CONTEXT
    ORIGINAL_CONTEXT = getcontext().copy()
    DefaultTestContext = Context(
        prec = 9,
        rounding = ROUND_HALF_EVEN,
        traps = dict.fromkeys(Signals, 0)
        )
    setcontext(DefaultTestContext)
