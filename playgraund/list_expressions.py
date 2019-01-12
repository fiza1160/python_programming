'''лаконичный способ создавать списки

Пример 1
с циклом'''
square_list = []
for number in range (10):
    square_list.append(number ** 2)

print(square_list)

square_list_short = [number_2 ** 2 for number_2 in range(10)]
print(square_list_short)


'''пример 2:
с условием'''
even_list = []
for number in range(10):
    if number % 2 == 0:
        even_list.append(number)

print(even_list)

even_list_short = [num for num in range(10) if num % 2 == 0]
print(even_list_short)

'''так же можно определять словари'''
square_map = {number: number ** 2 for number in range(5)}
print(square_map)

