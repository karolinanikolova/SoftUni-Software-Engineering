# тръби в басейн
# Басейн с обем V има две тръби, от които се пълни. Всяка тръба има определен дебит (литрите вода, минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа.
# Напишете програма, която изкарва състоянието на басейна, в момента, когато работникът се върне.

from math import trunc

V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

V1 = P1 * H
V2 = P2 * H

if V >= (V1 + V2):
    print(f'The pool is {trunc(((V1 + V2) / V ) * 100)}% full. Pipe 1: {trunc((V1 / (V1 + V2)) * 100)}%. Pipe 2: {trunc((V2 / (V1 + V2)) * 100)}%.')
else:
    print(f'For {H} hours the pool overflows with {(V1 + V2) - V} liters.')