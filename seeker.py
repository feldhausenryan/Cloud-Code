import os
import json

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

#CC: Open a file in the current directory and overwrite the entire file with the listed contents.
def save_json_overwrite(filename, content):
    f = open(filename, "w+")
    f.write(json.dumps(content))
    f.close

#No relevant cloud code use
def create_default_configuration():
    f = open("configuration.txt", 'w+')
    f.write('{"table_path": "test_table", "code_base_path": "test_code_base", "table_name": "test_table.dat", "segment_path": "test_segment_base"}')
    f.close()

#CC: Create an empty JSON file in the current directory with a given name. 
def create_default_table(table_name):
    f = open(table_name, 'w+')
    f.write('{}')
    f.close()

if __name__ == "__main__":
    starting_path = os.getcwd()
    database = {}
    configuration = {}

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
            database = open_and_parse_json(table_filename)
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
            print "Failure"
            os.mkdir(segment_path)
            print "Failure - Created Path"
            continue

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

    while(1):

        '''
        input_line = raw_input("SEARCH : ")
        parsed_input_line = input_line.split()
        
        word_values = []
        missing = []
        existing = []
        for word in parsed_input_line:
            try:
                value = database[word]
                word_values.append([set(value[1]),value[0]])
                existing.append(word)
            except:
                missing.append(word)
                continue

        if len(word_values) == 0:
            print "No Results, no words matched at all"
            continue
        sorted(word_values, key=lambda index_value: index_value[1], reverse=True)
        intersection = word_values[0][0]
        for value in word_values:
            intersection = intersection.intersection(value[0])
        print "Searched: "+str(existing)+"\t\tMissing: "+str(missing)
        print "Results: "+str(len(intersection))
        for value in intersection:
            print_code_segment(value, configuration["segment_path"])

        '''

        input_line = raw_input("SEARCH : ").lower()
        parsed_input_line = input_line.split()

        word_values = []
        missing = []
        
        for word in parsed_input_line:
            try:
                value = database[word]
                files = value[1]
                sorted(files)
                word_values.append([(files, int(value[0]))])
            except:
                missing.append(word)

        if len(word_values) == 0:
            print "No Results. No Words Matched."
            continue
        sorted(word_values, key=lambda index_value: index_value[1], reverse=True)


        for least_common_filename in word_values[0][0]:
            itr_list = [0,True]*(len(word_values)-1)
            
            
        
