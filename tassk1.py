class Book:
    """Класс, представляющий книгу."""

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        Параметры:
            id_: идентификатор книги (целое положительное число)
            name: название книги (непустая строка)
            pages: количество страниц (целое положительное число)
        """
        # Валидация данных
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("id должен быть положительным целым числом")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("название должно быть непустой строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages должен быть положительным целым числом")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        Возвращает:
            str: строка с названием книги в формате 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает валидную Python строку для создания такого же экземпляра.

        Возвращает:
            str: строка вида "Book(id_=1, name='test_name_1', pages=200)"
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# Данные из задания
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__