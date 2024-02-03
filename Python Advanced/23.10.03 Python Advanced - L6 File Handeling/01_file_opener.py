# You are given a file called text.txt with the following text:
# Create a program that opens the file.If the file is found, print 'File found'.
# If the file is not found, print 'File not found'.


# Way to find the path without hardcodding (without / or \):
import os
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, "my_dir", "text.txt")
# -

try:
    file = open("my_dir/text.txt", "r")
    print("Found")
except FileNotFoundError:
    print("File not found")
