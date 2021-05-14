# 8.	Зоомагазин
# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и други животни.
# Една опаковка храна за кучета е на цена 2.50лв., а всяка останала, която не е за тях струва 4лв.
dog_number = int(input())
other_pets_number = int(input())
dog_food_price = 2.5
other_pet_food_price = 4
total_price = dog_number * dog_food_price + other_pets_number * other_pet_food_price
# print(str(total_price) + " lv.")
# print(f"{total_price} lv.")

# For long sentences, can break up on two rows in the code
# print(str(total_price), end='')
# print(" lv.")
