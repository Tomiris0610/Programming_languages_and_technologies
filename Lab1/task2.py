num = int(input("Введите трехзначное число:"))

a = num // 100
b = num // 10 % 10
c = num % 10

summ = a + b + c
proizvedenie = a * b * c

print("Сумма:", summ)
print("Произведение:", proizvedenie)
