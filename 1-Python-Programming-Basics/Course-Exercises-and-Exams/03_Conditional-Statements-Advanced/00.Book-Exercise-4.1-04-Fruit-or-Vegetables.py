# плод или зеленчук
# Нека проверим дали даден продукт е плод или зеленчук. Плодовете "fruit" са banana, apple, kiwi, cherry, lemon и grapes.
# Зеленчуците "vegetable" са tomato, cucumber, pepper и carrot. Всички останали са "unknown"

product = input()

if product == 'banana' or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' or product == 'grapes':
    print('fruit')
elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    print('vegetable')
else:
    print('unknown')