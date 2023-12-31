from random import choice
import sys


def select_answer():
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
               'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
               'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
               'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
               'Перспективы не очень хорошие', 'Весьма сомнительно']
    pretext = ['Вселенная шепчет...', 'Я слышу...', 'Вселенная отвечает...', 'Ответ на твой вопрос...',
               'Услышь же ответ!', 'Ты должен знать...', 'Истина открывается...', 'Всё, что тебе нужно знать...']
    print(choice(pretext))
    print(choice(answers))


def main():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    print('Как твоё имя?')
    name = input()
    print(f'Привет, {name}!')
    print(f'Задай свой вопрос, а я попробую узнать у вселенной ответ на него!')
    input()
    select_answer()
    while True:
        print('Хочешь ли ты задать ещё вопрос? (напиши "да" или "нет")')
        answer = input()
        if answer.lower() == 'нет':
            print('Возвращайся если возникнут вопросы!')
            sys.exit()
        elif answer.lower() == 'да':
            print('Задай же свой вопрос!')
            input()
            select_answer()
            continue
        else:
            print('Я тебя не понял...')
            continue


if __name__ == "__main__":
    main()
