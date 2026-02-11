from abc import ABC, abstractmethod
from datetime import date
import doctest


class Sheep:
    """Овца как сельскохоз животное."""

    def __init__(self, name: str, age: int, weight: float):
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if age < 0 or age > 15:
            raise ValueError("Возраст овцы от 0 до 15 лет")
        if weight < 2 or weight > 200:
            raise ValueError("Вес овцы от 2 до 200 кг")

        self.name = name
        self.age = age
        self.weight = weight

    def bleat(self) -> str:
        """
        Издать звук.

        >>> sheep = Sheep("Бараш", 3, 50)
        >>> sheep.bleat()
        'Бе!'
        """
        return "Бе!"

    def shear(self) -> float:
        """
        Постричь овцу.

        >>> sheep = Sheep("Долли", 2, 45)
        >>> wool = sheep.shear()
        >>> wool > 0
        True
        """
        return self.weight * 0.1


class Meadow:
    """Луг как место обитания."""

    def __init__(self, area: float, grass_height: int, location: str):
        if area <= 0:
            raise ValueError("Площадь луга должна быть > 0")
        if grass_height < 0 or grass_height > 100:
            raise ValueError("Высота травы от 0 до 100 см")
        if not location.strip():
            raise ValueError("Укажите местоположение")

        self.area = area
        self.grass_height = grass_height
        self.location = location

    def grow_grass(self, days: int) -> None:
        """
        Трава растет.

        >>> meadow = Meadow(100, 10, "Зеленые холмы")
        >>> meadow.grow_grass(5)
        >>> meadow.grass_height > 10
        True
        """
        self.grass_height += days * 0.5

    def graze(self, sheep_count: int) -> float:
        """
        Сколько травы съедят.

        >>> meadow = Meadow(100, 20, "Луга")
        >>> grass_eaten = meadow.graze(10)
        >>> grass_eaten > 0
        True
        """
        eaten = sheep_count * 0.3
        self.grass_height -= eaten
        if self.grass_height < 0:
            self.grass_height = 0
        return eaten


class Shepherd:
    """Пастух."""

    def __init__(self, name: str, experience: int, dogs: int):
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if experience < 0 or experience > 60:
            raise ValueError("Стаж от 0 до 60 лет")
        if dogs < 0 or dogs > 10:
            raise ValueError("Не более 10 собак")

        self.name = name
        self.experience = experience
        self.dogs = dogs

    def herd(self, sheep_list: list) -> str:
        """
        Пасти овец.

        >>> shepherd = Shepherd("Иван", 10, 2)
        >>> result = shepherd.herd(["Бараш", "Долли", "Кудряш"])
        >>> "пасет" in result
        True
        """
        return f"{self.name} пасет {len(sheep_list)} овец"

    def count_sheep(self, sheep_list: list) -> int:
        """
        Пересчитать овец.

        >>> shepherd = Shepherd("Петр", 5, 1)
        >>> count = shepherd.count_sheep(["овца1", "овца2", "овца3"])
        >>> count
        3
        """
        return len(sheep_list)


if __name__ == "__main__":
    doctest.testmod(verbose=True)