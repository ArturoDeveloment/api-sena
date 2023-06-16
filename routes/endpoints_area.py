from flask import Blueprint, jsonify
from controllers import controller_areas

endpoints_area = Blueprint('endpoints_area', __name__)

routes = [
    'construccion',
    'automatizacion',
    'teleinformatica',
    'fabricacion-mecanica',
    'confecciones',
    'soldadura',
    'electricidad',
    'automotriz'
]

@endpoints_area.get('/areas')
def areas():
    return jsonify(controller_areas.list_areas())

@endpoints_area.get('/areas/<int:id>')
def area(id):
    areas = controller_areas.list_areas()
    if controller_areas.search_area_id(id):
        return jsonify(controller_areas.get_area_information(id))
    else:
        return jsonify({'message': 'Error - The area does not exists'})