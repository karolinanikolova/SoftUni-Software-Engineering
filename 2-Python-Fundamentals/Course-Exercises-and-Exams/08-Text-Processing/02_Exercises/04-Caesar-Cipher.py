# 4.	 Caesar Cipher
# Write a program that returns an encrypted version of the same text.
# Encrypt the text by shifting each character with three positions forward.
# For example A would be replaced by D, B would become E, and so on. Print the encrypted text.

text = input()

encrypted_text = [chr(ord(character) + 3) for character in text]

print("".join(encrypted_text))

