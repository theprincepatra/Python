#program to print the contents of a directory using the OS module

import os 

# Specify the directory you want to list 
directory_path = '/ '
# list all the files and directories in the specified path

contents = os.listdir(directory_path)

# print each file and directory name
for item in contents:
    print(item)
