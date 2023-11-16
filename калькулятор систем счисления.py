def transfer(number_to_convert, from_which_system='10', to_which_system='2'):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    if int(from_which_system) > len(digits):
        return None
    number_to_convert = int(number_to_convert, int(from_which_system))

    while number_to_convert > 0:
        result = digits[number_to_convert % int(to_which_system)] + result
        number_to_convert //= int(to_which_system)
    return result.upper()


def main():
    from_notation = input('Из какой системы счисления хотите перевести? Введите число (2 - двоичная, '
                          '8 - восьмеричная и т.п.)\n')
    to_notation = input('В какую систему счисления хотите перевести? Введите число (2 - двоичная, '
                        '8 - восьмеричная и т.п.)\n')
    the_number = input('Введите число, которое хотите перевести:\n')
    print(f'Результат: {transfer(the_number, from_notation, to_notation)}')


if __name__ == "__main__":
    main()
