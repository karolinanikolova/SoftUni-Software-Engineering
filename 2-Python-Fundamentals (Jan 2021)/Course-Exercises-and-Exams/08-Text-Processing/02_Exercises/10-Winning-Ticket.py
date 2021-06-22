# 10.	*Winning Ticket
# Lottery is exciting. What is not, is checking a million tickets for winnings only by hand.
# So, you are given the task to create a program which automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces. You need to check every one of them if it has a winning combination of symbols.
# A valid ticket should have exactly 20 characters. The winning symbols are '@', '#', '$' and '^'.
# But in order for a ticket to be a winner the symbol should uninterruptedly repeat for at least 6 times in both the tickets left half and the tickets right half.
# For example, a valid winning ticket should be something like this:
# "Cash$$$$$$Ca$$$$$$sh"
# The left half "Cash$$$$$$" contains "$$$$$$", which is also contained in the tickets right half "Ca$$$$$$sh".
# A winning ticket should contain symbols repeating up to 10 times in both halves, which is considered a Jackpot (for example: "$$$$$$$$$$$$$$$$$$$$").

winning_symbols = ["@", "#", "$", "^"]


def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if ticket.count(winning_symbol) == 20:
            print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
            return True
    return False


def is_winning_ticket(ticket):
    left_half_ticket = ticket[:10]
    right_half_ticket = ticket[10:]
    for winning_symbol in winning_symbols:
        if winning_symbol * 6 in left_half_ticket and winning_symbol * 6 in right_half_ticket:
            print(f"ticket \"{ticket}\" - {min(left_half_ticket.count(winning_symbol), right_half_ticket.count(winning_symbol))}{winning_symbol}")
            return True
    return False


tickets = [ticket.strip() for ticket in input().split(",")]

for ticket in tickets:

    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    if is_jackpot(ticket):
        continue

    if is_winning_ticket(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")





