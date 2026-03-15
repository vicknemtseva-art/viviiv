from abc import ABC, abstractmethod
import doctest


class Спорткар(ABC):
    def __init__(self, марка: str, модель: str, год: int):
        if not марка:
            raise ValueError("Марка не может быть пустой")
        if not модель:
            raise ValueError("Модель не может быть пустой")
        if год < 1900 or год > 2025:
            raise ValueError("Некорректный год")

        self.марка = марка
        self.модель = модель
        self.год = год
        self.скорость = 0

    def разогнаться(self, скорость: int) -> str:
        if скорость < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.скорость = скорость
        return f"Разогнался до {скорость} км/ч"

    def __str__(self) -> str:
        return f"{self.марка} {self.модель}"

    def __repr__(self) -> str:
        return f"Спорткар('{self.марка}', '{self.модель}', {self.год})"


class РедБул(Спорткар):
    def __init__(self, модель: str, год: int):
        super().__init__("Red Bull", модель, год)
        self.дрифт_режим = False

    def включить_дрифт(self) -> str:
        self.дрифт_режим = True
        return "Дрифт режим включен"

    def разогнаться(self, скорость: int) -> str:
        self.скорость = скорость
        return f"Red Bull разогнался до {скорость} км/ч"

    def __str__(self) -> str:
        return f"Red Bull {self.модель}"

    def __repr__(self) -> str:
        return f"РедБул('{self.модель}', {self.год})"


class Феррари(Спорткар):
    def __init__(self, модель: str, год: int):
        super().__init__("Ferrari", модель, год)
        self.режим = "спорт"

    def сменить_режим(self, режим: str) -> str:
        self.режим = режим
        return f"Режим {режим}"

    def разогнаться(self, скорость: int) -> str:
        self.скорость = скорость
        return f"Ferrari едет {скорость} км/ч в режиме {self.режим}"

    def __str__(self) -> str:
        return f"Ferrari {self.модель}"

    def __repr__(self) -> str:
        return f"Феррари('{self.модель}', {self.год})"


class Макларен(Спорткар):
    def __init__(self, модель: str, год: int):
        super().__init__("McLaren", модель, год)

    def открыть_двери(self) -> str:
        return "Двери открыты вверх"

    def разогнаться(self, скорость: int) -> str:
        self.скорость = скорость
        return f"McLaren разогнался до {скорость} км/ч"

    def __str__(self) -> str:
        return f"McLaren {self.модель}"

    def __repr__(self) -> str:
        return f"Макларен('{self.модель}', {self.год})"


if __name__ == "__main__":
    rb = РедБул("RB19", 2023)
    print(rb)
    print(rb.включить_дрифт())
    print(rb.разогнаться(300))

    f = Феррари("F40", 1990)
    print(f)
    print(f.сменить_режим("гоночный"))
    print(f.разогнаться(280))

    m = Макларен("P1", 2015)
    print(m)
    print(m.открыть_двери())
    print(m.разогнаться(320))

    doctest.testmod()