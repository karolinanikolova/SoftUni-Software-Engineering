# всички латински букви
# Да се напише програма, която отпечатва буквите от латинската азбука: a, b, c, …, z.

for i in range(ord('a'), ord('z') + 1):
    print(chr(i))

# https://en.wikibooks.org/wiki/Python_Programming/Text#:~:text=To%20get%20the%20ASCII%20code,use%20the%20ord()%20function.&text=To%20get%20the%20character%20encoded,use%20the%20chr()%20function.&text=To%20know%20if%20all%20the,use%20the%20isalnum()%20function.