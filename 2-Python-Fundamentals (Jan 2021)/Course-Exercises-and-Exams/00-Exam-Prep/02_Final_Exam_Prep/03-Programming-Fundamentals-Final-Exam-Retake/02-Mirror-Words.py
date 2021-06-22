# Problem 2. Mirror words
#
# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there,
# it`s different and a lot more fun! You, of course, are a participant and you are eager to show the competition that
# you are the best, so go ahead, learn the rules and win!
# On the first line of the input you will be given a text string. In order to win the competition you have to find all
# hidden word pairs, read them and mark the ones that are mirror images of each other.
# First of all you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backwards is the same as the first word and vice versa (casing matters!), then they are a
# match and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, etc…"

import re

text = input()

pattern = r"(#|@)[A-Za-z]{3,}\1\1[A-Za-z]{3,}\1"

valid_word_pairs = [match.group() for match in re.finditer(pattern, text)]
mirror_words = []

if valid_word_pairs:
    print(f"{len(valid_word_pairs)} word pairs found!")
    for word_pair in valid_word_pairs:
        first_word = word_pair[:int(len(word_pair)/2)]
        second_word = word_pair[int(len(word_pair)/2):]
        if first_word[::-1] == second_word:
            mirror_word = first_word[1:len(first_word)-1]
            mirror_words.append(mirror_word + " <=> " + mirror_word[::-1])
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")
