# 5.	SoftUni Party
# There is a party at SoftUni. Many guests are invited and there are two types of them: Regular and VIP.
# When a guest comes, check if he/she exists in any of the two reservation lists.
# All reservation codes are 8 characters long and all VIP numbers will start with a digit.
# On the first line you will receive the number of guests – N. On the next N lines you will be receiving
# their reservation codes. After that, you will be receiving guests, who came to the party, until you read
# the "END" command.
# In the end, print the number of the guests who did not come to the party and their reservation numbers.
# The VIP guests must be first.
# Both the VIP and the Regular guests must be sorted in ascending order.

N = int(input())

guest_list = set()

for _ in range(N):
    guest_list.add(input())

guest_list_attended = set()

guest_attending = input()

while not guest_attending == "END":
    guest_list_attended.add(guest_attending)

    guest_attending = input()

guests_not_attending = guest_list.difference(guest_list_attended)

print(len(guests_not_attending))

for g in sorted(guests_not_attending):
    print(g)
