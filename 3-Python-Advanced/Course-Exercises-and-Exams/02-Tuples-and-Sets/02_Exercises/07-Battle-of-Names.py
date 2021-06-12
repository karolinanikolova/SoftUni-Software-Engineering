# 7.	Battle of Names
# You will receive a number N. On the next N lines, you will be receiving names.
# You must sum the ascii values of each letter in the name and integer divide it to the number of the current row
# (starting from 1). Save the result to a set of either odd or even numbers, depending on if the devised number is
# an odd or even. After that, sum the values of each set.
# •	If the sums of the two sets are equal, print the union values, separated by ", ".
# •	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values,
# separated by ", ".
# •	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric different
# values, separated by ", ".
# NOTE: On every operation, the starting set should be the odd set

N = int(input())

results_odd = set()
results_even = set()

for row in range(1, N+1):
    name = input()

    result = sum(ord(ch) for ch in name) // row

    if result % 2 == 0:
        results_even.add(result)
    else:
        results_odd.add(result)

sum_results_odd = sum(results_odd)
sum_results_even = sum(results_even)

if sum_results_odd == sum_results_even:
    print(', '.join([str(el) for el in results_odd.union(results_even)]))
elif sum_results_odd > sum_results_even:
    print(', '.join([str(el) for el in results_odd.difference(results_even)]))
elif sum_results_odd < sum_results_even:
    print(', '.join([str(el) for el in results_odd.symmetric_difference(results_even)]))