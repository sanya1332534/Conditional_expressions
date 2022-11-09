
class Products:
    """Базовий клас для всіх товарів"""
    def __init__(self, category, name: str, price: int, brand: str):
        """
        Метод ініціалізації, в якому задаються атрибути классу
        :param category: категорія
        :param name: ім'я
        :param brand: бренд
        :param additional_fields: додаткові поля, блютуз
        """
        self.category = category
        self.name = name
        self.price = price
        self.brand = brand

