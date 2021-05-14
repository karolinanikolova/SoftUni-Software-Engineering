# еднакви 3 числа
# Да се напише програма, в която се въвеждат 3 числа и се отпечатва дали те са еднакви ("yes" / "no").

number_one = float(input())
number_two = float(input())
number_three = float(input())

if number_one == number_two and number_one == number_three:
    print('yes')
else:
    print('no')