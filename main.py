def get_ops():
    return {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }


def calculator():
    ops = get_ops()

    try:
        number1 = float(input('Введите A: '))
        op = input('Введите операцию: ')
        number2 = float(input('Введите B: '))

        res = ops[op](number1, number2)
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
    print(f'{number1} {op} {number2} = {res}')
    input()


def main():
    calculator()


if __name__ == '__main__':
    main()
