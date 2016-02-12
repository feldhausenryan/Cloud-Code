import json
import os
import re

#Example C:\Users\User\Google Drive

def open_and_parse_json(filename):
    f = open(filename, 'r')
    raw_contents = f.read()
    print raw_contents
    f.close()
    contents = json.loads(raw_contents)
    return contents

def save_json_overwrite(filename, content):
    f = open(filename, "w+")
    f.write(json.dumps(content))
    f.close
    
def create_default_configuration():
    f = open("configuration.txt", 'w+')
    f.write('{"table_path": "test_table", "code_base_path": "test_code_base", "table_name": "test_table.dat"}')
    f.close()

def create_default_table(table_name):
    f = open(table_name, 'w+')
    f.write('{}')
    f.close()

def make_table():
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
                    table = read_python_file(file_name, table)
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
            return
        try:
            table[stripped_word].append(filename)
        except:
            table[stripped_word] = []
            table[stripped_word].append(filename)
    return table
    
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


#TODO HERE  PARSE OUT THE COMMENT TO WORDS
#           MAKE A NEW FILE FOR EACH FUNCTION (temp  + temp2)
def read_python_file(filename, table):
    print "Python file : " + filename
    f = open(filename, 'r')
    state = "neutral"
    temp = ""
    temp2 = ""
    for line in f:
        #print line[:3], line[-4:-1], 'TESTETsTSTE'
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
        elif line[0] == "#":
            temp += line[1:]
            #RUN
            state = "post_comment"
        elif line[:3] == "'''" and line[-4:-1] == "'''":
            state = "post_comment"
            temp = line[3:-4]
            #RUN
        elif line[:3] == '"""' and line[-4:-1] == '"""':
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
            state = "live_code"
            temp2 += line
        elif state == "live_code" and (line[0] == " "):
            temp2 += line
        elif state == "live_code":
            state = "neutral"
            print "--------------------------------------COMMENT-------------------------------------------"
            print temp.strip()
            print "---------------------------------------CODE---------------------------------------------"
            print temp2[:-1].strip()
            print "========================================================================================"
            temp = ""
            temp2 = ""
            #RUN
        elif state == "post_comment":
            state = "neutral"
            temp = ""
            temp2 = ""
        else:
            state = "neutral"
            
        

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
    table = make_table()
    print "-----------------------------------------------"
    print "Saving...\t\t\t\t",
    os.chdir(starting_path)
    os.chdir(table_path)
    save_json_overwrite(table_filename, table)
    print "Success"

    
