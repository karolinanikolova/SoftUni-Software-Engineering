# време + 15 минути
# Да се напише програма, която въвежда час и минути от 24-часово денонощие и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат hh:mm. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри и с водеща нула, когато е необходимо.

current_h = int(input())
current_m = int(input())

current_minutes = current_h * 60 + current_m
future_minutes = current_minutes + 15

future_h = future_minutes // 60
future_m = future_minutes % 60

if future_h == 24:
    future_h = 0

if 0 <= future_m <= 9:
    print(f'{future_h}:0{future_m}')
else:
    print(f'{future_h}:{future_m}')