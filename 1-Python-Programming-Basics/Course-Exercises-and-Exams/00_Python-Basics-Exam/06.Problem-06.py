# Задача 6. Пътници на полет
# Напишете програма, която проследява колко пътници средно на полет има всяка авиокомпания.
# Всеки ден има определен брой авиокомпании, които имат полети. До получаване на команда "Finish" получавате брой пътници
# на полет. Трябва да изчислите средния брой пътници на полет на авиокомпания. След като излетят всички полети на всички
# авиокомпании трябва да отпечатате коя е компанията с най-голям среден брой пътници за полетите си.
# Средният брой пътници винаги трябва да бъде закръглен към най-близкото цяло число надолу.

from math import floor
from sys import maxsize

number_of_airlines = int(input())
max_number_of_average_passengers_per_airline = - maxsize

for airline in range(1, number_of_airlines + 1):
    airline = input()
    count_flights_per_airline = 0
    count_passengers_per_airline = 0

    command = input()
    while command != 'Finish':
        number_of_passengers_per_flight = int(command)
        count_flights_per_airline += 1
        count_passengers_per_airline += number_of_passengers_per_flight
        command = input()

    if command == 'Finish':
        count_average_passengers_per_airline = floor(count_passengers_per_airline / count_flights_per_airline)
        print(f'{airline}: {count_average_passengers_per_airline} passengers.')

    if count_average_passengers_per_airline > max_number_of_average_passengers_per_airline:
        max_number_of_average_passengers_per_airline = count_average_passengers_per_airline
        airline_with_max_number_of_average_passengers = airline

print(f'{airline_with_max_number_of_average_passengers} has most passengers per flight: {max_number_of_average_passengers_per_airline}')