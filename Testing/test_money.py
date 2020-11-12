import pytest

from money import Money


def test_null():
    null = False
    assert null == False


def test_dollar_multiplication():

    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)

    five = Money.francs(5)
    assert Money.francs(10) == five.times(2)
    assert Money.francs(15) == five.times(3)


def test_equality():

    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(5) != Money.dollar(6)

    assert Money.francs(5) != Money.dollar(5)


def test_currency():

    assert("USD" == Money.dollar(1).currency)
    assert("CHF" == Money.francs(1).currency)


def test_addition():

    sum = Money.dollar(5) + Money.dollar(6)

    assert sum == Money.dollar(11)
