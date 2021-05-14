# 3. Characters in Range
# Write a function that receives two characters and returns a single string with all the characters in between them according to the ASCII code.

def get_characters_in_range(first_char, second_char):
    start_int = ord(first_char)
    end_int = ord(second_char)
    characters_in_range = []

    for character in range(start_int + 1, end_int):
        characters_in_range.append(chr(character))

    return characters_in_range


first_character = input()
second_character = input()

result = get_characters_in_range(first_character, second_character)

print(' '.join(result))



