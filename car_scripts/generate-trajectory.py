import os
import math
import json
from tqdm import tqdm
from controllers.car.Settings import Settings
from components.model.ModelName import ModelName
from controllers.car.StrategyInterface import StrategyInterface
from controllers.car.StrategyResolver import StrategyResolver
from controllers.car.Math import normalizeAngle
from helpers.Utility import createDirectory, parseArgs


def generateTrajectory(strategy: StrategyInterface, number: int) -> list[object]:
    x: float = 0.0  # [m]
    y: float = 0.0  # [m]
    duration: float = 0.1  # [s]
    yaw: float = math.radians(0.0)  # [rad]
    steering: float = strategy.generateSteering()  # [rad]
    speed: float = strategy.generateSpeed(steering=steering)  # [m/s]
    points: int = strategy.generatePoints(speed=speed)
    result: list[object] = [{
        'x': x,
        'y': y,
        'yaw': math.degrees(yaw),
        'steering': math.degrees(steering),
        'speed': speed,
    }]

    for _ in tqdm(range(number), desc='Generating trajectory'):
        for _ in range(points):
            x += speed * math.cos(yaw) * duration  # [m]
            y += speed * math.sin(yaw) * duration  # [m]
            yaw += math.tan(steering) * (speed / Settings.LENGTH) * duration  # [rad]
            yaw: float = normalizeAngle(yaw)  # [rad]

        x, y = strategy.modifyCoordinate(x=x, y=y, yaw=yaw, speed=speed, duration=duration)
        steering: float = strategy.generateSteering()  # [rad]
        speed: float = strategy.generateSpeed(steering=steering)  # [m/s]
        points: int = strategy.generatePoints(speed=speed)

        result.append({
            'x': x,
            'y': y,
            'yaw': math.degrees(yaw),
            'steering': math.degrees(steering),
            'speed': speed,
        })

    return result


def saveTrajectory(path: str, trajectory: list[object]) -> None:
    with open(path, 'w') as file:
        file.write(json.dumps(trajectory))
        file.write('\n')


def main() -> None:
    args: any = parseArgs()
    number: int = args.number
    modelName: str = args.model
    modelDirectory: str = 'models/' + modelName + '/'
    modelFile: str = modelDirectory + args.file + '.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)
    print('Number: ' + str(number))

    strategy: StrategyInterface = StrategyResolver().resolve(modelName=ModelName(modelName))
    trajectory: list[object] = generateTrajectory(strategy=strategy, number=number)
    createDirectory(directory=modelDirectory)
    saveTrajectory(path=modelFile, trajectory=trajectory)


if __name__ == '__main__':
    main()
