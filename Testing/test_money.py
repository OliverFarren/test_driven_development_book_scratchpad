import pytest

from money import Money
from money import Bank

def test_null():
    null = False
    assert null == False


def test_dollar_multiplication():

    five = Money.dollar(5)
    ten = Money.dollar(10)

    assert Money.dollar(50) == five * ten
    assert Money.dollar(50) == ten * 5
    assert Money.dollar(50) == 10 * five
    assert Money.dollar(60) == 2 * five * 6

def test_equality():

    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)

    assert Money.francs(5) != Money.dollar(5)


def test_currency():

    assert("USD" == Money.dollar(1).currency)
    assert("CHF" == Money.francs(1).currency)


def test_simple_addition():

    five = Money.dollar(5)
    money_sum = five + five
    bank = Bank()
    reduced = bank.exchange(money_sum, "USD")
    assert Money.dollar(10) == reduced


def test_identity_rate():

    bank = Bank()
    assert 1 == bank.get_rate("USD", "USD")


def test_reduce_money_different_currency():

    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.exchange(Money.francs(2), "USD")

    assert Money.dollar(1) == result


def test_mixed_addition():

    five_bucks = Money.dollar(5)
    ten_francs = Money.francs(10)

    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    result = five_bucks + bank.exchange(ten_francs, "USD")

    assert result == Money.dollar(10)