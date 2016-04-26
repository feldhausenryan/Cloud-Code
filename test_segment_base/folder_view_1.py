# We construct a PIDL from a pickle of a dict - turn it back into a
# dict (we should *never* be called with a PIDL that the last elt is not 
# ours, so it is safe to assume we created it (assume->"ass" = "u" + "me" :)
def pidl_to_item(pidl):
    # Note that only the *last* elt in the PIDL is certainly ours,
    # but it contains everything we need encoded as a dict.
    return pickle.loads(pidl[-1])
