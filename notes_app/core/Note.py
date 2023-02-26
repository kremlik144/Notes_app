import random
from datetime import datetime

class Note:
    
    def __init__(self, title, body):
        self.id = random.randint(123456,999999)
        time_create = datetime.now()
        self.time_create = f"{time_create.day}.{time_create.month}.{time_create.year}" 
        self.title = title
        self.body = body
