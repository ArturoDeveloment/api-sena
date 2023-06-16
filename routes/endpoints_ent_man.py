from flask import Blueprint
from controllers import controller_ent_man

endpoints_ent_man = Blueprint('endpoints_ent_man', __name__)

"""@endpoints_ent_man.get('/gestion-emprendimiento')
def entrepreneurship_management():
    return ent_man_controller.#"""