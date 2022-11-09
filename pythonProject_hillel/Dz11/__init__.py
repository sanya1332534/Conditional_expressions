from Headphones_class import Headphones
from TV_class import TV
from pprint import pprint
import csv
import json

menu = list()
filename = 'products.csv'
numerator = 0
print("Internet-shop Tech_no-stop welcomes you!")
user_input = input("Categories to search in: \n TV \n Headphones \n Choose one: ")

with open(filename, newline='') as csvfile:     # читання файлу csv
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:      # фільтрація за категорією і формування об'єктів для подальшого сортування
        json_field = json.loads(row['additional_fields'])
        row['additional_fields'] = json_field
        if user_input == "TV" and row["category"] == 'TV':
            obj = TV(row['category'], row['name'], row['price'], row['brand'], json_field)
            numerator += 1
            menu.append(obj)
        elif user_input == "Headphones" and row["category"] == 'Headphones':
            obj = Headphones(row['category'], row['name'], row['price'], row['brand'], json_field)
            numerator += 1
            menu.append(obj)

last_shown_objects = menu.copy()  # копіює menu в last_shown_objects для подальшого редагування і виводу

while True:
    pprint(last_shown_objects)
    menu_input = input(f" Found {numerator} products.\nFilter \nReset\nYour choice: ")
    if menu_input == "Filter":  # виконує фільтрацію об'єктів за вибраною категорією
        pole_filter = input('Which field to filter by: ')
        numerator = 0
        value_filter = input("Enter by which value from the available ones to filter: ")
        my_filter = (pole_filter, value_filter)
        filtered_objects = list()
        if my_filter[0] == 'price':
            for obj in last_shown_objects:
                if obj.price == my_filter[1]:   # виконує фільтрацію об'єктів за ціною
                    filtered_objects.append(obj)
                    numerator += 1
        if my_filter[0] == 'name':
            for obj in last_shown_objects:
                if obj.name == my_filter[1]:    # виконує фільтрацію об'єктів за назвою
                    filtered_objects.append(obj)
                    numerator += 1
        if my_filter[0] == 'brand':
            for obj in last_shown_objects:
                if obj.brand == my_filter[1]:       # виконує фільтрацію об'єктів за брендом
                    filtered_objects.append(obj)
                    numerator += 1
        else:
            print("Try again, type: price,name or brand")
        last_shown_objects = filtered_objects.copy()
    elif menu_input == "Reset":
        print(f"Previous {user_input}")
    else:
        print("Try again, type: Filter or Reset")

