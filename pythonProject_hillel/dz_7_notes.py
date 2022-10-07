def notes_list():
    notes_list_0 = list()
    return notes_list_0


def cycle_while(notes_list_0):
    while True:
        user_choice = input(">")
        if user_choice == "add":
            user_inp = input("Введіть нотатку:")
            notes_list_0.append(user_inp)
            print('\n')
        elif user_choice == "earliest": #виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
            print("Від найранішої до найпізнішої")
            notes_list_1 = notes_list_0.copy()
            for notes in notes_list_1:
                print(notes)
            print('\n')
        elif user_choice == "latest":   #виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
            print("Від найпізнішої до найранішої")
            notes_list_1 = notes_list_0.copy()
            notes_list_1.reverse()
            for notes in notes_list_1:
                print(notes)
            print('\n')
        elif user_choice == "longest":  #виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
            print("Від найдовшої до найкоротшої")
            notes_list_1 = notes_list_0.copy()
            notes_list_1.sort(key=len)
            notes_list_1.reverse()
            for notes in notes_list_1:
                print(notes)
            print('\n')
        elif user_choice == "shortest": #виводить збережені  нотатки у порядку їх довжини - від найкоротшої до найдовшої
            print("Від найкоротшої до найдовшої")
            notes_list_1 = notes_list_0.copy()
            notes_list_1.sort(key=len)
            for notes in notes_list_1:
                print(notes)
            print('\n')
        else:
            print("Введіть одне із доступних значень:add, earliest, longest, shortest")


cycle_while(notes_list())




