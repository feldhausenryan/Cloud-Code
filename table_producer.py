import json
import os
import re

#Example C:\Users\User\Google Drive

def open_and_parse_json(filename):
    f = open(filename, 'r')
    raw_contents = f.read()
    f.close()
    contents = json.loads(raw_contents)
    return contents

def save_json_overwrite(filename, content):
    f = open(filename, "w+")
    f.write(json.dumps(content))
    f.close
    
def create_default_configuration():
    f = open("configuration.txt", 'w+')
    f.write('{"table_path": "test_table", "code_base_path": "test_code_base", "table_name": "test_table.dat", "segment_path": "test_segment_base"}')
    f.close()

def create_default_table(table_name):
    f = open(table_name, 'w+')
    f.write('{}')
    f.close()

def make_table(configuration):
    #The table to fill up
    table = {}

    #Create an array which will contain all the directories to visit.
    directories = []

    #Add the current directory as the starting point
    directories.append(os.getcwd())

    while(len(directories) > 0):
        #Fetch the next directory to scan
        directory = directories.pop()

        #Move to the new directory
        os.chdir(directory)

        #Iterate through the file names in the directory
        for file_name in os.listdir(os.getcwd()):

            #Split the extensions apart from the file names
            split_file_name = file_name.split(".")
            
            #If there is no extension to a file...
            if (len(split_file_name) == 1):
                #If it is a not a directory...
                if (os.path.isdir(file_name) == False):
                    #Extensionless file
                    #print "Extensionless File"
                    pass
                else:
                    #Directory
                    full_sub_directory_path = os.path.realpath(file_name)
                    directories.append(full_sub_directory_path)
            #If there is an extension to the file...
            if (len(split_file_name) == 2):
                #If that extension is a python file...
                if (split_file_name[1] == "py"):
                    #Python file
                    table = read_python_file(file_name, table, configuration)
                #If that extension is not a python file...
                else:
                    #Not a python file
                    #print "Other File"
                    pass
    return table

def distribute_words_from_line(input_line, filename, table):
    non_alphanumeric_character_threshold = 3
    for word in input_line.split():
        stripped_word = (re.sub(r'\W+', '', word)).lower()
        if (len(stripped_word)+non_alphanumeric_character_threshold < len(word)):
            return table
        try:
            table[stripped_word].append(filename)
        except:
            table[stripped_word] = []
            table[stripped_word].append(filename)
    return table

def code_segments_to_file(table, index_of_code_segments, comment, code, filename, configuration):
    segment_filename = filename.split('.')[0]+"_"+str(index_of_code_segments)+".py"
    print segment_filename
    #print comment
    #print code
    current_directory = os.getcwd()
    segment_base_directory = configuration["segment_path"]
    os.chdir(segment_base_directory)
    f = open(segment_filename, "w+")
    f.write("'''\n"+comment.strip()+"\n'''\n")
    f.write(code)
    f.close()
    if comment.strip() == "":
        os.chdir(current_directory)
        return table
    table = distribute_words_from_line(comment, segment_filename, table)
    os.chdir(current_directory)    
    return table

"""
def read_python_file(filename, table):
    print "Python file : " + filename
    f = open(filename, 'r')
    switch = 0
    for line in f:
        if line[0] == "#":
            switch = 1
            table = distribute_words_from_line(line[1:], filename, table)
        elif line[0:3] == "'''":
            switch = 2
            table = distribute_words_from_line(line[3:-3], filename, table)
    return table
"""

