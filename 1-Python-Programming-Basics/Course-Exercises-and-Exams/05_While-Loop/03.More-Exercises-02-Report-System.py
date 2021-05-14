# 2.	Система за отчет
# На благотворително събитие плащанията за закупените продукти винаги се редуват:
# плащане в брой и плащане с карта. Установени са следните правила за заплащане:
# •	Ако продуктът надвишава 100лв., за него не може да се плати в брой
# •	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.

desired_raised_money = float(input())
command = input()
raised_money = 0
count_transaction = 0
count_sale_card = 0
count_sale_cash = 0
raised_money_card = 0
raised_money_cash = 0
isPaymentByCard = False
isPaymentCash = False
isPaymentSuccessful = True
isRaisedMoneyEnough = False

while command != 'End':
    product_price = int(command)
    count_transaction += 1
    if count_transaction % 2 == 0:
        isPaymentByCard = True
    else:
        isPaymentCash = True
    if product_price > 100 and isPaymentCash:
        print(f'Error in transaction!')
    elif product_price < 10 and isPaymentByCard:
        print(f'Error in transaction!')
    else:
        raised_money += product_price
        print(f'Product sold!')
        if isPaymentByCard:
            count_sale_card += 1
            raised_money_card += product_price
        if isPaymentCash:
            count_sale_cash += 1
            raised_money_cash += product_price
    if raised_money >= desired_raised_money:
        isRaisedMoneyEnough = True
        break
    isPaymentByCard = False
    isPaymentCash = False
    command = input()

if isRaisedMoneyEnough:
    print(f'Average CS: {raised_money_cash / count_sale_cash:.2f}')
    print(f'Average CC: {raised_money_card / count_sale_card:.2f}')
if command == 'End':
    print(f'Failed to collect required money for charity.')
