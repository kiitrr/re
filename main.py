# app/main.py
from app.cone import Cone

if __name__ == "__main__":
    # Вывод информации о команде разработки
    Cone.about()

    # Создание объекта конуса с радиусом 5 и высотой 10
    cone = Cone(5, 10)
    
    # Вывод объема конуса
    cone.dump()
