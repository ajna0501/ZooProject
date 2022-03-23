from flask import Flask, jsonify
from flask_restx import Api, reqparse, Resource
from zoo_json_utils import ZooJsonEncoder
from zoo import Zoo
from animal import Animal
from enclosure import Enclosure
my_zoo = Zoo()

zooma_app = Flask(__name__)
# need to extend this class for custom objects, so that they can be jsonified
zooma_app.json_encoder = ZooJsonEncoder 
zooma_api = Api(zooma_app)

animal_parser = reqparse.RequestParser()
animal_parser.add_argument('species', type=str, required=True, help='The scientific name of the animal, e,g. Panthera tigris')
animal_parser.add_argument('name', type=str, required=True, help='The common name of the animal, e.g., Tiger')
animal_parser.add_argument('age', type=int, required=True, help='The age of the animal, e.g., 12')

animal_enclosure = reqparse.RequestParser()
animal_enclosure.add_argument ('enclosure_id', type=str, required=True, help='The id of animals enclosure')

animal_mother = reqparse.RequestParser()
animal_mother.add_argument('mother_id', type=str, required=True, help='Input animals ID when it gives birth')

animal_death = reqparse.RequestParser()
animal_death.add_argument('animal_id', type=str, required=True, help='Input animals ID that died')

enclosure_zoo = reqparse.RequestParser()
enclosure_zoo.add_argument('name', type=str, required=True, help='Name of enclosure')
enclosure_zoo.add_argument('area', type=int, required=True, help='Area of enclosure')


@zooma_api.route('/animal')
class AddAnimalAPI(Resource):
    @zooma_api.doc(parser=animal_parser)
    def post(self):
        # get the post parameters 
        args = animal_parser.parse_args()
        name = args['name']
        species = args['species']
        age = args['age']
        # create a new animal object 
        new_animal = Animal (species, name, age) 
        #add the animal to the zoo
        my_zoo.addAnimal (new_animal) 
        return jsonify(new_animal) 
    

@zooma_api.route('/animal/<animal_id>')
class Animal_ID(Resource):
     def get(self, animal_id):
        search_result  = my_zoo.getAnimal(animal_id)
        return search_result # this is automatically jsonified by flask-restx
    
     def delete(self, animal_id):
        targeted_animal  = my_zoo.getAnimal(animal_id)
        if not targeted_animal: 
            return jsonify(f"Animal with ID {animal_id} was not found")
        my_zoo.removeAnimal(targeted_animal)
        return jsonify(f"Animal with ID {animal_id} was removed")

@zooma_api.route('/animals')
class AllAnimals(Resource):
     def get(self):
        return jsonify( my_zoo.animals)  
    
     
@zooma_api.route('/animals/<animal_id>/feed')
class FeedAnimal(Resource):
     def post(self, animal_id):
        targeted_animal  = my_zoo.getAnimal(animal_id)
        if not targeted_animal: 
            return jsonify(f"Animal with ID {animal_id} was not found")
        targeted_animal.feed()
        return jsonify(targeted_animal)

@zooma_api.route('/animal/<animal_id>/vet')
class AnimalVet(Resource):
    def post(self, animal_id):
        targeted_animal = my_zoo.getAnimal(animal_id)
        if not targeted_animal:
            return jsonify(f"Animal with ID {animal_id} was not found")
        targeted_animal.vet()
        return jsonify(targeted_animal)

@zooma_api.route('/animal/<animal_id>/home ')
class Home(Resource):
    @zooma_api.doc(parser=animal_enclosure)
    def post(self, animal_id):
        targeted_animal = my_zoo.getAnimal(animal_id)
        if not targeted_animal:
            return jsonify(f"Animal with ID {animal_id} was not found")
        args = animal_enclosure.parse_args() #get the paramter of parser animla enclosrue
        enclosure = args["enclosure_id"] #gets the id of enclosure
        home = my_zoo.getEnclosure(enclosure) # exsiting enlcosre in zooo
        targeted_animal.AnimalHome(enclosure) #add encllsure ID to animal
        #also add animal to enclosure class
        home.addAnimal(targeted_animal)
        if not home:
            return jsonify(f"Enclosurw with ID {enclosure} was not found")
        return jsonify(targeted_animal)


@zooma_api.route('/animal/birth/ ')
class Birth(Resource):
    @zooma_api.doc(parser=animal_mother)
    def post(self):
        args = animal_mother.parse_args() # to get mother parameter
        motherId = args["mother_id"] #get mother id
        mother = my_zoo.getAnimal(motherId) #gets you the animal
        if not mother:
            return jsonify( f"This id animal {motherId} is not a mother")
        newborn = mother.birth()
        my_zoo.addAnimal(newborn)
        return jsonify(newborn)


@zooma_api.route('/animal/death/ ')
class Death(Resource):
    @zooma_api.doc(parser=animal_death)
    def post(self):
        args = animal_death.parse_args() # to get animal_id
        animal_id = args["animal_id"] #get animal id
        death = my_zoo.getAnimal(animal_id) #gets you the animal
        if not death:
            return jsonify( f"This id animal {animal_id} was not found")
        my_zoo.removeAnimal(death)

        return jsonify(f"This animal {animal_id} died and was removed from system")

@zooma_api.route('/enclosure')
class Enclosure_in_zoo(Resource):
    @zooma_api.doc(parser=enclosure_zoo)
    def post(self):
        args = enclosure_zoo.parse_args()# get the agument
        enclosure_name = args ["name"]
        enclosure_area = args ["area"]
        add_enclosure = Enclosure(enclosure_name,enclosure_area)
        my_zoo.addEnclosure(add_enclosure)
        return jsonify(add_enclosure)

@zooma_api.route('/enclosures')
class Get_Enclosures(Resource):
    def get(self):
        all_enclosures = my_zoo.zoo_enclosure
        return jsonify(all_enclosures)

@zooma_api.route('/enclosures/<enclosure_id>/clean')
class Clean_Enclosure(Resource):
    def post(self, enclosure_id):
        targeted_enclosure = my_zoo.getEnclosure(enclosure_id)
        if not targeted_enclosure:
            return jsonify(f"Enclosure with ID {enclosure_id} was not found")

        targeted_enclosure.clean()
        return jsonify(targeted_enclosure)

@zooma_api.route('/enclosures/<enclosure_id>/animals')
class Get_animals(Resource):
    def get(self,enclosure_id):
        targeted_enclosure = my_zoo.getEnclosure(enclosure_id)
        if not targeted_enclosure:
            return jsonify(f"Enclosure with ID {enclosure_id} was not found")

        return jsonify(targeted_enclosure.enclosure_animals)

@zooma_api.route('/enclosure/<enclosure_id> ')
class Delete_Animals(Resource):
    def delete(self,enclosure_id):
        targeted_enclosure = my_zoo.getEnclosure(enclosure_id)
        if not targeted_enclosure:
            return jsonify(f"Enclosure with ID {enclosure_id} was not found")
        animals = targeted_enclosure.enclosure_animals
        #Continue this realize how to tranfer to another enclosure and then delete this one












    
if __name__ == '__main__':
    zooma_app.run(debug = False, port = 7890)
