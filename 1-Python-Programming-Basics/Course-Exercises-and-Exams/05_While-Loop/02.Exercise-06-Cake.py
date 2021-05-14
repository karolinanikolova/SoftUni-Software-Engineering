# 6.	Торта
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата
# "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."

width = int(input())
length = int(input())
total_pieces = width * length
command = input()

while command != 'STOP':
    current_pieces = int(command)
    total_pieces -= current_pieces
    if total_pieces < 0:
        break
    command = input()

if total_pieces >= 0:
    print(f'{total_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')

