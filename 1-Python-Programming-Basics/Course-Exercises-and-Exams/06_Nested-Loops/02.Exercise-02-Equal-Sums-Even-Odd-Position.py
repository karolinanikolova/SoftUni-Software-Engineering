# 2.	Еднакви суми на четни и нечетни позиции
# Напишете програма, която чете от конзолата две шестцифрени цели числа в диапазона. Винаги първото въведено число ще
# бъде по-малко от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират
# между двете, прочетени от конзолата числа, и отговарят на условието сумата от цифрите на четни и нечетни позиции да са
# равни. Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.



# Each number has indiced for its digits in the computer memory. An index for each digit. The index starts from 0, 1, 2..
# To work with indices, we need to convert number to string. So we need to convert number to string and then we can
# work with the indices of the number

start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    number_as_string = str(number)
    odd_sum = 0
    even_sum = 0
    # Enumerate goes through each symbol in a string and allows us to pull out / work with the value and index of each symbol
    # Index is returning 0, 1, 2, 3, 4 (by default when using enumared the index starts from zero, based on google this can be changed, but he didn't explain it at this point)...
    # Digit is returning the value of the digit at a specific index
    # It doesn't need to be called index or digit. This is just what makes sense for this problem. But could be just i and d or anything else.
    for index, digit in enumerate(number_as_string):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(f'{number_as_string}', end=' ')



# # My more stupid decision
# start_number = int(input())
# end_number = int(input())
#
# for number in range(start_number, end_number + 1):
#     digit_six = number % 10
#     digit_five = (number // 10) % 10
#     digit_four = (number // 100) % 10
#     digit_three = (number // 1000) % 10
#     digit_two = (number // 10000) % 10
#     digit_one = (number // 100000) % 10
#     if (digit_one + digit_three + digit_five) == (digit_two + digit_four + digit_six):
#         print(f'{number}', end =' ')