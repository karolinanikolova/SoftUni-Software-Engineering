# 4.	Number Beggars
# Your task here is pretty simple: given a list of numbers and a number of beggars, you are supposed to return a
# list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.
# For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5], the second collects [2,4].
# The same list with 3 beggars would produce a better outcome for the second beggar: 5, 7 and 3,
# as they will respectively take [1, 4], [2, 5] and [3].
# Also note that not all beggars have to take the same amount of "offers",
# meaning that the length of the list is not necessarily a multiple of n; length can be even shorter,
# in which case the last beggars will of course take nothing (0).

earnings_list = input().split(", ")
beggars_count = int(input())


earnings_per_beggar = []

start_index = 0

for beggar in range(beggars_count):
    current_beggar_earnings = 0

    for earning in range(start_index, len(earnings_list), beggars_count):
        current_beggar_earnings += int(earnings_list[earning])

    earnings_per_beggar.append(current_beggar_earnings)

    start_index += 1

print(earnings_per_beggar)