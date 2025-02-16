# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os

# Specify the directory (use '.' for the current directory)
directory_path = "/Apps"

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
