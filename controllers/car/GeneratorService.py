import pickle
import tensorflow as tf
from tf_keras.models import model_from_json, Sequential
from sklearn.preprocessing import MinMaxScaler
from controllers.car.Config import Config
from controllers.car.CoordinateTransformer import CoordinateTransformer
from controllers.car.Command import Command
from controllers.car.Part import Part
from controllers.car.PartTransformer import PartTransformer


class GeneratorService:
    def __init__(self, partTransformer: PartTransformer,
                 coordinateTransformer: CoordinateTransformer) -> None:
        self.partTransformer = partTransformer
        self.coordinateTransformer = coordinateTransformer

    def predict(self, part: Part, modelName: str) -> dict:
        modelDirectory: str = 'models/' + modelName + '/'
        command: Command = self.__getCommand(part, modelDirectory)

        return {
            'steering': command.steering,
            'speed': command.speed,
        }

    def __getCommand(self, part: Part, modelDirectory: str) -> Command:
        steering: float = self.__doPredict(part, modelDirectory + 'steering/')
        speed: float = self.__doPredict(part, modelDirectory + 'speed/')

        return Command(
            steering=max(Config.MIN_STEERING, min(Config.MAX_STEERING, steering)),
            speed=max(Config.MIN_SPEED, min(speed, Config.MAX_SPEED)),
        )

    def __doPredict(self, part: Part, modelDirectory: str) -> float:
        part: Part = self.partTransformer.normalizeToZero(Part(
            coordinates=part.coordinates,
            yaw=part.yaw,
        ))

        with open(modelDirectory + 'x_scaler.pickle', 'rb') as file:
            xScaler: MinMaxScaler = pickle.load(file)

        inputX: list[float] = self.partTransformer.presentForInput(part)
        inputX: list[float] = xScaler.transform([inputX])[0]

        with open(modelDirectory + 'y_scaler.pickle', 'rb') as file:
            yScaler: MinMaxScaler = pickle.load(file)

        prediction: any = self.__loadModel(modelDirectory).predict(tf.expand_dims(inputX, axis=0))
        command: list[float] = prediction[0].tolist()
        command: list[float] = yScaler.inverse_transform([command])[0]

        return command[0]

    def __loadModel(self, modelDirectory: str) -> Sequential:
        with open(modelDirectory + 'model.json', 'r') as file:
            json: str = file.read()

        model: Sequential = model_from_json(json)
        model.load_weights(modelDirectory + 'model.h5')

        return model
