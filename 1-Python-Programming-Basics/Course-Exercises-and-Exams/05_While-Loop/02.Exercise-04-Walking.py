# 4.	Стъпки
# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма,
# която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си да се
# изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла докато
# се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише
# "{разликата между стъпките} more steps to reach goal."

target_steps = 10000
total_steps = 0
command = input()
goalReached = False

while command != 'Going home':
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= target_steps:
        goalReached = True
        break
    command = input()

if command == 'Going home':
    last_steps = int(input())
    total_steps += last_steps
    if total_steps >= target_steps:
        goalReached = True

difference = abs(total_steps - target_steps)

if goalReached:
    print(f'Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')



