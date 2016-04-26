# Start of msdn sample port...
# make_item_enum replaces the sample's entire EnumIDList.cpp :)
def make_item_enum(level, flags):
    pidls = []
    nums = """zero one two three four five size seven eight nine ten""".split()
    for i, name in enumerate(nums):
        size = random.randint(0,255)
        sides = 1
        while sides in [1,2]:
            sides = random.randint(0,5)
        is_folder = (i % 2) != 0
        # check the flags say to include it.
        # (This seems strange; if you ask the same folder for, but appear
        skip = False
        if not (flags & shellcon.SHCONTF_STORAGE):
            if is_folder:
                skip = not (flags & shellcon.SHCONTF_FOLDERS)
            else:
                skip = not (flags & shellcon.SHCONTF_NONFOLDERS)
        if not skip:
            data = dict(name=name, size=size, sides=sides, level=level, is_folder=is_folder)
            pidls.append([pickle.dumps(data)])
    return NewEnum(pidls, shell.IID_IEnumIDList)
