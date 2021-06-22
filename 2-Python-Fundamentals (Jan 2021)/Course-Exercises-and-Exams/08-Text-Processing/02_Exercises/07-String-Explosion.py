# 7.	 String Explosion
# Explosions are marked with '>'. Immediately after the mark, there will be an integer, which signifies the strength of the explosion.
# You should remove x characters (where x is the strength of the explosion), starting after the punch character ('>').
# If you find another explosion mark ('>') while you’re deleting characters, you should add the strength to your previous explosion.
# When all characters are processed, print the string without the deleted characters.
# You should not delete the explosion character – '>', but you should delete the integers, which represent the strength.

string = input()


def remove_char_at_index(i, s):
    return s[:i] + s[i+1:]


index = 0
strength = 0

while index < len(string):
    if string[index] == ">":
        strength += int(string[index + 1])

        i = index + 1

        while strength > 0 and i < len(string) and not string[i] == ">":
            string = remove_char_at_index(i, string)
            strength -= 1

    index += 1

print(string)
