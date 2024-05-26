import math
import random
from controllers.car.Settings import Settings
from car_scripts.strategies.StrategyInterface import StrategyInterface


class StaticSmoothlyStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float, duration: float) -> tuple[float, float]:
        return x, y

    def generateSteering(self) -> float:
        return math.radians(float(random.randint(
            int(Settings.MIN_STEERING),
            int(Settings.MAX_STEERING),
        )))

    def generateSpeed(self, steering: float) -> float:
        return Settings.MAX_SPEED

    def generatePoints(self, speed: float) -> int:
        return random.randint(10, 40)
