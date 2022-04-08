import uuid 
import datetime 
class Animal: 
    def __init__ (self, species_name, common_name, age): 
        self.animal_id = str(uuid.uuid4())
        self.species_name = species_name 
        self.common_name = common_name 
        self.age = age 
        self.feeding_record = [] 
        self.enclosure = None 
        self.care_taker = None
        self.medical_checkup = []

        # add more as required here 
        
    # simply store the current system time when this method is called    
    def feed(self):
        date = datetime.datetime.now()
        self.feeding_record.append(date)

    def vet(self):
        date = datetime.datetime.now()
        self.medical_checkup.append(date)


    def AnimalHome(self, enclosure):
        self.enclosure = enclosure # sets animals enclosure to targeted one

    def birth(self):
        child = Animal(self.species_name, self.common_name, 0)
        child.AnimalHome(self.enclosure)
        return child

    def assignCaretaker(self,employee_id):
        self.care_taker = employee_id
            # changes care taker from noen to employes object: