class Bankaccount:
    def __init__(self, name, balance):
        self.name = name #public
        self._balance = balance #private

    def get_balance(self):
        return self._balance

acc1 = Bankaccount("Rahul Kumar", 100_000)

print(acc1.name, acc1.get_balance())