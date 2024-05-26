from controllers.TrainControllerInterface import TrainControllerInterface
from controllers.car.CommandTransformer import CommandTransformer
from controllers.car.CoordinateParser import CoordinateParser
from controllers.car.CoordinateTransformer import CoordinateTransformer
from controllers.car.PartTransformer import PartTransformer
from controllers.car.TrainService import TrainService
from controllers.car.TrainHelper import TrainHelper


class TrainController(TrainControllerInterface):
    def __init__(self):
        self.trainService = TrainService(
            coordinateParser=CoordinateParser(),
            trainHelper=TrainHelper(
                coordinateTransformer=CoordinateTransformer(),
                commandTransformer=CommandTransformer(),
                partTransformer=PartTransformer(),
            ),
        )

    def train(self, modelName: str) -> None:
        self.trainService.train(modelName)
