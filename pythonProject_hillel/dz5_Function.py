def user_input_0():
    print("Введіть сторони опуклого чотирикутника:")
    side_1 = float(input("сторона 1 "))
    side_2 = float(input("сторона 2 "))
    side_3 = float(input("сторона 3 "))
    side_4 = float(input("сторона 4 "))
    return side_1, side_2, side_3, side_4


side_1, side_2, side_3, side_4 = user_input_0()
counter_1 = 0


def check_for_rectangle():
    if side_1 ** 2 + side_2 ** 2 == side_3 ** 2 + side_4 ** 2 or side_3 ** 2 + side_2 ** 2 ==\
            side_1 ** 2 + side_4 ** 2 or side_4 ** 2 + side_2 ** 2 == side_1 ** 2 + side_3 ** 2:
        print("Ваш чотирикутник прямокутник")
        s_rectangle()
    else:
        print("Ваш чотирикутник не є ні квадратом ,ні прямокутником")


def check_for_square():
    if side_1 == side_2 == side_3 == side_4:
        print("Ваш чотирикутник квадрат")
        global counter_1
        counter_1 += 1
        return counter_1


def s_rectangle():
    s_rec = max(side_1, side_2, side_3, side_4) * min(side_1, side_2, side_3, side_4)
    print(f"Площа вашого прямокутника : {s_rec}")


check_for_square()
if counter_1 == 0:
    check_for_rectangle()



