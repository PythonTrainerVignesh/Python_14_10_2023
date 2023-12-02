import csv


class Products:
    all = []
    discount = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"{price} is less than 0"
        assert quantity >= 0, f"{quantity} is less than 0"
        assert len(name) > 2, f"{name} is less than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        Products.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def discounted_price(self):
        return Products.total_price(self) * self.discount

    @classmethod
    def data_init(cls):
        with open('new.csv', 'r') as file:
            data = csv.DictReader(file)
            x = list(data)
            for i in x:
                Products(
                    name=i.get('name'),
                    price=float(i.get('price')),
                    quantity=int(i.get('quantity'))
                )

    def __repr__(self):
        return f"Products('{self.name}', {self.price}, {self.quantity})"


Products.data_init()
print(Products.all)
