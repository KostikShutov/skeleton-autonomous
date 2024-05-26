#!/usr/bin/python

import os
from controllers.ControllerCreator import ControllerCreator
from helpers.Utility import parseArgs


def main() -> None:
    args: any = parseArgs()
    modelName: str = args.model

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model name: ' + modelName)

    ControllerCreator().createTrain().train(modelName=modelName)


if __name__ == '__main__':
    main()
