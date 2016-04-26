# Called with a dictionary argument of the form
# {'*.c':'C source files', '*.txt':'Text Files', '*':'All files'}
# returns a string which can be used to configure the fsbox file types
# in an ExFileSelectBox. i.e.,
# '{{*} {* - All files}} {{*.c} {*.c - C source files}} {{*.txt} {*.txt - Text Files}}'
def FileTypeList(dict):
    s = ''
    for type in dict.keys():
        s = s + '{{' + type + '} {' + type + ' - ' + dict[type] + '}} '
    return s
