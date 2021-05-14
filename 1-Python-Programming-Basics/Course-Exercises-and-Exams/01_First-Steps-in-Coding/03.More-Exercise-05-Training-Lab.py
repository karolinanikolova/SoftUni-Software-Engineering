# 5.	Учебна зала
# Учебна зала има правоъгълен размер w на h метра, без колони във вътрешността си. Залата е разделена на две части – лява и дясна, с коридор приблизително по средата.
# В лявата и в дясната част има редици с бюра. В задната част на залата има голяма входна врата. В предната част на залата има катедра с подиум за преподавателя.
# Едно работно място заема 70 на 120 cm (маса с размер 70 на 40 cm + място за стол и преминаване с размер 70 на 80 cm).
# Коридорът е широк поне 100 cm. Изчислено е, че заради входната врата (която е с отвор 160 cm) се губи точно 1 работно място, а заради катедрата (която е с размер 160 на 120 cm)
# се губят точно 2 работни места. Напишете програма, която въвежда размери на учебната зала и изчислява броя работни места в нея при описаното разположение (вж. фигурата).

from math import floor

w = float(input())
h = float(input())

w_desk = 1.2
h_desk = 0.7
h_corridor = 1

desk_per_height = floor((h - h_corridor) / h_desk)
desk_per_width = floor(w / w_desk)

desk_space_taken_by_door = 1
desk_space_taken_by_podium = 2

desks_possible = desk_per_width * desk_per_height - desk_space_taken_by_door - desk_space_taken_by_podium

print(desks_possible)