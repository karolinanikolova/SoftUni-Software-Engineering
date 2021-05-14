# 5.	Предизвикай Сватбата
# Провокирани от сватбата си, Михаела и Иван решават да предоставят нова услуга на клиенти на ресторанта си,
# а именно вечеря за запознанства - "Предизвикай Сватбата". Напишете програма, която отпечатва всички възможни срещи
# на клиентите на ресторанта. При настаняване всеки мъж и всяка жена получават талончета с поредни номера стартирайки
# от 1. Ако бъдат заети всички маси, програмата трябва да приключи. Всяка маса има две места.

max_number_of_men = int(input())
max_number_of_women = int(input())
max_number_of_tables = int(input())
counter_taken_tables = 0

for man in range(1, max_number_of_men + 1):
    for woman in range(1, max_number_of_women + 1):
        counter_taken_tables += 1
        if counter_taken_tables <= max_number_of_tables:
            print(f'({man} <-> {woman})', end = ' ')
        else:
            break