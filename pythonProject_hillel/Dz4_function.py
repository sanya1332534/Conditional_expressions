def uah_to_usd():
    uah = float(input("Enter the amount of hryvnias => "))
    usd = 40
    print(round(uah / usd, 2))


def usd_to_uah():
    usd = float(input("Enter the amount of usd => "))
    uah = 0.025
    print(round(usd / uah, 2))


def user_choice1():
    user_choice = input("What exactly do you want to convert(your choice write 1 or 2)?")
    if user_choice == '1':
        uah_to_usd()
    elif user_choice == '2':
        usd_to_uah()
    else:
        print("You have only two way of converting")


print(""""
    1.  uah to usd
    2.  usd to uah
""")
user_choice1()
