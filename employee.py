import uuid
class Employee:
    def __init__(self, employee_name, employee_address):
        self.employee_id = str(uuid.uuid4())
        self.employee_name = employee_name
        self.employee_address = employee_address
        self.Taking_care_of_animals =[]

    def assignAnimal(self,animal_id):
        self.Taking_care_of_animals.append(animal_id) # assign animals to the list employee is taking care of

