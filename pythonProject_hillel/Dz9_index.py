import json
from pprint import pprint
from uuid import uuid4


def display_people_data(d: dict) -> str:
    """
    Читаємо та репрезентативно формує рядок для виводу повних данних про одну людину
    :param d: повні данні про цю людину
    :return: вертає сформований рядок про людину
    """
    return f'{d["full name"]} відноситься до {d["category"]} і має рейтинг #{d["rating"]}'


def view_index(index_name: str, index_to_view: dict, source_uid_data: dict):
    """
    Функція виводить на екран в читаємому репрезентативному виді
    людей, розділених по признаку index_name (в index_to_view)
    :param index_name: назва нашого індексу для виводу
    :param index_to_view: сам індекс, словник списком.
    :param source_uid_data: повні данні людей промарковані своїм id
    :return: нічого
    """
    print(f'Люди за індексом {index_name.capitalize()}')
    for key, values in index_to_view.items():
        print(f'Відображення людей з {key} :')
        for uid in values:
            print(f'    {display_people_data(source_uid_data[uid])}')


data = json.load(open('people.json', mode='r'))
# індекси всіх людей
uid_index = dict()

category_index = dict()
rating_index = dict()

print('Люди за індексом id')
# проходимось по данним кожної людини
for people_data in data['people']:
    # присвоюємо кожному унікальний id
    people_data['uid'] = str(uuid4())
    # заповнюємо поле з повним ім'ям людини
    people_data['full name'] = f"{people_data['name']} {people_data['surname']}"
    # додоємо ссилку на повні данні людей в індекс id
    uid_index[people_data['uid']] = people_data

    if people_data['category'] in category_index:
        category_index[people_data['category']].append(people_data['uid'])

    else:
        category_index[people_data['category']] = list()
        category_index[people_data['category']].append(people_data['uid'])

    if people_data['rating'] in rating_index:
        rating_index[people_data['rating']].append(people_data['uid'])
    else:
        rating_index[people_data['rating']] = list()
        rating_index[people_data['rating']].append(people_data['uid'])

pprint(uid_index)
print('\n')
view_index('категорія', category_index, uid_index)
print('\n')
view_index('рейтинг', rating_index, uid_index)

# зберігаємо данні про людей в форматі списку
json.dump({'people': list(uid_index.values())}, open('people.json', 'w'), indent=4)

