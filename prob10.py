class Order:
    def __init__(self, id: int, customer_name: str):
        self.id = id
        self.c_n = customer_name
        self.items = []
        self.total_price = 0

    def add_item(self, product: str, price: float, quantity: int):
        tpl = (product, price, quantity)
        self.items.append(tpl)
        print(self.items)

    def remove_item(self, product: str):
        self.items = [p for p in self.items if p[0] != product]
        print(self.items)

    def calculate_total(self):
        for price in self.items:
            self.total_price+=price[1] * price[2]
        print(self.total_price)

    def __str__(self):
        return f"\n{self.id} {self.c_n}"


buyurtma = Order(id=1, customer_name="Javohir Karimov")

buyurtma.add_item("Olma", 5000, 3)
buyurtma.add_item("Banan", 7000, 2)

buyurtma.calculate_total()

buyurtma.remove_item("Banan")

print(buyurtma)