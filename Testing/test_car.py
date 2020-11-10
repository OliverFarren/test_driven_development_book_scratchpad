import pytest
from car import Car


class TestCar:

    speed_data = {45, 50, 55, 100}

    @pytest.mark.parametrize("speed_accelerate", speed_data)
    def test_car_accelerate(self, speed_accelerate):
        car = Car(50)
        car.accelerate()
        assert car.speed == speed_accelerate

    @pytest.mark.parametrize("speed_brake", speed_data)
    def test_car_brake(self, speed_brake):
        car = Car(50)
        car.brake()
        assert car.speed == speed_brake
