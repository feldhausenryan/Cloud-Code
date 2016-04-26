# Compute closure (this is in fact totally general)
#
def closure(table):
    modules = table.keys()
    #
    # Initialize reach with a copy of table
    #
    reach = {}
    for mod in modules:
        reach[mod] = table[mod][:]
    #
    # Iterate until no more change
    #
    change = 1
    while change:
        change = 0
        for mod in modules:
            for mo in reach[mod]:
                if mo in modules:
                    for m in reach[mo]:
                        if m not in reach[mod]:
                            reach[mod].append(m)
                            change = 1
    #
    return reach
