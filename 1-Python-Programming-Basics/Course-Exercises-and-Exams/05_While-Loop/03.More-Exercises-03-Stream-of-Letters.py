# 3.	Поток от букви
# Напишете програма, която прочита скрито съобщение в поредица от символи.
# Те се получават по един на ред до получаване на командата "End".
# Думите се образуват от буквите в реда на четенето им. Символите, които не са латински букви трябва да бъдат игнорирани.
# Думите скрити в потока са разделени от тайна команда от три букви – "c", "o" и "n".
# При първото получаване на една от тези букви, тя се маркира като срещната, но не се запазва в думата.
# При всяко следващо нейно срещане се записва нормално в думата. След като са налични и трите символа от командата,
# се печата думата и интервал " ". Започва се нова дума, която по същия начин чака тайната команда, за да бъде отпечатана.

word = ''
hasEncountered_n = False
hasEncountered_c = False
hasEncountered_o = False
command = input()
printed_words = ''

while command != 'End':
    character_numerical_representation = ord(command)
    if 65 <= character_numerical_representation <= 90 or 97 <= character_numerical_representation <= 122:
        if command == 'c' and not hasEncountered_c:
            hasEncountered_c = True
        elif command == 'n' and not hasEncountered_n:
            hasEncountered_n = True
        elif command == 'o' and not hasEncountered_o:
            hasEncountered_o = True
        else:
            word = word + command
        if hasEncountered_c and hasEncountered_n and hasEncountered_o:
            print(f'{word}', end=' ')
            word = ''
            hasEncountered_n = False
            hasEncountered_c = False
            hasEncountered_o = False
    command = input()