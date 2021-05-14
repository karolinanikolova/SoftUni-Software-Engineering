# хотелска стая
# Хотел предлага два вида стаи: студио и апартамент.
#
# Напишете програма, която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:
#
# Май и октомври	Юни и септември	Юли и август
# Студио – 50 лв./нощувка	Студио – 75.20 лв./нощувка	Студио – 76 лв./нощувка
# Апартамент – 65 лв./нощувка	Апартамент – 68.70 лв./нощувка	Апартамент – 77 лв./нощувка
# Предлагат се и следните отстъпки:
#
# За студио, при повече от 7 нощувки през май и октомври: 5% намаление.
# За студио, при повече от 14 нощувки през май и октомври: 30% намаление.
# За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# За апартамент, при повече от 14 нощувки, без значение от месеца: 10% намаление.

month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    if 7 < nights <= 14:
        studio_price = 50 * 0.95
    elif nights > 14:
        studio_price = 50 * 0.7
    else:
        studio_price = 50
    apartment_price = 65
elif month == 'June' or month == 'September':
    if nights > 14:
        studio_price = 75.20 * 0.8
    else:
        studio_price = 75.20
    apartment_price = 68.70
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if nights > 14:
    apartment_price = 0.9 * apartment_price

apartment_price_total = nights * apartment_price
studio_price_total = nights * studio_price

print(f'Apartment: {apartment_price_total:.2f} lv.')
print(f'Studio: {studio_price_total:.2f} lv.')
