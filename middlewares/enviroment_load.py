from dotenv import load_dotenv
import os

class EnviromentVariables:
    load_dotenv()
    def __init__(self) -> None:
        self.__data_server = {
            'host': os.getenv('HOST'),
            'port': os.getenv('PORT'),
            'debug': os.getenv('DEBUG')
        }
        
    @property
    def data_server(self):
        return self.__data_server