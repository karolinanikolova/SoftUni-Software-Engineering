# 5.	Време + 15 минути
# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

current_hours = int(input())
current_minutes = int(input())
current_time_in_minutes = current_hours * 60 + current_minutes
time_after_fifteen_minutes = current_time_in_minutes + 15
hours_after_fifteen_minutes = time_after_fifteen_minutes // 60
minutes_after_fifteen_minutes = time_after_fifteen_minutes % 60

if hours_after_fifteen_minutes > 23:
    hours_after_fifteen_minutes -= 24

if minutes_after_fifteen_minutes < 10:
    print(f'{hours_after_fifteen_minutes}:0{minutes_after_fifteen_minutes}')
else:
    print(f'{hours_after_fifteen_minutes}:{minutes_after_fifteen_minutes}')

# #Other method 1:
# time_hours = int(input())
# time_minutes = int(input())
#
# if time_minutes < 45:
#     time15_minutes = time_minutes + 15
#     time15_hours = time_hours
# else:
#     time15_minutes = (time_minutes + 15) % 60
#     if time_hours < 23:
#         time15_hours = time_hours + 1
#     else:
#         time15_hours = 0
#
# if time15_minutes < 10:
#     print(f'{time15_hours}:0{time15_minutes}')
# else:
#     print(f'{time15_hours}:{time15_minutes}')

# #Other method 2:
# time_hours = int(input())
# time_minutes = int(input())
#
# if (time_minutes + 15) % 60 >= 15:
#     time15_minutes = time_minutes + 15
#     time15_hours = time_hours
# else:
#     time15_minutes = (time_minutes + 15) % 60
#     if time_hours < 23:
#         time15_hours = time_hours + 1
#     else:
#         time15_hours = 0
#
# if time15_minutes < 10:
#     print(f'{time15_hours}:0{time15_minutes}')
# else:
#     print(f'{time15_hours}:{time15_minutes}')
