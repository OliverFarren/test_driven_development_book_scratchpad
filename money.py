
# Step 1: Multiplication
import numbers


def pair_str(string1, string2):
    return f'{string1}_{string2}'


class Bank:

    def __init__(self):
        self.rates = dict()

    def exchange(self, money, to_currency):
        rate = self.get_rate(money.currency, to_currency)
        return Money(money.amount/rate, to_currency)

    def add_rate(self, from_currency, to_currency, rate):
        self.rates[pair_str(from_currency, to_currency)] = rate

    def get_rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        elif pair_str(from_currency, to_currency) in self.rates:
            return self.rates[pair_str(from_currency, to_currency)]
        else:
            raise KeyError(f'KeyError, {__class__.__name__} has no rate for {from_currency} - {to_currency}')


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
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount+other.amount, self.currency)
            else:
                raise ValueError(f'Expected same currency and got: {self.currency},{other.currency}')
        elif isinstance(other, numbers.Real):
            return Money(self.amount+other, self.currency)
        else:
            raise TypeError(f'Expected type Money or Numeric, received type{other}')

    def __radd__(self, other):
        return self * other

    def __mul__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return Money(self.amount*other.amount, self.currency)
            else:
                raise ValueError(f'Expected same currency and got: {self.currency},{other.currency}')
        elif isinstance(other, numbers.Real):
            return Money(self.amount*other, self.currency)
        else:
            raise TypeError(f'Expected type Money or Numeric, received type{other}')

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        return f'{__class__.__name__} in currency:{self.currency}, amount:{self.amount}'

    @property
    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def francs(amount):
        return Money(amount, "CHF")





