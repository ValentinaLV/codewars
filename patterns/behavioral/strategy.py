# https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e
from abc import ABC, abstractmethod


class QuackStrategy(ABC):
    @abstractmethod
    def quack(self):
        """Required Method"""


class LoudQuackStrategy(QuackStrategy):
    def quack(self):
        print("QUACK! QUACK!!")


class GentleQuackStrategy(QuackStrategy):
    def quack(self):
        print("quack!")


class LightStrategy(ABC):
    @abstractmethod
    def lights_on(self):
        """Required Method"""


class OnForTenSecondsStrategy(LightStrategy):
    def lights_on(self):
        print("Lights on for 10 seconds")


loud_quack = LoudQuackStrategy()
gentle_quack = GentleQuackStrategy()
ten_seconds = OnForTenSecondsStrategy()


class Duck(object):
    def __init__(self, quack_strategy, light_strategy):
        self._quack_strategy = quack_strategy
        self._light_strategy = light_strategy

    def quack(self):
        self._quack_strategy.quack()

    def lights_on(self):
        self._light_strategy.lights_on()


# Types of Ducks
class VillageDuck(Duck):
    def __init__(self):
        super().__init__(loud_quack, None)

    def go_home(self):
        print("Going to the river")


class CityDuck(Duck):
    def __init__(self):
        super().__init__(gentle_quack, None)

    def go_home(self):
        print("Going to the Central Park pond")


class ToyDuck(Duck):
    def __init__(self):
        super(ToyDuck, self) \
            .__init__(gentle_quack, ten_seconds)


class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self) \
            .__init__(loud_quack, ten_seconds)


robot_duck = RobotDuck()
robot_duck.quack()
robot_duck.lights_on()
