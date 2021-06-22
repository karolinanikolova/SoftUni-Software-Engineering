# Programming Fundamentals Final Exam Retake 15.08.2020
# Problem 3. The Pianist
# You are a pianist and you like to keep a list of your favorite piano pieces. Create a program, to help you organize it
# and add, change, remove pieces from it!
# On the first line of the standard input you will receive an integer n – the number of pieces that you will initially have.
# On the next n lines the pieces themselves will follow with their composer and key, separated by "|" in the following format:
# {piece}|{composer}|{key}
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
# •	Add|{piece}|{composer}|{key}
# o	You need to add the given piece with the information about it to the other pieces
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# o	If the piece is not in the collection, print:
# "{piece} by {composer} in {key} added to the collection!"
# •	Remove|{piece}
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	If the piece is not in the collection, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	ChangeKey|{piece}|{new key}
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	If the piece is not in the collection, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command you need to print all pieces in your collection, sorted by their name and by the
# name of their composer in alphabetical order, in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"

n = int(input())

pieces = {}

for _ in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

command = input()

while not command == "Stop":
    command = command.split("|")
    action = command[0]
    piece = command[1]

    if action == "Add":
        composer = command[2]
        key = command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece in pieces:
            pieces.pop(piece)
#             del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        if piece in pieces:
            new_key = command[2]
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_piece_composer_alphabetical = sorted(pieces.items(), key= lambda kvp: (kvp[0], kvp[1]["composer"]))

for piece, piece_data in sorted_piece_composer_alphabetical:
    composer = piece_data["composer"]
    key = piece_data["key"]
    print(f"{piece} -> Composer: {composer}, Key: {key}")

# # Solution 2 (with classes)
#
# class Piece:
#     def __init__(self, piece_name, composer, key):
#         self.piece_name = piece_name
#         self.composer = composer
#         self.key = key
#
#
# n = int(input())
# pieces = []
#
# for _ in range(n):
#     piece_name, composer, key = input().split("|")
#     piece = Piece(piece_name, composer, key)
#     pieces.append(piece)
#
# command = input()
#
# while not command == "Stop":
#     command = command.split("|")
#     action = command[0]
#     piece_name = command[1]
#
#     if action == "Add":
#         composer = command[2]
#         key = command[3]
#         if piece_name in [p.piece_name for p in pieces]:
#             print(f"{piece_name} is already in the collection!")
#         else:
#             piece = Piece(piece_name, composer, key)
#             pieces.append(piece)
#             print(f"{piece_name} by {composer} in {key} added to the collection!")
#
#     elif action == "Remove":
#         if piece_name in [p.piece_name for p in pieces]:
#             piece_to_remove = [p for p in pieces if piece_name == p.piece_name][0]
#             pieces.remove(piece_to_remove)
#             print(f"Successfully removed {piece_name}!")
#         else:
#             print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#     elif action == "ChangeKey":
#         if piece_name in [p.piece_name for p in pieces]:
#             new_key = command[2]
#             piece_to_change = [p for p in pieces if piece_name == p.piece_name][0]
#             piece_to_change.key = new_key # референтен тип данни. Ако променим обекта, то обектът в листа директно се променя също.
#             print(f"Changed the key of {piece_name} to {new_key}!")
#         else:
#             print(f"Invalid operation! {piece_name} does not exist in the collection.")
#
#     command = input()
#
#
# sorted_piece_composer_alphabetical = sorted(pieces, key=lambda p: (p.piece_name, p.composer))
#
# for piece in sorted_piece_composer_alphabetical:
#     print(f"{piece.piece_name} -> Composer: {piece.composer}, Key: {piece.key}")
