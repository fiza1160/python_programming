import functools

'''Декоратор - это функция, принимающая на вход функцию и
возвращающая другую функцию
Декораторы используют, чтобы модифицировать поведение функций (обычно сразу нескольких).
Например, можно добавть логирование.'''

'''Синтаксис:'''


def decorator(funk):
    def new_funk():
        pass
    return new_funk()


@decorator
def decorated():
    print('Hello!')


'''в этом случае print не вызовется, 
потому что на самом деле decorated уже содержит другую функцию - new_funk'''

'''@decorator - это синтаксический сахар, за ним скрыто:
decorated = decorator(decorated)'''

'''Пример 1:
декоратор, который записывает в лог результат декорируемой функции'''


def logger(func):
    @functools.wraps(func) # чтобы название декорируемой функции оставалось оригинальным, а не изменялось на wrapped
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)

        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


@logger
def multiplicator(num_list):
    return functools.reduce(lambda x, y: x * y, num_list)


summator([1, 2, 3, 4, 5, 6])
multiplicator([1, 2, 3, 4, 5, 6])


'''Пример 2:
декоратор, с параметром'''


def logger_with_arg(file_name):
    def decorator_2(func):
        @functools.wraps(func)
        def wrapped_2(*args, **kwargs):
            result = func(*args, **kwargs)

            with open(file_name, 'w') as f:
                f.write(str(result))

            return result
        return wrapped_2
    return decorator_2


@logger_with_arg('log.txt')
def squares(num_list):
    return list(map(lambda x: x * x, num_list))

# эквивалентно записи squares = logger_with_arg('log.txt')(squares)


squares([1, 2, 3, 4, 5])

'''Пример 3:
очередность исполнения декораторов'''


def first_decorator(func):
    def wrapped():
        print('First call')
        return func()
    return wrapped


def second_decorator(func):
    def wrapped():
        print('Second call')
        return func()
    return wrapped


@first_decorator
@second_decorator
def decorated():
    print('Finally called')


# decarated = first_decorator(second_decorator(decorated)))
decorated()

'''Пример 4:
форматирование текста'''


def bold(func):
    def wrapped():
        return '<b>' + func() + '<b>'
    return wrapped


def italic(func):
    def wrapped():
        return '<i>' + func() + '<i>'
    return wrapped


@bold
@italic
def hello():
    return 'hello, world!'

# hello = bold(italic(hello))


print(hello())
