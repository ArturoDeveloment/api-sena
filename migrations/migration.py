import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from models.conexion import Conexion 
from flask import Flask
import flask_migrate
import flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info_sena.db'
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

conexion = Conexion()

tabla = "prueba2"
columns =["id integer primary key autoincrement","name text", "description text"]
conexion.create_table(tabla, columns)

