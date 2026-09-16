class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга «{book}» добавлена.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Книга «{book}» удалена.")
        else:
            print("Книга не найдена.")

    def search_book(self, title):
        if title in self.books:
            print(f"Книга «{title}» найдена.")
        else:
            print("Книга не найдена.")
library = Library()
library.add_book("Мастер и Маргарита")
library.add_book("Гарри Поттер")
library.add_book("Убийство в Восточном экспрессе")
print("\nПоиск:")
library.search_book("Гарри Поттер")
print("\nУдаление:")
library.remove_book("Гарри Поттер")
print("\nПовторный поиск:")
library.search_book("Гарри Поттер")
