# Console cross-currency converter
# Write a program to convert money from one currency to another . The following currencies must be maintained: BGN, USD, EUR, GBP . Use the following fixed exchange rates:
# Course	USD	        EUR	        GBP
# 1 BGN	    1.79549	    1.95583	    2.53405

currency_amount = float(input())
currency_input = input()
currency_output = input()

dict = {'BGN':1, 'USD':1.79549, 'EUR':1.95583, 'GBP':2.53405}

result = round((currency_amount * (dict[currency_input]/dict[currency_output])), 2)
print(f'{result} {currency_output}')


