# load external packages
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# load libraries
from flask import Flask

# load packages
from middlewares.enviroment_load import EnviromentVariables

# instance the enviroment variables, it's having security in a class from package middlewares 
enviroments = EnviromentVariables()

app = Flask(__name__)

if __name__ == '__main__':
    app.run(**enviroments.data_server)