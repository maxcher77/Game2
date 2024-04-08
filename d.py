def total_score(amount):
    return sum(amount)


def give_reward(points):
    if points > 80:
        return 'Наградить дипломом.'
    elif 50 < points <= 80:
        return 'Наградить похвальной грамотой.'
    else:
        return 'Выдать грамоту об участии.'


while True:
    name = input('Введите имя: (стоп - завершить):')

    if name.lower() == 'стоп':
        break

    subjects = int(input('Число изученных предметов:'))
    s = []

    for i in range(subjects):
        while True:
            score = int(input('Введите балл:'))

            if 0 <= score <= 50:
                break
            else:
                print('Неверное количество баллов. Должно быть от 0 до 50')

        s.append(score)

    total_score = total_score(s)

    print(f'Итоговый счет: {total_score}')
    print(give_reward(total_score))