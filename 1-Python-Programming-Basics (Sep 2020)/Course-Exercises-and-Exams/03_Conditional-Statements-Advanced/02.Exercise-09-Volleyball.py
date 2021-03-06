# 9.	*Волейбол
# Влади е студент, живее в София и си ходи от време на време до родния град. Той е много запален по волейбола,
# но е зает през работните дни и играе волейбол само през уикендите и в празничните дни.
# Влади играе в София всяка събота, когато не е на работа и не си пътува до родния град, както и в 2/3 от празничните дни.
# Той пътува до родния си град h пъти в годината, където играе волейбол със старите си приятели в неделя.
# Влади не е на работа 3/4 от уикендите, в които е в София. Отделно, през високосните години Влади играе с 15% повече волейбол от нормалното.
# Приемаме, че годината има точно 48 уикенда, подходящи за волейбол.
# Напишете програма, която изчислява колко пъти Влади е играл волейбол през годината.
# Закръглете резултата надолу до най-близкото цяло число (например 2.15  2; 9.95  9).
# Входните данни се въвеждат от потребителя, в следния вид:
# •	Първият ред съдържа думата "leap" (високосна година) или "normal" (невисокосна);
# •	Вторият ред съдържа цялото число p – брой празници в годината (които не са събота и неделя);
# •	Третият ред съдържа цялото число h – брой уикенди, в които Влади си пътува до родния град.

from math import floor

year_type = input()
holidays = int(input())
count_weekend_hometown = int(input())

count_weekend_total = 48
count_weekend_in_Sofia = count_weekend_total - count_weekend_hometown
count_weekend_in_Sofia_not_working = count_weekend_in_Sofia * 3 / 4

play_sofia = count_weekend_in_Sofia_not_working + holidays * 2 / 3
play_hometown = count_weekend_hometown

play_total = play_sofia + play_hometown

if year_type == 'leap':
    play_total = 1.15 * play_total

print(floor(play_total))