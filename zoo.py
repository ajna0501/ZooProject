import datetime


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


    def removeEnclosure(self,enclosure):
        self.zoo_enclosure.remove(enclosure)

    def addEmployeer(self,emp):
        self.zoo_employers.append(emp)

    def getEmployee(self,employee_id):
        for caretaker in self.zoo_employers:
            if caretaker.employee_id == employee_id:
                return caretaker

    def employee_stats(self):
        employers_num = []
        for employee in self.zoo_employers:
            number_of_animals = len(employee.Taking_care_of_animals)
            employers_num.append(number_of_animals)

        min_animal = min(employers_num)
        max_animal = max(employers_num)
        avg_animal = (sum(employers_num)/len(employers_num))
        return {"Minimum": min_animal, "Maximum": max_animal, "Average": avg_animal}

    def removeEmployee(self,employee):
        self.zoo_employers.remove(employee)

    def cleaningPlan(self):
        for enclosure in self.zoo_enclosure:
            last_cleaned = enclosure.clean_date[-1]
            next_plan = last_cleaned+datetime.timedelta(days=3)
            next_plan = f"{next_plan.year} / {next_plan.month}/ {next_plan.date}"
            self.cleaning_plan[enclosure.enclosure_id] = next_plan

        return self.cleaning_plan

    def medicalCheckUp(self):
        for medical in self.animals:
            last_checkup = medical.medical_checkup[-1]
            next_checkup = last_checkup + datetime.timedelta(days = 35)
            next_checkup = f"{next_checkup.year} / {next.plan.month} / {next_checkup.date}"
            self.medical_plan[medical.animal_id] = next_checkup

        return self.medical_plan

    def feedingPlan(self):
        for feeding in self.animals:
            last_feeding = feeding.feeding_record [-1]
            next_feeding = last_feeding + datetime.timedelta(days = 2)
            next_feeding = f" {next_feeding.year} / {next_feeding.month} / {next_feeding.date}"
            self.feeding[feeding.animal_id] = next_feeding

        return self.feeding








  
