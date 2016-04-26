# make it case insensitive
def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m:
        return ''
    prefix = m[0]
    for item in m:
        for i in range(len(prefix)):
            if prefix[:i + 1].lower() != item[:i + 1].lower():
                prefix = prefix[:i]
                if i == 0:
                    return ''
                break
    return prefix
