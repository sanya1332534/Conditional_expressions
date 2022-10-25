class Triangle:
    def __init__(self, name: str, a, b, c):
        """
        Метод ініціалізації, в якому задаються атрибути классу
        :param name: назва трикутнику
        :param a, b, c: довжини сторін трикутника
        """
        self.name = name
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def perimeter_area(self):
        """
            Функція рахує периметр трикутника, виводить її на екран
            :param self: силка на сам об'єкт цього классу
        """
        p_triangle = self.a + self.b + self.c
        print(f"Периметр трикутника {self.name} {p_triangle}")

    def area(self):
        """
            Функція рахує площу трикутника, виводить її на екран
            :param self: силка на сам об'єкт цього классу
        """
        p_half_triangle = (self.a + self.b + self.c) / 2
        s_triangle = pow((p_half_triangle * (p_half_triangle - self.a) * (p_half_triangle - self.b) * (p_half_triangle - self.c)), 1 / 2)
        print(f"Площа трикутника {self.name} {round(s_triangle, 3)}")

    def exists(self):
        """
            Функція перевіряє чи може існувати трикутник
            :param self: силка на сам обєкт цього классу
            :return: повертає True, якщо трикутник може існувати або False, якщо не може
        """
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False


if __name__ == '__main__':
    triangle1 = Triangle(name="triangle_1", a=1, b=1, c=1.41)
    triangle2 = Triangle(name="triangle_2", a=2, b=5, c=5)
    triangle3 = Triangle(name="triangle_3", a=1, b=5, c=15)
    if triangle1.exists():
        triangle1.perimeter_area()
        triangle1.area()
    else:
        print(f"Triangle {triangle1.name} does not exists")
    print('\t')

    if triangle2.exists():
        triangle2.perimeter_area()
        triangle2.area()
    else:
        print(f"Triangle {triangle2.name} does not exists")
    print('\t')
    if triangle3.exists():
        triangle3.perimeter_area()
        triangle3.area()
    else:
        print(f"Triangle {triangle3.name} does not exists")



