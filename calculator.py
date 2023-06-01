def get_ops():
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }


def calculator():
    d = get_ops()

    try:
        a = float(input('Введите A: '))
        op = input('Введите операцию: ')
        b = float(input('Введите B: '))

        res = d[op](a, b)
    except ValueError:
        print('Неверный формат числа!')
        return
    except KeyError:
        print('Неизвестная операция!')
        return
    except ZeroDivisionError:
        print('Деление на ноль запрещено!')
        return

    print('Результат:')
    print(f'{a} {op} {b} = {res}')

