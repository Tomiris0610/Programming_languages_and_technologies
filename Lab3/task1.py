class Student:
    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty
    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Специальность: {self.specialty}")
    def change_specialty(self, new_specialty):
        self.specialty = new_specialty
# Создание объекта
student = Student()
# Вывод информации
student.show_info()
# Изменение специальности
student.change_specialty()
print("\nПосле изменения специальности:")
student.show_info()
