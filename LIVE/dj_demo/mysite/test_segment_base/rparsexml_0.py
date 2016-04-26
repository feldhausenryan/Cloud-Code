#replacelist = []
def unEscapeContentList(contentList):
    result = []
    from string import replace
    for e in contentList:
        if "&" in e:
            for (old, new) in replacelist:
                e = replace(e, old, new)
        result.append(e)
    return result
