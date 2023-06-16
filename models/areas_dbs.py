class Areas:
    __columns = {
        'name': None,
        'description': None,
        'levels': None,
        'aditional_info': None
    }
    
    def __init__(self) -> None:
        self.__table = Areas.__name__

    def created_area(self, columns_values: list):
        columns_values = zip(self.__columns.keys(), columns_values)
        print(columns_values)
        columns = self.__columns.copy()
        columns.update(columns_values)
        return columns
    
    #def list_areas(self, data: dict):

    


areas = Areas()
creacion = areas.created_area(
    [
        'construcción', 'dwnqiudbniubdw', 'técnico', 'fibqugfeu'
    ]
)

print(creacion) 
