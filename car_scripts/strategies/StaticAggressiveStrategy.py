import math
import random
from controllers.car.Settings import Settings
from car_scripts.strategies.StrategyInterface import StrategyInterface


class StaticAggressiveStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float, duration: float) -> tuple[float, float]:
        for _ in range(random.randint(10, 20)):
            x += speed * math.cos(yaw) * duration  # [m]
            y += speed * math.sin(yaw) * duration  # [m]

        return x, y

    def generateSteering(self) -> float:
        return math.radians(random.choice([
            float(random.randint(
                int(Settings.MIN_STEERING),
                -35,
            )),
            float(random.randint(
                35,
                int(Settings.MAX_STEERING),
            )),
        ]))

    def generateSpeed(self, steering: float) -> float:
        return Settings.MAX_SPEED

    def generatePoints(self, speed: float) -> int:
        return random.randint(10, 20)
