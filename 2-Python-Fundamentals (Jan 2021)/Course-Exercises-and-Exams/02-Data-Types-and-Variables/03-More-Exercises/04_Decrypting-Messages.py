# 4.	Decrypting Messages
# You will receive a key (integer) and n characters afterward. Add the key to each of the characters and append
# them to a message. At the end print the message, which you decrypted.

key = int(input())
number_of_lines = int(input())

message = ''

for line in range(1, number_of_lines+1):
    character = input()
    decrypter_character = chr(ord(character) + key)
    message += decrypter_character

print(message)

