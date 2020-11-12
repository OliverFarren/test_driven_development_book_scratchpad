
# Step 1: Multiplication

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount \
                   and self.currency == other.currency
        else:
            raise TypeError(f'Expecting type Money, received type:{type(other)}')

    def __add__(self, other):
        return Money(self.amount+other.amount, self.currency)

    @property
    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def francs(amount):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self.amount*multiplier, self.currency)




