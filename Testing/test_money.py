from money import Dollar


def test_null():
    null = False
    assert null == False


def test_multiplication():

    five = Dollar(5)
    five.times(2)
    assert five.amount == 10