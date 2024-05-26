from controllers.car.CoordinateParser import CoordinateParser
from controllers.car.Part import Part


class PartParser:
    def __init__(self, coordinateParser: CoordinateParser) -> None:
        self.coordinateParser = coordinateParser

    def parse(self, data: object) -> tuple[Part, str]:
        part: Part = Part(
            coordinates=self.coordinateParser.parse(data['coordinates']),
            yaw=float(data['yaw']),
        )

        return part, str(data['model'])
