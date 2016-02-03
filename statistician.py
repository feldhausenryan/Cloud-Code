import os
import re

#Example C:\Users\User\Google Drive

big_dict = {}

def read_python_file(filename):
    global big_dict
    f = open(filename, 'r')
    for line in f:
        if line[0] == "#":
            for word in line[1:].split():
                stripped_word = (re.sub(r'\W+', '', word)).lower()
                #stripped_word = word
                if (len(stripped_word)+3 < len(word)):
                    continue
                try:
                    big_dict[stripped_word] += 1
                except:
                    big_dict[stripped_word] = 1

if __name__ == "__main__":
    #Obtain input directory name from user
    input_path = raw_input("Directory Path: ")

    #If this is not a valid input...
    if (os.path.isdir(input_path) == False):
        #Throw an exception and end the program
        raise NameError("Invalid Directory Name")

    #Create an array which will contain all the directories to visit.
    directories = []

    directories.append(input_path)

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
                    read_python_file(file_name)
                #If that extension is not a python file...
                else:
                    #Not a python file
                    #print "Other File"
                    pass
