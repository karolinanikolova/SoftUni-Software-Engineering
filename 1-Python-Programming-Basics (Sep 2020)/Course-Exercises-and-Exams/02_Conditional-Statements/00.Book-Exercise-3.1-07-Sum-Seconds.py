# сумиране на секунди
# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която въвежда времената на състезателите и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2 -> "02", 7 -> "07", 35 -> "35").

time_contestant_one = int(input())
time_contestant_two = int(input())
time_contestant_three = int(input())

seconds = time_contestant_one + time_contestant_two + time_contestant_three
minutes = 0

if 59 < seconds <= 119:
    minutes += 1
    seconds = seconds - 60
elif 119 < seconds <= 179:
    minutes += 2
    seconds = seconds - 120

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")


# Other method
#
# time_first = int(input())
# time_second = int(input())
# time_third = int(input())
#
# total_time = time_first + time_second + time_third
#
# minutes = total_time // 60
# seconds = total_time % 60
#
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")
