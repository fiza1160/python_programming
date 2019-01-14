'''
генератор - это функция в которой есть оператор yield.
Этот оператор возвращает результат, но не прерывает функцию.

генераторы используются когда мы хотим итерироваться по большому количеству значений,
но не хотим загружать ими память

Пример 1:
'''


def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


# for number in even_range(0, 10):
#     print(number)


def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


# for num in fibonacci(10):
#     print(num)


'''Еще одна важная особенность генераторов --- это возможность передавать генератору
какие-то значения

Пример 2:
'''

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
        if not value: break
        total += value


generator = accumulator()
next(generator)
for i in range(1, 5):
    print('Accumulated: {}'.format(generator.send(i)))
next(generator)
