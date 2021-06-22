# еднакви думи
# Да се напише програма, която въвежда две думи и проверява дали са еднакви.
# Да не се прави разлика между главни и малки букви. Да се изведе "yes" или "no".

word_one = input()
word_two = input()

word_one = word_one.lower()
word_two = word_two.lower()

if word_one == word_two:
    print('yes')
else:
    print('no')