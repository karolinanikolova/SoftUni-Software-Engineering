# 2.	Вело състезание
# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors") и
# старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите. Според възрастовата група и
# вида на трасето на което ще се провежда състезанието, таксата е различна.

count_juniors = int(input())
count_seniors = int(input())
track_type = input()

if track_type == 'trail':
    fee_junior = 5.50
    fee_senior = 7
elif track_type == 'cross-country':
    if (count_seniors + count_juniors) >= 50:
        fee_junior = 8 * 0.75
        fee_senior = 9.50 * 0.75
    else:
        fee_junior = 8
        fee_senior = 9.50
elif track_type == 'downhill':
    fee_junior = 12.25
    fee_senior = 13.75
elif track_type == 'road':
    fee_junior = 20
    fee_senior = 21.50

donation = (count_juniors * fee_junior + count_seniors * fee_senior) * .95

print(f'{donation:.2f}')

