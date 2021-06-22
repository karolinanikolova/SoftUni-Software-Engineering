# 5.	Faro Shuffle
# A faro shuffle of a deck of playing cards is a shuffle in which the deck is split exactly in half and then the cards
# in the two halves are perfectly interwoven, such that the original bottom card is still on the
# bottom and the original top card is still on top.
# For example, faro shuffling the list
# ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a
# number of faro shuffles that have to be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number

# ['ace', 'two', 'three', 'four', 'five', 'six']
# ['ace', 'four', 'two', 'five', 'three', 'six']
#
# a b c d | e f g h
# a c e g | b d f h
#
# one two three four
# one three two four

deck = input().split()
shuffles_count = int(input())

left_half = []
right_half = []

half = int(len(deck) / 2)


for shuffle in range(shuffles_count):
    current_deck = []

    left_half = deck[0:half]
    right_half = deck[half::]

    for card in range(len(left_half)):
        current_deck.append(left_half[card])
        current_deck.append(right_half[card])

    deck = current_deck

print(deck)