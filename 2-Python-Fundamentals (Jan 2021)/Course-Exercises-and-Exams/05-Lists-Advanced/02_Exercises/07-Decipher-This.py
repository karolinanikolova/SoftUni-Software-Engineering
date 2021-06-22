# 7.	Decipher This!
# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
# For each word:
# •	the second and the last letter are switched (e.g. Hello becomes Holle)
# •	the first letter is replaced by its character code (e.g. H becomes 72)

secret_message = input().split()

for word in secret_message:
    # first_letter_coded = "".join([character for character in word if character.isdigit()])
    first_letter_coded = ''
    for character in word:
        if character.isdigit():
            first_letter_coded += character

    first_letter_decoded = chr(int(first_letter_coded))
    current_word = first_letter_decoded + word[len(first_letter_coded):]
    # current_word = word.replace(first_letter_coded, first_letter_decoded)
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)} ", end="")
