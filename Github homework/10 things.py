firstSet = {"Нож", "Запасы питьевой воды", "Спички", "Палатка", "Медицинская аптечка", "Солнечные панели", "Книги", "Палка для ходьбы", "Средство для очистки воды", "Сигнальная ракета"}
secondSet = {"Нож", "Крем от загара", "Контейнер для хранения воды", "Удочка", "Палатка", "Аптечка", "Компас", "Солнечные панели", "Спички", "Бинокль"}
print("Множество вещей, которые бы взяли двое: ", firstSet.intersection(secondSet))
print("Множество вещей, которые бы взял только первый: ", firstSet.difference(secondSet))