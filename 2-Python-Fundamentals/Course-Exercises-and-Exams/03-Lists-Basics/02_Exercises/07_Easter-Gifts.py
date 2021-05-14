# Easter Gifts
# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the
# gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if there are any, and change their values to "None".
# •	"Required {gift} {index}"
# o	Replace the value of the current gift on the given index with this gift, if the index is valid.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"

gifts = input().split()
command = input()

while command != 'No Money':
    command = command.split()
    current_gift = command[1]

    if command[0] == 'OutOfStock':
        for gift_index in range(len(gifts)):
            if gifts[gift_index] == current_gift:
                gifts[gift_index] = 'None'

    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(gifts):
            gifts[int(command[2])] = current_gift

    elif command[0] == 'JustInCase':
        gifts[-1] = current_gift
    # gifts.pop() - deletes last element of list
    # gifts.append(current_gift)

    command = input()

while 'None' in gifts:
    gifts.remove('None')

print(" ".join(gifts))

# for gift in gifts:
#     if gift != 'None':
#         print(gift, end = ' ')