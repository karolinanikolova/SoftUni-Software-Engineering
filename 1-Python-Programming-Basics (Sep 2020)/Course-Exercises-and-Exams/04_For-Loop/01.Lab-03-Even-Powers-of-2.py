# 3.	Четни степени на 2
# Да се напише програма, която чете число n, въведено от потребителя, и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.

n = int(input())

for n in range(0, n + 1, 2):
    print(2 ** n)