def user_input_0():
    print("Введіть сторони опуклого чотирикутника:")
    side_1 = float(input("сторона 1 "))
    side_2 = float(input("сторона 2 "))
    side_3 = float(input("сторона 3 "))
    side_4 = float(input("сторона 4 "))
    return side_1, side_2, side_3, side_4


counter_1 = 0


def check_for_square(side_1, side_2, side_3, side_4):
    if side_1 == side_2 == side_3 == side_4:
        print("Ваш чотирикутник квадрат")
        global counter_1
        counter_1 += 1
        return counter_1


def check_for_rectangle(side_1, side_2, side_3, side_4):
    if side_1 ** 2 + side_2 ** 2 == side_3 ** 2 + side_4 ** 2 or side_3 ** 2 + side_2 ** 2 ==\
            side_1 ** 2 + side_4 ** 2 or side_4 ** 2 + side_2 ** 2 == side_1 ** 2 + side_3 ** 2:
        if not check_for_square(side_1, side_2, side_3, side_4):
            print("Ваш чотирикутник прямокутник")
            s_rectangle(side_1, side_2, side_3, side_4)

    else:
        print("Ваш чотирикутник не є ні квадратом ,ні прямокутником")


def s_rectangle(side_1, side_2, side_3, side_4):
    if counter_1 == 0:
        s_rec = max(side_1, side_2, side_3, side_4) * min(side_1, side_2, side_3, side_4)
        print(f"Площа вашого прямокутника : {s_rec}")


check_for_rectangle(*user_input_0())


