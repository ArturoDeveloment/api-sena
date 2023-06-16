from flask import jsonify
from models.queries import RequestDataBase

def list_areas():
    try:
        rq = RequestDataBase()
        data = rq.show_registers('formation_areas', ['id', 'name', 'description'], {'status': 'active'})
        #data_r = [row[0] for row in data]
        x = []
        print(data)   
        for i in range(len(data)):
            y = {
                'id': data[i][0],
                'name': data[i][1],
                'description': data[i][2]
            }
            x.append(y)

        return {'areas': x , 'message': 'Areas listing successful!'}
    except Exception as ex:
        return {'message': 'Error - Areas listing unsuccessful!'}
    
def search_area_id(area_id):
    try:
        rq = RequestDataBase()
        rs = rq.show_registers('formation_areas', ['*'], {'id': area_id})
        if len(rs) > 0:
            return True
        else:
            return False
    except Exception as ex:
        return False
    
def get_area_information(area_id):
    try:
        rq = RequestDataBase()
        data = rq.show_registers('formation_areas', ['id', 'area_name', 'description'], {'id': area_id})
        return {'area': data , 'message': 'Areas listing successful!'}
    except Exception as ex:
        return {'message': 'Error - Areas describing unsuccessful!'}