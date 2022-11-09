from Products_class import Products


class Headphones(Products):
    """
    Клас для товарів Headphones
    :param1 : Базовий клас для всіх товарів
    """
    def __init__(self, category, name: str, price: int, brand: str, additional_fields):
        """
        Функція __init__ викликається щоразу, коли об'єкт створюється із класу.
        Метод __init__ дозволяє класу ініціалізувати атрибути об'єкта
        :param category: категорія
        :param name: ім'я
        :param brand: бренд
        :param additional_fields: додаткові поля, блютуз
        """
        super().__init__(category, name, price, brand)
        self.category = category
        self.name = name
        self.price = price
        self.brand = brand
        self.additional_fields = additional_fields

    def __repr__(self):
        """
        Видає текстове представлення об'єкту
        :param self: силка на сам обєкт цього классу
        :return: повертає текстове значення об'єкту
        """
        return f"Name: {self.name}\n price: {self.price}uah\n brand: {self.brand}\n aditional: {self.additional_fields}\n"
