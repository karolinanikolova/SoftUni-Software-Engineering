# 10.	* Bread Factory
# As a young baker, you are baking the bread out of the bakery.
# You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2|event3…"
# Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
# •	If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your initial
# energy (100). Print: "You gained {0} energy.".
# After that, print your current energy: "Current energy: {0}.".
# •	If the event is "order": You've earned some coins, the number in the second part. Each time you get an order, your ' \
#                                  'energy decreases with 30 points.
# o	If you have energy to complete the order, print: "You earned {0} coins.".
# o	If your energy drops below 0, you skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case you are having an ingredient, you have to buy. The second part of the event, contains the coins
# you have to spent and remove from your coins.
# o	If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print ("You bought {ingredient}.")
# o	If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the next three lines:
# "Day completed!", "Coins: {coins}", "Energy: {energy}".

initial_energy = 100
initial_coins = 100

all_events = input().split('|')

current_energy = initial_energy
coins = initial_coins

is_bankrupt = False

for event_index in range(len(all_events)):
    event = all_events[event_index].split('-')
    event_name_or_item = event[0]
    event_number = int(event[1])

    if event_name_or_item == 'rest':
        if current_energy + event_number <= initial_energy:
            current_energy += event_number
            print(f'You gained {event_number} energy.')
        else:
            print(f'You gained {initial_energy - current_energy} energy.')
            current_energy = 100
        print(f'Current energy: {current_energy}.')

    elif event_name_or_item == 'order':
        if current_energy - 30 >= 0:
            current_energy -= 30
            coins += event_number
            print(f'You earned {event_number} coins.')
        else:
            current_energy += 50
            print("You had to rest!")

    else:
        if coins > event_number:
            coins -= event_number
            print(f'You bought {event_name_or_item}.')
        else:
            print(f'Closed! Cannot afford {event_name_or_item}.')
            is_bankrupt = True
            break

if not is_bankrupt:
    print('Day completed!')
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")