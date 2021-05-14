# 9.	Озеленяване на дворове
# Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои от тях, като по този начин създаде уютна обстановка и комфорт на гостите си.
# За целта е наела фирма.
# Напишете програма, която изчислява необходимите средства, които Божидара ще трябва да заплати на фирмата изпълнител на проекта.
# Цената на един кв. м. е 7.61лв със ДДС. Тъй като нейният двор е доста голям, фирмата изпълнител предлага 18% отстъпка от крайната цена.
area = float(input())
price_sq_m = 7.61
discount_percentage = 0.18
discount = area * price_sq_m * discount_percentage
price_total_with_discount = area * price_sq_m * (1 - discount_percentage)
print(f'The final price is: {price_total_with_discount:.2f} lv.')
print(f"The discount is: {discount:.2f} lv.")