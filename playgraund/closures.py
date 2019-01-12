''' Пример 1
Функция может принимать функцию в качестве параметра '''


def caller(func, param):
    return func(*param)


def printer(name, age):
    print('My name is {name}. I`m {age}'.format(name=name, age=age))


caller(printer, ['Alex', 31])

'''Пример 2 
Функция может возвращать функцию.
Функцию можно создать внутри функции
Функцию можно сложить в переменную'''


def get_additioner():
    def inner(a, b):
        return a + b

    return inner


additioner = get_additioner()
print(additioner(55, 18))
print(additioner(42, 24))

'''Пример 3
А вот эта штука называется замыкание.
Передаем в функцию параметр, пусть 2.
Внутри функции создаем функцию с параметром, функция умножает пар-р на пар-р внешней функции, на 2
Сохраняем это все в переменную, получаем умножатель на 2'''


def get_multiplier(number):
    def inner(a):
        return a * number

    return inner


multiplier = get_multiplier(2)
print(multiplier(10))
print(multiplier(14))
