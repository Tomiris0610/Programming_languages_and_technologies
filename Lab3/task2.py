class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    def show_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год издания: {self.year}")
        print(f"Количество страниц: {self.pages}")
book = Book("")
book.show_info()
