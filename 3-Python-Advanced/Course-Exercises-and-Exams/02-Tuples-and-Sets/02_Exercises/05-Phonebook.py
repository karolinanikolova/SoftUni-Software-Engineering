# 5.	Phonebook
# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of a contact by name and print its details in format
# "{name} -> {number}". In case the contact isn't found, print "Contact {name} does not exist."

# data = input()
#
# phonebook = {}
#
# while not data.isdigit():
#     name, phone_number = data.split('-')
#     phonebook[name] = phone_number
#
#     data = input()
#
# for _ in range(int(data)):
#     contact = input()
#
#     if phonebook.get(contact):
#         print(f"{contact} -> {phonebook[contact]}")
#     else:
#         print(f"Contact {contact} does not exist.")

# With functions

from typing import Dict, Tuple


def fill_phonebook() -> Tuple[Dict[str, str], int]:
    data = input()

    phonebook = {}

    while not data.isdigit():
        name, phone_number = data.split('-')
        phonebook[name] = phone_number

        data = input()

    return phonebook, int(data)


def search_contact(contact, phonebook):
    if phonebook.get(contact):
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")


phonebook, iterations_count = fill_phonebook()

for _ in range(iterations_count):
    contact = input()
    search_contact(contact, phonebook)

