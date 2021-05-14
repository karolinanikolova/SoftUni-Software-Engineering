# 2.	Поспаливата котка Том
# Котката Том обича по цял ден да спи, за негово съжаление стопанинът му си играе с него винаги когато  има свободно време.
# За да се наспи добре, нормата за игра на Том е 30 000  минути в година. Времето за игра на Том зависи от почивните дни на стопанина му:
# •	Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# •	Когато почива, стопанинът му си играе с него  по 127 минути на ден.
# Напишете програма, която въвежда броя почивни дни и отпечатва дали Том може да се наспи добре и колко е разликата от нормата за текущата година,
# като приемем че годината има 365 дни.
# Пример: 20 почивни дни -> работните дни са 345 (365 – 20 = 245). Реалното време за игра е 24 275 минути (345 * 63 + 20 *127).
# Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.

holidays = int(input())
workdays = 365 - holidays

playtime = holidays * 127 + workdays * 63

if playtime > 30000:
    print('Tom will run away')
    print(f'{(playtime - 30000) // 60} hours and {(playtime - 30000) % 60} minutes more for play')
elif playtime < 30000:
    print('Tom sleeps well')
    print(f'{abs(playtime - 30000) // 60} hours and {abs(playtime - 30000) % 60} minutes less for play')