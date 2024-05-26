from car_scripts.strategies.ModelName import ModelName
from car_scripts.strategies.StaticSmoothlyStrategy import StaticSmoothlyStrategy
from car_scripts.strategies.StaticAggressiveStrategy import StaticAggressiveStrategy
from car_scripts.strategies.SpeedDynamicStrategy import SpeedDynamicStrategy
from car_scripts.strategies.SpeedSlowStrategy import SpeedSlowStrategy
from car_scripts.strategies.SpeedWeeklyStrategy import SpeedWeeklyStrategy
from car_scripts.strategies.StrategyInterface import StrategyInterface


class StrategyResolver:
    def resolve(self, modelName: ModelName) -> StrategyInterface:
        if modelName == ModelName.STATIC_SMOOTHLY:
            return StaticSmoothlyStrategy()

        if modelName == ModelName.STATIC_AGGRESSIVE:
            return StaticAggressiveStrategy()

        if modelName == ModelName.SPEED_DYNAMIC:
            return SpeedDynamicStrategy()

        if modelName == ModelName.SPEED_SLOW:
            return SpeedSlowStrategy()

        if modelName == ModelName.SPEED_WEEKLY:
            return SpeedWeeklyStrategy()

        raise NotImplementedError('Model not implemented')
