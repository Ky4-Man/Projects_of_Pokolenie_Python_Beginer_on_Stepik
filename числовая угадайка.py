from random import randrange as rr
import sys


def quit_the_game(input_text: str):
    if input_text.lower() == 'q':
        print('Игра завершена. Всего доброго!')
        sys.exit()


def get_predel():
    while True:
        print(f'Введите целое число X - правую границу последовательности для угадывания от 1 до X')
        predel = input()
        quit_the_game(predel)
        if not predel.isdigit() or int(predel) <= 1:
            print('Нужно ввести целое число больше 1')
            continue
        else:
            return int(predel)


def get_num(predel):
    while True:
        print(f'Введите число от 1 до {predel}')
        num = input()
        quit_the_game(num)
        if not num.isdigit() or not (1 < int(num) <= predel):
            print(f'А может быть все-таки введем целое число от 1 до {predel}?')
            continue
        else:
            return int(num)


def main_game():
    counter = 0
    predel = get_predel()
    hidden_number = rr(1, predel+1)
    while True:
        player_attempt = get_num(predel)
        counter += 1
        if player_attempt < hidden_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        if player_attempt > hidden_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        if player_attempt == hidden_number:
            print('Вы угадали, поздравляем!')
            print(f'У вас ушло {counter} попыток.')
            break


def main():
    print('Добро пожаловать в числовую угадайку!')
    print('Для выхода введите "q"')
    main_game()
    print()
    print('Хотите сыграть ещё разок?) (Введите "да" или "нет")')
    while True:
        question = input()
        quit_the_game(question)
        if question.lower() == 'да':
            main()
        elif question.lower() == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            quit_the_game('q')
        else:
            print('Введите "да" для новой игры, либо "нет" или "q" для выхода')
            continue


if __name__ == "__main__":
    main()
