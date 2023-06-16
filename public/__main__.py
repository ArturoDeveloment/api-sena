# load external packages
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# load libraries
from flask import Flask

# load packages
from middlewares.enviroment_load import EnviromentVariables

# load routes
from routes.endpoints_area import endpoints_area
from routes.endpoints_welfare import endpoints_welfare
from routes.endpoints_ent_man import endpoints_ent_man

# instance the enviroment variables, it's having security in a class from package middlewares 
enviroments = EnviromentVariables()

namespace = '/inicio'

app = Flask(__name__)

app.register_blueprint(endpoints_area, url_prefix=f'{namespace}')

app.register_blueprint(endpoints_welfare, url_prefix=f'{namespace}')

app.register_blueprint(endpoints_ent_man, url_prefix=f'{namespace}')

if __name__ == '__main__':
    app.run(**enviroments.data_server)