# 2.	No Vowels
# Using a comprehension write a program that receives a text and removes all the vowels from it,
# case insensitive. Print the new text string after removing the vowels.
# The vowels that should be considered are 'a', 'o', 'u', 'e' and 'i'.

# text = input()
#
# text_without_vowels = ''.join([character for character in text if character.lower() not in 'aouei'])
#
# print(text_without_vowels)

# Option 2 - with functions

def is_vowel(character):
    if character.lower() in 'aouei':
        return True
    return False


text_without_vowels = ''.join([character for character in input() if not is_vowel(character)])

print(text_without_vowels)