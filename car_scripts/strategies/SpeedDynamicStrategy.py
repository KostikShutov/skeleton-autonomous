import math
import random
from controllers.car.Settings import Settings
from car_scripts.strategies.StrategyInterface import StrategyInterface


class SpeedDynamicStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float, duration: float) -> tuple[float, float]:
        return x, y

    def generateSteering(self) -> float:
        return math.radians(float(random.randint(
            int(Settings.MIN_STEERING),
            int(Settings.MAX_STEERING),
        )))

    def generateSpeed(self, steering: float) -> float:
        steering: float = math.degrees(steering)  # [deg]
        steering: float = abs(steering)  # [deg]

        if 40.0 < steering <= Settings.MAX_STEERING:
            return 0.1

        if 35.0 < steering <= 40.0:
            return 0.15

        if 30.0 < steering <= 35.0:
            return 0.2

        if 25.0 < steering <= 30.0:
            return 0.25

        if 20.0 < steering <= 25.0:
            return 0.3

        if 15.0 < steering <= 20.0:
            return 0.35

        if 10.0 < steering <= 15.0:
            return 0.4

        if 5.0 < steering <= 10.0:
            return 0.45

        return Settings.MAX_SPEED

    def generatePoints(self, speed: float) -> int:
        return round((Settings.MAX_SPEED / speed) * random.randint(10, 40))
