from datetime import date

class Rabbit:

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
        
rogerRabbit = Rabbit("Roger", "Cartoon Rabbit", "midday" )
print(f'{rogerRabbit.name} is a {rogerRabbit.species}, and is at the zoo {rogerRabbit.shift}')

print(rogerRabbit)