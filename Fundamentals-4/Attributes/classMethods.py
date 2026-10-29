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

l2 = Laptop("8GB", "512GB")

l2.get_storage_type()