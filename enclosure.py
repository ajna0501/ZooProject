import uuid
import datetime
class Enclosure:
    def __init__(self, enclosure_name, enclosure_area):
        self.enclosure_name = enclosure_name
        self.enclosure_area = enclosure_area
        self.enclosure_id = str(uuid.uuid4())
        self.clean_date = []
        self.enclosure_animals = []

    def clean(self):
        date = datetime.datetime.now()
        dt_string = date.strftime("%d/%m/%Y %H:%M:%S")
        self.clean_date.append(dt_string)

    def addAnimal(self,animal_id):
        self.enclosure_animals.append(animal_id)





