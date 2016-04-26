# Collect data from one file
#
def process(filename, table):
    fp = open(filename, 'r')
    mod = os.path.basename(filename)
    if mod[-3:] == '.py':
        mod = mod[:-3]
    table[mod] = list = []
    while 1:
        line = fp.readline()
        if not line: break
        while line[-1:] == '\\':
            nextline = fp.readline()
            if not nextline: break
            line = line[:-1] + nextline
        if m_import.match(line) >= 0:
            (a, b), (a1, b1) = m_import.regs[:2]
        elif m_from.match(line) >= 0:
            (a, b), (a1, b1) = m_from.regs[:2]
        else: continue
        words = line[a1:b1].split(',')
        # print '#', line, words
        for word in words:
            word = word.strip()
            if word not in list:
                list.append(word)
