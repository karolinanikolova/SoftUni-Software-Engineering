# сумиране на гласните букви
# Да се напише програма, която въвежда текст (стринг), изчислява и отпечатва сумата от стойностите на гласните букви
# според таблицата по-долу:
# a	e	i	o	u
# 1	2	3	4	5

text = input()
sum = 0

for i in text:
    if i == 'a':
        sum = sum + 1
    elif i == 'e':
        sum = sum + 2
    elif i == 'i':
        sum = sum + 3
    elif i == 'o':
        sum = sum + 4
    elif i == 'u':
        sum = sum + 5

print(sum)