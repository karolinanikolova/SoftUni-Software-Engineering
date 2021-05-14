# 3.	Football Cards
# Most football fans love it for the goals and excitement. Well, this problem doesn't. ' \
#         'You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players remaining,
# the game is stopped immediately by the referee, and the team with less than 7 players loses.
#
# A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g. the card 'B-7'
# means player #7 from team B received a card.
# The task: Given a list of cards (could be empty), return the number of remaining players on each team at the end of the game in the format:
# "Team A - {players_count}; Team B - {players_count}". If the game was terminated print an additional line: "Game was terminated"
# Note for the random tests: If a player that has already been sent off receives another card - ignore it.

cards = input()

cards_list = cards.split(" ")

A_red_players = list(range(1, 12))
B_red_players = list(range(1, 12))

for card in cards_list:
    card = card.split('-')

    team_of_player_to_be_removed = card[0]
    player_to_be_removed = int(card[1])

    if team_of_player_to_be_removed == 'A':
        for i in range(len(A_red_players)-1, -1, -1):
            if player_to_be_removed == A_red_players[i]:
                A_red_players.remove(A_red_players[i])

    if team_of_player_to_be_removed == 'B':
        for i in range(len(B_red_players)-1, -1, -1):
            if player_to_be_removed == B_red_players[i]:
                B_red_players.remove(B_red_players[i])

    if len(A_red_players) < 7 or len(B_red_players) < 7:
        break

print(f'Team A - {len(A_red_players)}; Team B - {len(B_red_players)}')

if len(A_red_players) < 7 or len(B_red_players) < 7:
    print('Game was terminated')