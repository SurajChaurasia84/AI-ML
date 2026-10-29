# product store

class Product:
    count = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
        self.count

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")

p1 = Product("phone", 10_000)
p2 = Product("laptop", 50_000)
p3 = Product("pen", 10)

Product.get_count()