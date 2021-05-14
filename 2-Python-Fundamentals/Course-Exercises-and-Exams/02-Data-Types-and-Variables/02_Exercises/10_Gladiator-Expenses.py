# 10.	* Gladiator Expenses
# As a gladiator, Peter has to repair his broken equipment when he loses a fight. His equipment consists of helmet,
# sword, shield and armor. You will receive the Peter`s lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also brakes.
# Every second time, when his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment.

count_lost_fight = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
total_cost = 0

for lost_game in range(1, count_lost_fight + 1):
    if lost_game % 2 == 0:
        total_cost += price_helmet
    if lost_game % 3 == 0:
        total_cost += price_sword
    if lost_game % 6 == 0:
        total_cost += price_shield
    if lost_game % 12 == 0:
        total_cost += price_armor

print(f"Gladiator expenses: {total_cost:.2f} aureus")
