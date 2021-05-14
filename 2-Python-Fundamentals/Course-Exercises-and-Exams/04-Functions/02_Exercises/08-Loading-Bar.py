# 8. * Loading Bar
# You will receive a single integer number between 0 and 100 which is divided with 10 without residue (0, 10, 20, 30...).
# Your task is to create a function that visualizes a loading bar depending on that number you have received in the input.

# def loading_bar(num):
#     bar = []
#
#     count_percentages = int(num / 10)
#     count_dots = 10 - count_percentages
#
#     bar.append(count_percentages * '%' + count_dots * '.')
#
#     return bar
#
#
# number = int(input())
#
# bar_result = loading_bar(number)
#
# if number == 100:
#     print('100% Complete!')
#     print(f'[{bar_result[0]}]')
# else:
#     print(f'{number}% [{bar_result[0]}]')
#     print('Still loading...')


def loading_bar(num):
    bar = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']

    if num == 0:
        return bar

    n = num // 10

    for index in range(n):
        bar[index] = '%'

    return bar


number = int(input())

bar_result = loading_bar(number)

if bar_result.count('%') == 10:
    print('100% Complete!')
    print(f'[{"".join(bar_result)}]')
else:
    print(f'{number}% [{"".join(bar_result)}]')
    print('Still loading...')