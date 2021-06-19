# 3.	File Writer
# Create a program that creates a file called my_first_file.txt.
# In that file write a single line with the content: 'I just created my first file!'

# file = open("my_first_file.txt", "w")
#
# file.write('I just created my first file!')
#
# file.close()

# With manager is better than just open as it automatically closes file
with open("my_first_file.txt", "w") as file:
    file.write('I just created my first file!')
