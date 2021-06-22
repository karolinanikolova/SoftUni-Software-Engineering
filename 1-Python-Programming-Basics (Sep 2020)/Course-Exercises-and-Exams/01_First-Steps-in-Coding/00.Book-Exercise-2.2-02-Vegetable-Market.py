#  зеленчукова борса
# Градинар продава реколтата от градината си на зеленчуковата борса. Продава зеленчуци за N лева на килограм и плодове за M лева за килограм.
#  Напишете програма, която да пресмята приходите от реколтата в евро (ако приемем, че едно евро е равно на 1.94 лв.).

price_kg_veg_in_LEV = float(input())
price_kg_fruit_in_LEV = float(input())
kg_veg = int(input())
kg_fruit = int(input())

sum = (price_kg_fruit_in_LEV * kg_fruit + price_kg_veg_in_LEV * kg_veg) / 1.94
print(sum)

