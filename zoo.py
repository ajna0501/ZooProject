import datetime
import random


class Zoo:
    def __init__ (self): 
        self.animals = []
        self.zoo_enclosure = []
        self.zoo_employers = []
        self.cleaning_plan ={}
        self.medical_plan = {}
        self.feeding = {}

        
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
        for e in self.zoo_enclosure:
            if e.enclosure_id == enclosure_id:
                return e

    def moveAnimaltoNewEnclosure(self, animals, new_home):
        for animal in animals:
            animal.AnimalHome(new_home.enclosure_id)
            new_home.addAnimal(animal)


    def removeEnclosure(self,enclosure):
        animals = enclosure.enclosure_animals
        self.zoo_enclosure.remove(enclosure)
        new_home = random.choice.zoo_enclosure

        self.moveAnimaltoNewEnclosure(animals,new_home)



    def addEmployeer(self,emp):
        self.zoo_employers.append(emp)

    def getEmployee(self,employee_id):
        for caretaker in self.zoo_employers:
            if caretaker.employee_id == employee_id:
                return caretaker

    def employee_stats(self):
        employers_num = []
        try:
            for employee in self.zoo_employers:
                number_of_animals = len(employee.Taking_care_of_animals)
                employers_num.append(number_of_animals)

            min_animal = min(employers_num)
            max_animal = max(employers_num)
            avg_animal = (sum(employers_num)/len(employers_num))
            return {"Minimum": min_animal, "Maximum": max_animal, "Average": avg_animal}
        except:
            None

    def moveAnimal(self,animals,caretaker):
        for animal in animals:
            animal.assignCaretaker(caretaker.employee_id)
            caretaker.assignAnimal(animal)

    def removeEmployee(self,employee):
        animals = employee.Taking_care_of_animals
        self.zoo_employers.remove(employee)
        new_caretaker = random.choice.zoo_employers

        self.moveAnimal(animals,new_caretaker)



    def cleaningPlan(self):
        for enclosure in self.zoo_enclosure:
            last_cleaned = enclosure.clean_date[-1]
            next_plan = last_cleaned+datetime.timedelta(days=3)
            next_plan = f"{next_plan.day} / {next_plan.month}/ {next_plan.year} "
            self.cleaning_plan[enclosure.enclosure_id] = next_plan



    def medicalCheckUp(self):
        for medical in self.animals:
            last_checkup = medical.medical_checkup[-1]
            next_checkup = last_checkup + datetime.timedelta(days = 35)
            next_checkup = f"{next_checkup.day}/{next_checkup.month} /{next_checkup.year}   "
            self.medical_plan[medical.animal_id] = next_checkup

    def feedingPlan(self):
        for feeding in self.animals:
            last_feeding = feeding.feeding_record[-1]
            next_feeding = last_feeding + datetime.timedelta(days = 2)
            next_feeding = f" {next_feeding.day}/ {next_feeding.month} /{next_feeding.year}  "
            self.feeding[feeding.animal_id] = next_feeding



    def animalsPerSpeciesStats(self):
        dict = {}
        try:

            for animal in self.animals:
                if animal.species_name in dict.keys():
                    dict[animal.species_name] += 1
                else:
                    dict[animal.species_name] = 1

            return dict
        except:
            return None


    def animalsPerEnclosureStats(self):
        try:
            return len(self.zoo_enclosure) / len(self.animals)
        except:
            return None

    def numEnclosureMultipleSpecies(self):
        count = 0
        try:
            for enclosure in self.zoo_enclosure:
                if not enclosure:
                    count +=1
            return count
        except:
            return None

    def availableSpace(self):
        dict = {}
        try:
            for enclosure in self.zoo_enclosure:
                dict[enclosure.enclosure_id] = len(enclosure.enclosure_animals) / enclosure.enclosure_area
            return dict
        except:
            return None






  
