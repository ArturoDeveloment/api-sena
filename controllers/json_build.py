import json

class BuiltinContext:
    def __init__(self) -> None:
        self.__json = None
        self.__reset_json()

    def __reset_json(self):
        self.__json = {}
    
    @staticmethod
    def areas()-> dict:
        pass
    
    @staticmethod
    def apprentice_welfare()-> dict:
        pass
    
    @staticmethod
    def entrepreneurship_management()-> dict:
        pass
    
    @property
    def json(self):
        return self.__json
    
    @json.setter
    def json(self, data: dict = None):
        self.__json[0].update(data) if data != None else None
    
    def convert_json(self):
        json_dump = json.dumps(self.json)
        return json_dump