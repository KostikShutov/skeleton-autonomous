from controllers.GeneratorControllerInterface import GeneratorControllerInterface
from controllers.car.PartParser import PartParser
from controllers.car.CoordinateParser import CoordinateParser
from controllers.car.GeneratorService import GeneratorService
from controllers.car.PartTransformer import PartTransformer
from controllers.car.CoordinateTransformer import CoordinateTransformer


class GeneratorController(GeneratorControllerInterface):
    def __init__(self):
        self.partParser = PartParser(
            coordinateParser=CoordinateParser(),
        )

        self.generatorService = GeneratorService(
            partTransformer=PartTransformer(),
            coordinateTransformer=CoordinateTransformer(),
        )

    def generate(self, data: dict) -> dict:
        part, modelName = self.partParser.parse(data=data)

        return self.generatorService.predict(part=part, modelName=modelName)
