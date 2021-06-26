def best_list_pureness(numbers_list, K):

    pureness = []
    current_pureness = 0
    current_rotation = -1

    while not current_rotation == K:
        for index in range(len(numbers_list)):
            current_pureness += numbers_list[index] * index

        pureness.append(current_pureness)
        current_pureness = 0

        numbers_list.insert(0, numbers_list.pop())

        current_rotation += 1

    return f"Best pureness {max(pureness)} after {pureness.index(max(pureness))} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
