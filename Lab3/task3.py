class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
      
    def change_price(self, new_price):
        self.price = new_price
      
    def add_quantity(self, amount):
        self.quantity += amount
      
    def stock_value(self):
        return self.price * self.quantity
      
product = Product("Ноутбук", 300000, 5)

print(f"Товар: {product.name}")
print(f"Цена: {product.price} тг")
print(f"Количество: {product.quantity}")
print(f"Стоимость запасов: {product.stock_value()} тг")

product.change_price(320000)
product.add_quantity(2)

print("\nПосле изменений:")
print(f"Новая цена: {product.price} тг")
print(f"Новое количество: {product.quantity}")
print(f"Стоимость запасов: {product.stock_value()} тг")
