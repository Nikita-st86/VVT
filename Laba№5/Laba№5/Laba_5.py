class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'Book: {self.title}; {self.author}; {self.year}'

title, author, year = input().strip(), input().strip(), int(input().strip())
book = Book(title, author, year)
print(book)


radius1 = int(input("Введите радиус:"))
new_radius1 = int(input("Введите новый радиус:"))
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
        return self.radius
circle = Circle(radius1)
print("Старый Радиус:", circle.get_radius())
print("Новый радиус:", circle.set_radius(new_radius1))
