from controllers.car.Settings import Settings
from controllers.car.Coordinate import Coordinate
from controllers.car.CoordinateTransformer import CoordinateTransformer


class InitService:
    def __init__(self, coordinateTransformer: CoordinateTransformer) -> None:
        self.coordinateTransformer = coordinateTransformer

    def init(self, course: list[Coordinate]) -> dict:
        if not course:
            return {}

        result: list[list[object]] = []
        course: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinate(coordinates=course)
        fragments: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments(coordinates=course)

        for fragment in fragments:
            result.append([{'x': c.x, 'y': c.y} for c in fragment])

        return {
            'length': Settings.LENGTH,
            'fragments': result,
        }
