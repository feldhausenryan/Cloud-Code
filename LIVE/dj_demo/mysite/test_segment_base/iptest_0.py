# ------------------------------------------------------------------------------
# Monkeypatch Xunit to count known failures as skipped.
# ------------------------------------------------------------------------------
def monkeypatch_xunit():
    try:
        knownfailureif(True)(lambda: None)()
    except Exception as e:
        KnownFailureTest = type(e)
    def addError(self, test, err, capt=None):
        if issubclass(err[0], KnownFailureTest):
            err = (SkipTest,) + err[1:]
        return self.orig_addError(test, err, capt)
    Xunit.orig_addError = Xunit.addError
    Xunit.addError = addError
