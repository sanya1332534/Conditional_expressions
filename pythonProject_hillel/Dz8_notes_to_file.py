import os


def add():  # додає нотатку в "глобальний" список
    user_inp = input("Введіть нотатку:")
    notes_list_0.append(user_inp)
    print('\n')
    return notes_list_0


def notes_list_2(notes_list_0):  # видає копію списку для сортування
    notes_list_1 = notes_list_0.copy()
    return notes_list_1


def earliest(notes_list_1):  # сортує від найранішої до найпізнішої нотатки
    print("Від найранішої до найпізнішої")
    for notes in notes_list_1:
        print(notes)
    print('\n')


def latest(notes_list_1):   # сортує від найпізнішої до найранішої нотатки
    print("Від найпізнішої до найранішої")
    notes_list_1.reverse()
    for notes in notes_list_1:
        print(notes)
    print('\n')


def longest(notes_list_1):  # сортує від найдовшої до найкоротшої нотатки
    print("Від найдовшої до найкоротшої")
    notes_list_1.sort(key=len)
    notes_list_1.reverse()
    for notes in notes_list_1:
        print(notes)
    print('\n')


def shortest(notes_list_1):  # сортує від найкоротшої до найдовшої нотатки
    print("Від найкоротшої до найдовшої")
    notes_list_1.sort(key=len)
    for notes in notes_list_1:
        print(notes)
    print('\n')


def save():  # зберігає всі активні нотатки у службовий файл
    with open(filename, mode='a') as fp:
        for notes in notes_list_0:  # кожен елемент з notes_list_0 зберігає в файл, порядках
            fp.writelines(f'{notes} ')


def load():  # завантажує нотатки з file_to_writeDZ8.txt, виводить їх на екран, розбиває по пробілам на елементи списку
    with open(filename) as fp:
        text_notes = fp.readlines()
        print("Нотатки імпотровано з файлу, тепер ви можете продовжити роботу з ними")
        for line in text_notes:
            all_lines = line.split()
        for notes in all_lines:
            print(notes)
            notes_list_0.append(notes)


filename = 'file_to_writeDZ8.txt'
notes_list_0 = list()

while True:
    user_choice = input(">")
    if user_choice == "add":
        add()
    elif user_choice == "earliest":
        earliest(notes_list_2(notes_list_0))
    elif user_choice == "latest":
        latest(notes_list_2(notes_list_0))
    elif user_choice == "longest":
        longest(notes_list_2(notes_list_0))
    elif user_choice == "shortest":
        shortest(notes_list_2(notes_list_0))
    elif user_choice == "save":  # зберігає всі активні нотатки у file_to_writeDZ8.txt
        save()
    elif user_choice == "load":  # завантажує збережені нотатки з file_to_writeDZ8.txt
        load()
    elif user_choice == "clear":  # видаляє всі збережені нотатки та file_to_writeDZ8.txt
        os.remove(filename)
    elif user_choice == "exit":  # вихід з програми, без збереження
        break
    else:
        print("Введіть одне із доступних значень:add, earliest, latest, longest, shortest, save, load, clear, exit")
