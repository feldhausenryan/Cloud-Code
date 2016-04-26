##  I am thinking about this one.  Needs a change to reportlab to
##  work.
def encryptDocTemplate(dt,
                  userPassword, ownerPassword=None,
                  canPrint=1, canModify=1, canCopy=1, canAnnotate=1,
                       strength=40):
    "For use in Platypus.  Call before build()."
    raise Exception("Not implemented yet")
