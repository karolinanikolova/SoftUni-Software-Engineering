# 5.	Word Count
# Write a program that reads a list of words from the file words.txt and finds how many times each
# of the words is contained in another file text.txt. Matching should be case-insensitive.
# The results should be written to another text files. Sort the words by frequency in descending order.

# import re
#
# with open("words.txt", "w") as file:
#     file.write('quick is fault')
#
# with open("input.txt", "w") as file:
#     file.write("-I was quick to judge him, but it wasn't his fault.\n")
#     file.write("-Is this some kind of joke?! Is it?\n")
#     file.write("-Quick, hide here...It is safer.\n")
#
# with open("words.txt") as file:
#     searched_words = file.read().split()
#
# occurrences= {}
#
# with open("input.txt") as file:
#     content = file.read().lower()
#     for s_word in searched_words:
#         result = re.findall(rf"(?<=(\-|\s)){s_word}(?=(\.|))", content)
#         occurrences[s_word] = len(result)
#
# sorted_result = sorted(occurrences.items(), key=lambda x: -x[1])
#
# for key, value in sorted_result:
#     print(f"{key} - {value}")

# Option 20

def get_file_content(path):
    with open(path, 'r') as data:
        data = ''.join(data.readlines())
        return pattern.findall(data.lower())


def write_to_file(data):
    for k, v in data:
        output_data = f'{k} - {v}'
        with open('output.txt', 'a') as file:
            file.write(output_data)
            file.write("\n")


import re

pattern = re.compile(r"[a-zA-Z\']+")

path_to_words = 'words.txt'
path_to_input = 'input.txt'

get_words = get_file_content(path_to_words)
get_text = get_file_content(path_to_input)

my_dict = {word: get_text.count(word) for word in get_words if word in get_text}
sorted_list = sorted(my_dict.items(), key=lambda x: -x[1])

write_to_file(sorted_list)