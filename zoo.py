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
    
    def getAnimal(self, animal_id): #to find animal with corresponding id
        for animal in self.animals: 
            if animal.animal_id == animal_id: 
                return animal

    def addEnclosure(self,enclosure):
        self.zoo_enclosure.append(enclosure) # appends enclosure to the list as obejct

    def getEnclosure(self, enclosure_id): #to take the object that has same eclosure id
        for e in self.zoo_enclosure:
            if e.enclosure_id == enclosure_id:
                return e

    def moveAnimaltoNewEnclosure(self, animals, new_home):
        for animal in animals:
            animal.AnimalHome(new_home.enclosure_id)
            new_home.addAnimal(animal) # gets all animals to the targeted enclosure


    def removeEnclosure(self,enclosure):
        animals = enclosure.enclosure_animals # gets the animal from enclosure
        self.zoo_enclosure.remove(enclosure) # removes that enclosurw from the lsit
        new_home = random.choice(self.zoo_enclosure)  # gets new enclosure home for animals from revious enclposure

        self.moveAnimaltoNewEnclosure(animals, new_home) #adds those animals to encllosure that is already existing



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
                number_of_animals = len(employee.Taking_care_of_animals) # gets number of animals from the list
                employers_num.append(number_of_animals) #append to list

            min_animal = min(employers_num) #find minimum
            max_animal = max(employers_num) #finds mac
            avg_animal = (sum(employers_num)/len(employers_num)) #average
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
        new_caretaker = random.choice(self.zoo_employers)

        self.moveAnimal(animals,new_caretaker)



    def cleaningPlan(self):
        for enclosure in self.zoo_enclosure:
            if len(enclosure.clean_date) == 0:
                self.cleaning_plan[enclosure.enclosure_id] = "No cleaning recorded, clean it now" # if there is not cleaning record
            else:
                last_cleaned = enclosure.clean_date[-1]
                next_plan = last_cleaned+datetime.timedelta(days=3) #adds next date 3 days after last one
                next_plan = f"{next_plan.day} / {next_plan.month}/ {next_plan.year} "
                self.cleaning_plan[enclosure.enclosure_id] = next_plan



    def medicalCheckUp(self):
        for medical in self.animals:
            if len(medical.medical_checkup) == 0 :
                self.medical_plan[medical.animal_id] = "No medical Check-up recorded, to the chekup now"
            else:
                last_checkup = medical.medical_checkup[-1]
                next_checkup = last_checkup + datetime.timedelta(days = 35)#adds next date 35 days after last one
                next_checkup = f"{next_checkup.day}/{next_checkup.month} /{next_checkup.year}   "
                self.medical_plan[medical.animal_id] = next_checkup

    def feedingPlan(self):
        for feeding in self.animals:
            if len(feeding.feeding_record ) == 0:
                self.feeding[feeding.animal_id] = "No feeding recorded, feed animal now"
            else:
                last_feeding = feeding.feeding_record[-1]
                next_feeding = last_feeding + datetime.timedelta(days = 2)#adds next date 2 days after last one
                next_feeding = f" {next_feeding.day}/ {next_feeding.month} /{next_feeding.year}  "
                self.feeding[feeding.animal_id] = next_feeding



    def animalsPerSpeciesStats(self):# aniam,l per speices
        dict = {}
        try:

            for animal in self.animals:
                if animal.species_name in dict.keys():
                    dict[animal.species_name] += 1
                else:
                    dict[animal.species_name] = 1

            return dict
        except:
            return None #return none if its empty not to have error


    def animalsPerEnclosureStats(self):
        try:
            return len(self.zoo_enclosure) / len(self.animals) # total numbers of animals per enclosure
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






  
