a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

perimeter = a + b + c
p = perimeter / 2  # полупериметр

# Вычисление площади по формуле Герона: S = sqrt(p * (p - a) * (p - b) * (p - c))
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

# Вывод результатов
print(f"Периметр: {perimeter}")
print(f"Полупериметр: {p}")
print(f"Площадь (по формуле Герона): {area:.2f}")
