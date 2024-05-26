from controllers.car.Command import Command


class CommandTransformer:
    def presentForOutput(self, command: Command) -> list[float]:
        return [command.steering, command.speed]
