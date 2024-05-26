from controllers.InitControllerInterface import InitControllerInterface
from controllers.GeneratorControllerInterface import GeneratorControllerInterface
from controllers.TrainControllerInterface import TrainControllerInterface


class ControllerCreator:
    def createInit(self) -> InitControllerInterface:
        pass

    def createGenerator(self) -> GeneratorControllerInterface:
        pass

    def createTrain(self) -> TrainControllerInterface:
        pass
