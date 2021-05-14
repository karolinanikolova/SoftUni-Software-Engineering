# Задача 5. Грижи за кученце
# Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови.
# То изяжда дневно определено количество храна. Да се напише програма, която проверява дали количеството храна,
# което е закупено за кученцето, ще е достатъчно докато кученцето бъде осиновено.

food_bought_kg = float(input())
food_bought_grams = food_bought_kg * 1000
command = input()
food_needed = 0

while command != 'Adopted':
    food_per_meal_grams = float(command)
    food_needed += food_per_meal_grams
    command = input()

if food_needed <= food_bought_grams:
    print(f'Food is enough! Leftovers: {food_bought_grams - food_needed:.0f} grams.')
else:
    print(f'Food is not enough. You need {food_needed - food_bought_grams:.0f} grams more.')
