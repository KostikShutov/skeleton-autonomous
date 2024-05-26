#!/usr/bin/python

import os
import matplotlib
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from controllers.ControllerCreator import ControllerCreator
from controllers.InitControllerInterface import InitControllerInterface
from controllers.GeneratorControllerInterface import GeneratorControllerInterface
from helpers.Env import env

matplotlib.use('Agg')

app: Flask = Flask(__name__, template_folder=os.getcwd())
cors: CORS = CORS(app)
controllerCreator: ControllerCreator = ControllerCreator()
initController: InitControllerInterface = controllerCreator.createInit()
generatorController: GeneratorControllerInterface = controllerCreator.createGenerator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/openapi')
def openapi():
    return render_template('openapi.yaml')


@app.route('/init', methods=['POST'])
@cross_origin()
def init():
    data: dict = request.get_json(force=True, silent=True)

    return initController.init(data=data)


@app.route('/generate', methods=['POST'])
@cross_origin()
def generate():
    data: dict = request.get_json(force=True, silent=True)

    return generatorController.generate(data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(env['SERVER_PORT']))
