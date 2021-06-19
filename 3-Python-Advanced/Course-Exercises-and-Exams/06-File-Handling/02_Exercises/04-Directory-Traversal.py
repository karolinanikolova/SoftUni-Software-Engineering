# 4.	Directory Traversal
# Write a program that traverses a given directory for all files.
# Search through the first level of the directory only and write information about each
# found file in report.txt. The files should be grouped by their extension.
# Extensions should be ordered by name alphabetically.
# The files with extensions should also be sorted by name. report.txt should be saved on the Desktop.
# Ensure the desktop path is always valid, regardless of the user.

import os

# Input is the argument which is which directory to traverse. If we want current then it's .
_, _, files = next(os.walk(input())) # Underscore because we're not interested in the first two outputs of function

by_extension = {}

for file in files:
    ext = file.split('.')[-1]

    if ext not in by_extension:
        by_extension[ext] = []

    by_extension[ext].append(file)

with open(os.path.expanduser("~/Desktop/report.txt"), 'w') as out_file:

    for ext in sorted(by_extension.keys()):
        files = sorted(by_extension[ext])
        out_file.write(f'.{ext}\n')

        for file in files:
            out_file.write(f'- - - {file}\n')
