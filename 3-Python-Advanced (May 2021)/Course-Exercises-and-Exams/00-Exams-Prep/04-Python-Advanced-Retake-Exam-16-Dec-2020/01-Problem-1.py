from collections import deque

males = [int(el) for el in input().split() if int(el) > 0]
females = deque([int(el) for el in input().split() if int(el) > 0])

matches = 0

while females and males:
    current_female = females[0]
    current_male = males[-1]

    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue

    elif current_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    elif current_male == current_female:
        females.popleft()
        males.pop()
        matches += 1
        continue

    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()
            continue

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(el) for el in males[::-1])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(el) for el in list(females))}")
else:
    print(f"Females left: none")