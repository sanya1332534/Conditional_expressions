
str_list = []
while True:
    a = input("Ваше число:")

    if a == "sum":
        break
    if a != "sum":
        str_list.append(a)


def str_to_num(str_1):
    str_1 = str_1.strip()
    if '.' in str_1 and str_1.replace('.', '').isdigit():
        return float(str_1)
    elif '-' in str_1:
        return float(str_1) * 2 - float(str_1)
    elif str_1.isdigit():
        return float(str_1)


num_list = []
for i in str_list:
    n = str_to_num(i)
    if n is not None:
        num_list.append(str_to_num(i))

print(sum(num_list))

