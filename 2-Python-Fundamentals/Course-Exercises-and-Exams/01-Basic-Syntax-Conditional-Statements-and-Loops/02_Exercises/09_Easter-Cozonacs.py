# 9.	* Easter Cozonacs
# Since it’s Easter you have decided to make some cozonacs and exchange them for eggs.
# Create a program that calculates how much cozonacs you can make with the budget you have. First, you will receive your budget.
# Then, you will receive the price for 1 kg flour. Here is the recipe for one cozonac:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than price for 1 kg flour.
# Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
# Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
# •	For every cozonac that you make, you will receive 3 colored eggs.
# •	For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the usual 3 colored eggs for your cozonac.
#     The count of eggs you will lose is calculated when you subtract 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)
# In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, formatted to the 2nd decimal place, in the following format:
# "You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."

budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_eggs = 0.75 * price_per_kg_flour
price_per_quarter_liter_milk = 1.25 * price_per_kg_flour * 0.25
price_per_cozonac = price_per_pack_eggs + price_per_kg_flour + price_per_quarter_liter_milk

count_cozonacs = 0
count_colored_eggs = 0

while budget > price_per_cozonac:
    count_cozonacs += 1
    count_colored_eggs += 3
    budget -= price_per_cozonac
    if count_cozonacs % 3 == 0:
        count_colored_eggs -= count_cozonacs - 2

print(f'You made {count_cozonacs} cozonacs! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.')