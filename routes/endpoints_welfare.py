from flask import Blueprint
from controllers import controller_welfare

endpoints_welfare = Blueprint('endpoints_welfare', __name__)

"""@endpoints_welfare.get('/bienestar')
def welfare():
    return welfare_controller.#"""