# вид животно
# Напишете програма, която принтира вида на животно според името му:
#
# dog -> mammal
# crocodile, tortoise, snake -> reptile
# others -> unknown

animal_name = input()

if animal_name == 'dog':
    print('mammal')
elif animal_name == 'crocodile' or animal_name == 'tortoise' or animal_name == 'snake':
    print('reptile')
else:
    print('unknown')
