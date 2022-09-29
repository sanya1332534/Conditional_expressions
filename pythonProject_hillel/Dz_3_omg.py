
hallo_words = ['привіт', 'хай', 'Доброго дня']
ask_words = ['як справи?', 'що робиш?', 'чим займаєшся?']
film_words = ['фільм', 'кінотеатр', 'серіал']
bye_words = ['бувай', 'надобраніч', 'гудбай', 'до зустрічі']

t = 0
s = 0
break_0 = 0

while True:
    str_1 = input("Строка-звернення від користувача:")
    str_ = str_1.lower()
    t += 1

    for el in hallo_words:
        if el in str_:
            print('Доброго вечора, я бот з України!')
            s += 1

    for el in ask_words:
        if el in str_:
            print('Вчусь програмувати на Python!')
            s += 1

    for el in film_words:
        if el in str_:
            print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться фільм Дім великої матусі, він просто бомба!')
            s += 1

    for el in bye_words:
        if el in str_:
            print("Побачимось у мережі, I'll be back")
            break_0 += 1
            s += 1

    if s < t:
        print('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :(')
        s += 1
    elif break_0 == 1:
        break

