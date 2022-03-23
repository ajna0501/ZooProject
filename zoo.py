class Zoo: 
    def __init__ (self): 
        self.animals = []
        self.zoo_enclosure = []
        self.zoo_employers = []

        
    def addAnimal(self, animal): 
        self.animals.append (animal) 
        
    def removeAnimal(self, animal): 
        self.animals.remove(animal) 
    
    def getAnimal(self, animal_id): 
        for animal in self.animals: 
            if animal.animal_id == animal_id: 
                return animal

    def addEnclosure(self,enclosure):
        self.zoo_enclosure.append(enclosure)

    def getEnclosure(self, enclosure_id):
        for x in self.zoo_enclosure:
            if x.enclosure_id == enclosure_id:
                return x

    def removeEnclosure(self,enclosure_id):
        self.zoo_enclosure.remove(enclosure_id)

    def addEmployeer(self,emp):
        self.zoo_employers.append(emp)

  
