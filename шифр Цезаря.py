def language_check(language, text: str):
    rus_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    eng_low = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    alphabet = []

    if language == 'rus':
        alphabet += [rus_low, rus_upper]
    elif language == 'eng':
        alphabet += [eng_low, eng_upper]

    for i in text:
        if i.isalpha() and ((i not in alphabet[0]) and (i not in alphabet[1])):
            return False

    return True


def encrypt(language, direction, shift, text: str):
    rus_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    eng_low = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = ''
    alphabet = []

    # Объединение направления шифровки (+ или -) и её шага
    shift = shift*direction

    # Составление алфавита в соответствие с выбранным языком
    if language == 'rus':
        alphabet += [rus_low, rus_upper]
    elif language == 'eng':
        alphabet += [eng_low, eng_upper]

    for i in text:
        if not i.isalpha():
            result += i

        elif i.islower():
            result += alphabet[0][(alphabet[0].index(i) + shift) % len(alphabet[0])]

        elif i.isupper():
            result += alphabet[1][(alphabet[1].index(i) + shift) % len(alphabet[1])]

    return result


def main():
    print('Добро пожаловать в шифратор Цезаря!)')

    # Запрос выбора: шифрование или дешифрование
    shifr = int(input('Выберите направление: шифрование или дешифрование. '
                  '(напишите "1" для шифрования и "0" для дешифровки)\n'))
    if shifr:
        shifr = 1
    else:
        shifr = -1

    # Запрос выбора - какой язык
    lang = int(input('Выберите язык текста: английский или русский без буквы "ё". '
                 '(для английского введите "1", для русского введите "0")\n'))
    if lang:
        lang = 'eng'
    else:
        lang = 'rus'

    # Запрос выбора - шаг сдвига
    rot = int(input('Введите шаг сдвига. (целое число)\n'))

    # Проверка текста на соответствие выбранному языку
    while True:
        text = input('Введите текст для шифрования / дешифрования\n')
        if language_check(lang, text):
            break
        else:
            print('Введенный текст не соответствует выбранному языку.\n')
            continue

    print('\nРезультат шифрования / дешифрования:\n')
    print(encrypt(lang, shifr, rot, text))


if __name__ == "__main__":
    main()
