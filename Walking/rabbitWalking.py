from datetime import date

class Rabbit:

    def __init__(self, name , species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = "Petting Area"
        self.walking = True
        self.shift = shift
        self.food = food
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
rogerRabbit = Rabbit("Roger", "Cartoon Rabbit", "midday", "carrots"  )
print(f'{rogerRabbit.name} is a {rogerRabbit.species}, and is at the zoo {rogerRabbit.shift}')

print(rogerRabbit)