import random
from datetime import datetime

class Note:
    
    def __init__(self, title, body):
        self.__id = random.randint(123456,999999)
        time_create = datetime.now()
        self.__time_create = f"{time_create.day}.{time_create.month}.{time_create.year}" 
        self.__title = title
        self.__body = body

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

