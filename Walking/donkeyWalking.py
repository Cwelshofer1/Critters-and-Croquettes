from datetime import date

class Donkey:

    def __init__(self, name , species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = "Petting Area"
        self.walking = True
        self.shift = shift
        
    def __str__(self):
        return f"{self.name} is a {self.species}"