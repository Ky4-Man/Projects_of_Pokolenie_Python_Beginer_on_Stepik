from random import choice


def password_generator(l: int, ch: str):
    result = ''
    for i in range(l):
        result += choice(ch)
    return result


def answer_check(x):
    if x.lower() != 'да' or x.lower() != 'нет':
        return False
    else:
        return True


def main():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    exept = 'il1Lo0O'
    chars = ''

    answer = {'да': True, 'нет': False}
    print('Сколько паролей вы хотите сгенерировать? (введите число)')
    quantity = int(input())
    print('Какая длинна паролей необходима? (в количестве символов)')
    lenght = int(input())

    print('Включать ли цифры 0123456789 ? (введите "да" или "нет")')
    digits_list = answer[input().lower()]
    if digits_list:
        chars += digits

    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? (введите "да" или "нет")')
    big_letters = answer[input().lower()]
    if big_letters:
        chars += uppercase_letters

    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? (введите "да" или "нет")')
    little_letters = answer[input().lower()]
    if little_letters:
        chars += lowercase_letters

    print('Включать ли символы !#$%&*+-=?@^_ ? (введите "да" или "нет")')
    symbols = answer[input().lower()]
    if symbols:
        chars += punctuation

    print('Исключать ли неоднозначные символы il1Lo0O ? (введите "да" или "нет")')
    exeptions = answer[input().lower()]
    if exeptions:
        temper = ''
        for i in chars:
            if i not in exept:
                temper += i
        chars = temper

    print()
    print('Ваши пароли:')
    for i in range(quantity):
        print(password_generator(lenght, chars))


if __name__ == "__main__":
    main()
