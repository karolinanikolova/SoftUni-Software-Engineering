# 6.	Сватбени места
# Младоженците искат да направят списък кой на кое място ще седи на сватбената церемония.
# Местата са разделени на различни сектори. Секторите са главните латински букви като започват от A.
# Във всеки сектор има определен брой редове. От конзолата се чете броят на редовете в първия сектор (A),
# като във всеки следващ сектор редовете се увеличават с 1. На всеки ред има определен брой места - тяхната
# номерация е представена с малките латински букви. Броя на местата на нечетните редове се прочита от конзолата,
# а на четните редове местата са с 2 повече.

last_sector_letter = input()
number_of_rows_sector_A = int(input())
number_of_seats_on_odd_rows = int(input())
number_of_seats_on_even_rows = number_of_seats_on_odd_rows + 2
count_number_of_rows_in_sector = number_of_rows_sector_A
count_seats = 0

for sector in range(ord('A'), ord(last_sector_letter) + 1):
    for row in range(1, count_number_of_rows_in_sector + 1):
        if row % 2 == 0:
            number_of_seats_on_row = number_of_seats_on_even_rows
        else:
            number_of_seats_on_row = number_of_seats_on_odd_rows
        for seat in range(ord('a'), ord('a') + number_of_seats_on_row):
            print(f'{chr(sector)}{row}{chr(seat)}')
            count_seats += 1

    count_number_of_rows_in_sector += 1

print(f'{count_seats}')