#TODO HERE  PARSE OUT THE COMMENT TO WORDS
#           MAKE A NEW FILE FOR EACH FUNCTION (temp  + temp2)
def read_python_file(filename, table, configuration):
    index_of_code_segments = 0
    print "Python file : " + filename
    f = open(filename, 'r')
    state = "neutral"
    temp = ""
    temp2 = ""
    
    for line in f:
        if state == "long_comment_a":
            if line[-4:-1] == "'''":
                temp += line[:-4]
                #RUN
                state = "post_comment"
            else:
                temp += line
        elif state == "long_comment_b":
            if line[-4:-1] == '"""':
                temp += line[:-4]
                #RUN
                state = "post_comment"
            else:
                temp += line
        elif (line[0] == "#") and state == "live_code":
            table = code_segments_to_file(table, index_of_code_segments, temp, temp2, filename, configuration)
            state = "post_comment"
            temp = line
            temp2= ""
            index_of_code_segments += 1
        elif (line[:3] == "'''") and state == "live_code":
            table = code_segments_to_file(table, index_of_code_segments, temp, temp2, filename, configuration)
            state = "long_comment_a"
            temp = line
            temp2= ""
            index_of_code_segments += 1
        elif (line[:3] == '"""') and state == "live_code":
            table = code_segments_to_file(table, index_of_code_segments, temp, temp2, filename, configuration)
            state = "long_comment_b"
            temp = line
            temp2= ""
            index_of_code_segments += 1
        elif line[0] == "#" and state != "long_comment_a" and state != "long_comment_b":
            temp += line[1:]
            #RUN
            state = "post_comment"
        elif line[:3] == "'''" and line[-4:-1] == "'''" and len(line) > 4:
            state = "post_comment"
            temp = line[3:-4]
            #RUN
        elif line[:3] == '"""' and line[-4:-1] == '"""' and len(line) > 4:
            state = "post_comment"
            temp = line[3:-4]
            #RUN
        elif line[:3] == "'''":
            state = "long_comment_a"
            temp = line[3:]
        elif line[:3] == '"""':
            state = "long_comment_b"
            temp = line[3:]
        elif state == "post_comment" and line[:3] == "def":
            if filename == "Challenge7.py":
                print line
            state = "live_code"
            temp2 += line
        elif state == "live_code" and (line[0] == " " or len(line.strip()) == 0):
            #if filename == "Challenge7.py":
                #print line
                #print line[0]+"<-- line[0]\t\t\t"+str(len(line.strip()))+"<-- len"
            temp2 += line
        elif state == "live_code":
            state = "neutral"
            #print "--------------------------------------COMMENT-------------------------------------------"
            #print temp.strip()
            #print "---------------------------------------CODE---------------------------------------------"
            #print temp2[:-1].strip()
            #print "========================================================================================"
            table = code_segments_to_file(table, index_of_code_segments, temp, temp2, filename, configuration)
            temp = ""
            temp2 = ""
            index_of_code_segments += 1
            #RUN
        elif state == "post_comment":
            state = "neutral"
            temp = ""
            temp2 = ""
        else:
            state = "neutral"
        
        #if filename == "lab9_start.py":
        #    spaces = " "*(150-len(line.strip()))
        #    print line.strip()+spaces+state
    if state == "live_code":
        table = code_segments_to_file(table, index_of_code_segments, temp, temp2, filename, configuration)
        temp = ""
        temp2 = ""
        index_of_code_segments += 1
    return table
            
        

if __name__ == "__main__":
    starting_path = os.getcwd()
    
    while(1):
        print ""
        print "Opening Configuration File...\t\t",
        configuration_filename = "configuration.txt"
        try:
            configuration = open_and_parse_json(configuration_filename)
            print "Success"
        except:
            create_default_configuration()
            print "Failure - Created Default Configuration"
            continue
            
        print "Getting Table Path...\t\t\t",
        try:
            table_path = configuration["table_path"]
            print "Success"
        except:
            create_default_configuration()
            print "Failure - Created Default Configuration"
            continue

        print "Getting Table Name...\t\t\t",
        try:
            table_filename = configuration["table_name"]
            print "Success"
        except:
            create_default_configuration()
            print "Failure - Created Default Configuration"
            continue

        print "Checking Table Directory...\t\t",
        try:
            os.chdir(table_path)
            os.chdir(starting_path)
            print "Success"
        except:
            os.mkdir(table_path)
            print "Failure - Created Path"
            continue

        print "Getting Segment Path Name...\t\t",
        try:
            segment_path = configuration["segment_path"]
            print "Success"
        except:
            create_default_configuration()
            print "Failure - Created Default Configuration"
            continue

        print "Checking Segment Directory...\t\t",
        try:
            os.chdir(segment_path)
            configuration["segment_path"] = os.getcwd()
            os.chdir(starting_path)
            print "Success"
        except:
            os.mkdir(segment_path)
            print "Failure - Created Path"
            continue
        
        '''
        print "Opening Table...\t\t\t",
        try:
            table = open_and_parse_json(table_filename)
            print "Success"
        except:
            create_default_table(table_filename)
            os.chdir("..")
            print "Failure - Created Empty Table"
            continue
        '''

        print "Getting Code Base Path...\t\t",
        try:
            code_base_path = configuration["code_base_path"]
            print "Success"
        except:
            create_default_configuration()
            print "Failure - Created Default Configuration"
            raise

        print "Checking Code Base Path...\t\t",
        try:
            os.chdir(code_base_path)
            os.chdir(starting_path)
            print "Success"
        except:
            os.mkdir(code_base_path)
            print "Failure - Created Path"

        print "-----------------------------------------------"
        break

    print "Making Database..." 
    os.chdir(code_base_path)
    table = make_table(configuration)
    print "-----------------------------------------------"
    print "Saving...\t\t\t\t",
    os.chdir(starting_path)
    os.chdir(table_path)
    save_json_overwrite(table_filename, table)
    print "Success"

    
