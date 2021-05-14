# парички
# Преди време Пешо си е купил биткойни. Сега ще ходи на екскурзия из Европа и ще му трябва евро.
# Освен биткойни има и китайски юани. Пешо иска да обмени парите си в евро за екскурзията.
# Напишете програма, която да пресмята колко евро може да купи спрямо следните валутни курсове:
#
# 1 биткойн = 1168 лева.
# 1 китайски юан = 0.15 долара.
# 1 долар = 1.76 лева.
# 1 евро = 1.95 лева.
# Обменното бюро има комисионна от 0 до 5 процента от крайната сума в евро.

bitcoin = int(input())
chin = float(input())
commission = float(input()) / 100

bitcoin_to_lv = bitcoin * 1168
bitcoin_to_lv_to_eur = bitcoin_to_lv / 1.95

chin_to_USD = chin * 0.15
chin_to_USD_to_lv = chin_to_USD * 1.76
chin_to_USD_to_lv_to_EUR = chin_to_USD_to_lv / 1.95

sum = (bitcoin_to_lv_to_eur + chin_to_USD_to_lv_to_EUR) * (1 - commission)
print(f"{sum:.2f}")