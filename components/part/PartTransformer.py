import math
from components.coordinate.Coordinate import Coordinate
from components.part.Part import Part
from helpers.Utility import removeFirst
from helpers.Math import rotatePoints, normalizeAngle


class PartTransformer:
    def presentForInput(self, part: Part) -> list[float]:
        coordinates: list[Coordinate] = part.coordinates

        if len(coordinates) == 0:
            raise ValueError('Must provide >= 1 coordinates')

        if coordinates[0].y != 0.0:
            raise ValueError('First y coordinate must be 0')

        return [
            coordinates[0].x,
            part.yaw,
        ]

    def normalizeToZero(self, part: Part) -> Part:
        coordinates: list[Coordinate] = part.coordinates

        if len(coordinates) <= 1:
            raise ValueError('Must provide >= 2 coordinates')

        first: Coordinate = part.coordinates[0]
        normalized: list[Coordinate] = []

        for coordinate in coordinates:
            normalized.append(Coordinate(
                x=coordinate.x - first.x,
                y=coordinate.y - first.y,
            ))

        normalized, deltaAngle = rotatePoints(normalized)

        return Part(
            coordinates=removeFirst(normalized),
            yaw=math.degrees(normalizeAngle(math.radians(part.yaw + deltaAngle)))
        )
