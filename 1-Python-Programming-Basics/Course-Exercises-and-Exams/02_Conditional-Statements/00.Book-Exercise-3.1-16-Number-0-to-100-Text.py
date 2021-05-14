# изписване на число от 0 до 100 с думи
# Да се напише програма, която превръща число в диапазона [0 … 100] в текст.

number = int(input())

if number // 10 == 0:
    if number == 0:
        string = 'zero'
    elif number == 1:
        string = 'one'
    elif number == 2:
        string = 'two'
    elif number == 3:
        string = 'three'
    elif number == 4:
        string = 'four'
    elif number == 5:
        string = 'five'
    elif number == 6:
        string = 'six'
    elif number == 7:
        string = 'seven'
    elif number == 8:
        string = 'eight'
    elif number == 9:
        string = 'nine'
elif number // 10 <= 9:
    if number // 10 == 1:
        if number % 10 == 0:
            string = 'ten'
        elif number % 10 == 1:
            string = 'eleven'
        elif number % 10 == 2:
            string = 'twelve'
        elif number % 10 == 3:
            string = 'thirteen'
        elif number % 10 == 4:
            string = 'fourteen'
        elif number % 10 == 5:
            string = 'fifteen'
        elif number % 10 == 6:
            string = 'sixteen'
        elif number % 10 == 7:
            string = 'seventeen'
        elif number % 10 == 8:
            string = 'eighteen'
        elif number % 10 == 9:
            string = 'nineteen'
    elif number // 10 == 2:
        if number % 10 == 0:
            string = 'twenty'
        elif number % 10 == 1:
            string = 'twenty' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'twenty' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'twenty' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'twenty' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'twenty' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'twenty' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'twenty' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'twenty' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'twenty' + ' ' + 'nine'
    elif number // 10 == 3:
        if number % 10 == 0:
            string = 'thirty'
        elif number % 10 == 1:
            string = 'thirty' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'thirty' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'thirty' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'thirty' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'thirty' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'thirty' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'thirty' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'thirty' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'thirty' + ' ' + 'nine'
    elif number // 10 == 4:
        if number % 10 == 0:
            string = 'forty'
        elif number % 10 == 1:
            string = 'forty' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'forty' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'forty' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'forty' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'forty' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'forty' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'forty' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'forty' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'forty' + ' ' + 'nine'
    elif number // 10 == 5:
        if number % 10 == 0:
            string = 'fifty'
        elif number % 10 == 1:
            string = 'fifty' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'fifty' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'fifty' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'fifty' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'fifty' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'fifty' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'fifty' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'fifty' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'fifty' + ' ' + 'nine'
    elif number // 10 == 6:
        if number % 10 == 0:
            string = 'sixty'
        elif number % 10 == 1:
            string = 'sixty' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'sixty' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'sixty' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'sixty' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'sixty' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'sixty' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'sixty' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'sixty' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'sixty' + ' ' + 'nine'
    elif number // 10 == 7:
        if number % 10 == 0:
            string = 'seventy'
        elif number % 10 == 1:
            string = 'seventy' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'seventy' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'seventy' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'seventy' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'seventy' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'seventy' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'seventy' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'seventy' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'seventy' + ' ' + 'nine'
    elif number // 10 == 8:
        if number % 10 == 0:
            string = 'eighty'
        elif number % 10 == 1:
            string = 'eighty' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'eighty' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'eighty' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'eighty' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'eighty' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'eighty' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'eighty' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'eighty' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'eighty' + ' ' + 'nine'
    elif number // 10 == 9:
        if number % 10 == 0:
            string = 'ninety'
        elif number % 10 == 1:
            string = 'ninety' + ' ' + 'one'
        elif number % 10 == 2:
            string = 'ninety' + ' ' + 'two'
        elif number % 10 == 3:
            string = 'ninety' + ' ' + 'three'
        elif number % 10 == 4:
            string = 'ninety' + ' ' + 'four'
        elif number % 10 == 5:
            string = 'ninety' + ' ' + 'five'
        elif number % 10 == 6:
            string = 'ninety' + ' ' + 'six'
        elif number % 10 == 7:
            string = 'ninety' + ' ' + 'seven'
        elif number % 10 == 8:
            string = 'ninety' + ' ' + 'eight'
        elif number % 10 == 9:
            string = 'ninety' + ' ' + 'nine'
elif number // 10 == 10:
    string = 'one hundred'

print(string)