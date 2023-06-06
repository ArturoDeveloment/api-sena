class Areas:
    columns = {
        'name': None,
        'description': None,
        'levels': None,
        'aditional_info': None
    }
    
    def __init__(self) -> None:
        self.__table = Areas.__name__

    def created_area(self, colums_values: list):
        colums_values = zip(self.columns.keys(), colums_values)
        self.columns.update(colums_values)
    
