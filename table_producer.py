import json
import os

#Example C:\Users\User\Google Drive

def open_and_parse_json(filename):
    f = open(filename, 'r')
    raw_contents = f.read()
    f.close()
    contents = json.loads(raw_contents)
    return contents

def create_default_configuration():
    f = open("configuration.txt", 'w+')
    f.write('{"table_path": "test_table", "code_base_path": "test_code_base", "table_name": "test_table.dat"}')
    f.close()

def create_default_table(table_name):
    f = open(table_name, 'w+')
    f.write('{}')
    f.close()
    
if __name__ == "__main__":
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

        print "Moving to Table Directory...\t\t",
        try:
            os.chdir(table_path)
            print "Success"
        except:
            os.mkdir(table_path)
            os.chdir(table_path)
            create_default_table(table_filename)
            os.chdir("..")
            print "Failure - Created Path and Empty Table"
            continue

        print "Opening Talbe...\t\t\t",
        try:
            table = open_and_parse_json(table_filename)
            print "Success"
        except:
            create_default_table(table_filename)
            os.chdir("..")
            print "Failure - Created Empty Table"
            continue

        print "-----------------------------------------------"
        print table
        break
