# app/shape.py
class Shape:
    def __init__(self):
        self.__name = "Shape"  # Приватный атрибут

    @staticmethod
    def about():
        print("Команда разработки: Программа расчета объема конуса.")
