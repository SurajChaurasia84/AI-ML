class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price / 100)
        print(f"final price = {final_price}")

l2 = Laptop("8GB", "512GB")

l2.calc_discount(40_000, 10)