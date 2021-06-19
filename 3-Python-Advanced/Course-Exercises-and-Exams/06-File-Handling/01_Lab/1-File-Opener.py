# You are given a file called text.txt with the following text.txt
# Create program that opens the file. If the file is found, print 'File found'.
# If the file is not found, print 'File not found'.

# from os import path
#
# # First solution
# if path.exists("text.txt"):
#     print("File found")
# else:
#     print("File not found")

# Second solution solution
try:
    file = open("text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")

file.close()
