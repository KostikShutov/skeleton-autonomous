from controllers.InitControllerInterface import InitControllerInterface
from controllers.car.Coordinate import Coordinate
from controllers.car.CoordinateParser import CoordinateParser
from controllers.car.CoordinateTransformer import CoordinateTransformer
from controllers.car.InitService import InitService


class InitController(InitControllerInterface):
    def __init__(self):
        self.coordinateParser = CoordinateParser()

        self.initService = InitService(
            coordinateTransformer=CoordinateTransformer(),
        )

    def init(self, data: dict) -> dict:
        course: list[Coordinate] = self.coordinateParser.parse(data=data)

        return self.initService.init(course=course)
