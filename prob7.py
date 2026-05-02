class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, product: str, quantity: int):
        tpl = (product,quantity)
        self.items.append(tpl)
        print(self.items)

    def remove_item(self, product: str):
        self.items = [p for p in self.items if p[0] != product]
        print(self.items)

    def view_cart(self):
        print(self.items)

    def checkout(self, prices: dict[str, float]):
        return sum(prices.values())

savatcha = ShoppingCart()

savatcha.add_item("Olma", 3)
savatcha.add_item("Banan", 2)

savatcha.view_cart()

narxlar = {"Olma": 5000, "Banan": 7000}
print(savatcha.checkout(narxlar))
savatcha.remove_item("Olma")