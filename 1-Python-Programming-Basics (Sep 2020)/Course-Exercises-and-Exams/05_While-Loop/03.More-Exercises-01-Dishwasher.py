# 1.	Съдомиялна
# Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат за
# съдомиялна е достатъчно, за да измие определено количество съдове. Знае се, че всяка бутилка съдържа 750 мл.
# препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.  Приемете, че на всяко трето зареждане със съдове,
# съдомиялната се пълни само с тенджери, а останалите пъти с чинии. Докато не получите команда "End" ще
# продължите да получавате бройка съдове, които трябва да бъдат измити.

detergent_per_bottle = 750
detergent_needed_per_dish = 5
detergent_needed_per_pot = 15
count_dishwasher_load = 0
count_clean_dishes = 0
count_clean_pots = 0
isPot = False
isDish = False
detergent_needed_per_item = 0
isDetergentEnough = True
count_detergent_bottles = int(input())
detergent_total = detergent_per_bottle * count_detergent_bottles

command = input()



while command != 'End' and detergent_total >= 0:
    count_dishwasher_load += 1
    count_items = int(command)
    if count_dishwasher_load % 3 == 0:
        detergent_needed_per_item = detergent_needed_per_pot
        isPot = True
    else:
        detergent_needed_per_item = detergent_needed_per_dish
        isDish = True
    detergent_needed_for_this_load = detergent_needed_per_item * count_items
    if isPot:
        if detergent_total >= detergent_needed_for_this_load:
            count_clean_pots += count_items
        else:
            count_clean_pots += detergent_total // detergent_needed_per_item
            isDetergentEnough = False
    if isDish:
        if detergent_total >= detergent_needed_for_this_load:
            count_clean_dishes += count_items
        else:
            count_clean_dishes += detergent_total // detergent_needed_per_item
            isDetergentEnough = False
    detergent_total -= detergent_needed_for_this_load
    isPot = False
    isDish = False
    command = input()

if isDetergentEnough:
    print(f'Detergent was enough!')
    print(f'{count_clean_dishes} dishes and {count_clean_pots} pots were washed.')
    print(f'Leftover detergent {detergent_total} ml.')
else:
    print(f'Not enough detergent, {abs(detergent_total)} ml. more necessary!')