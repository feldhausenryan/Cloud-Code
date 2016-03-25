import os
import json

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

#CC: Read a file located in a specified path and print the file to the terminal.
def print_code_segment(filename, path):
    starting_path = os.getcwd()
    os.chdir(path)
    f = open(filename, "r")
    print "-"*80
    print f.read()
    print "-"*80
    f.close()

#CC: Open a file in the current directory and parse the entire contents as JSON. 
def open_and_parse_json(filename):
    f = open(filename, 'r')
    raw_contents = f.read()
    f.close()
    contents = json.loads(raw_contents)
    return contents

def cloud_code_search(input_line):
    database = {}
    return_path = os.getcwd()
    os.chdir("test_table")
    database = open_and_parse_json("test_table.dat")
    os.chdir(return_path)
    
    parsed_input_line = input_line.split()

    word_values = []
    missing = []
    
    for word in parsed_input_line:
        try:
            value = database[word]
            files = value[1]
            sorted(files)
            word_values.append([files, int(value[0]), word])
            #print word_values
        except:
            missing.append(word)

    if len(word_values) == 0:
        return []
    word_values = sorted(word_values, key=lambda index_value: index_value[1], reverse=False)
    itr_list = [0]*(len(word_values)-1)
    match_data = []

    #print "len(itr_list) =  " + str(len(itr_list))
    for least_common_filename in word_values[0][0]:
        match_count = 1
        missing_sub = []
        for itr_list_index in range(0, len(itr_list)):
            #print "itr_list_index = " + str(itr_list_index)
            try:
                while(word_values[itr_list_index+1][0][itr_list[itr_list_index]] < least_common_filename):
                    itr_list[itr_list_index] += 1
            except:
                missing_sub.append(word_values[itr_list_index+1][2])
                continue
            if (word_values[itr_list_index+1][0][itr_list[itr_list_index]] == least_common_filename):
                match_count += 1
                continue
            missing_sub.append(word_values[itr_list_index+1][2])
        match_data.append([truncate(float(match_count)/len(parsed_input_line),3), least_common_filename, missing_sub+missing])

    match_data = sorted(match_data, key=lambda index_value: index_value[0], reverse=True)

    return_values = []
    
    for item in match_data:
        os.chdir("test_segment_base")
        func_to_return = open(item[1], 'r').read()
        os.chdir(return_path)
        return_values.append([item[1], func_to_return])
    return return_values



