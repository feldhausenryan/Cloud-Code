# Manipulating text files ------
def find_line(lines,findstr):
    i_find_list = [lines.index(line) for line in lines if line.find(findstr)>-1]
    if len(i_find_list):
        return i_find_list[0]
    return i_find_list
