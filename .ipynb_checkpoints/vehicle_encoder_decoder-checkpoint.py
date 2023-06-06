#Vehicle data encoder/decoder
import json

class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass
        
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, d):
        return Vehicle(**d)

class MyEncoder(json.JSONEncoder):
    def default(self, w):
        if isinstance(w, Vehicle):
            return w.__dict__
        else:
            return super().default(self)
        
def create_car_with_input():
    #Collect input from the user
    registration_number = input('Registration number:')
    year_of_production = int(input('Year of production:'))
    passenger = bool(input('Passenger [True/False]:'))
    mass = float(input('Vehicle mass:'))
    
    #Create a new Python object/class instance
    new_car = Vehicle(registration_number, year_of_production, passenger, mass)
    return new_car

#Code for implementation
def vehicle_encoder_decoder():
    print('What can I do for you? \n 1 - Produce a JSON string describing a vehicle \n 2 - Decode a JSON string into vehicle data')
    response = input()

    try:
        response = int(response)
    except ValueError:
        print('Choice made is not an integer')
        return

    print(F'Your choice:{response}')

    if response == 1:
        new_car = create_car_with_input()

        #Create a JSON string from this object
        json_str = json.dumps(new_car, cls=MyEncoder)
        print('The resulting JSON string is:')
        print(json_str)

    elif response == 2:
        json_str = input('Enter vehicle JSON string:')

        new_car = json.loads(json_str, cls=MyDecoder)
        print(new_car.__dict__)

    else:
        print('This choice was none of the options given')
        return

    print('Done')
    return

#Run
vehicle_encoder_decoder()