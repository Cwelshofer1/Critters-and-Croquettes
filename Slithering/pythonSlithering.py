from datetime import date

class Python:

    def __init__(self, name , species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = "Glass Tank"
        self.slithering = True
        
    def __str__(self):
        return f"{self.name} is a {self.species}"
