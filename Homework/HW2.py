class Animals():
    def __init__(self, name, age, vax, purpose, benefits):
        self.name= name
        self.age= age
        self.vax= vax
        self.purpose= purpose
        self.benefits= benefits
    
    def get_info(self):
        print("Animal:" + self.name, "Age limit:" + self.age, "Vaccinated:" + self.vax, "Purpose:" + self.purpose, "Benefits:" + self.benefits)


class Cows(Animals):
    def __init__(self):
        super().__init__("Cow", "15-20 years" , "yes", "Milk, meat, leather", "dairy products, sustainable food source, fertilizes soil")

class Pigs(Animals):
    def __init__(self):
        super().__init__("Pig", "12-25 years", "yes", "Meat, leather", "Waste management, fertilizes soil, biodiverse")

class Chickens(Animals):
    def __init__(self):
        super().__init__("Chicken", "5-7 years", "yes", "Eggs, meat", "Insect control, soil fertilizer, sustainable food source")

class Goats(Animals):
    def __init__(self):
        super().__init__("Goat", "15-18 years", "yes", "Milk, meat, cashmere", "Reduce weed/overgrowth", "fertilizes soil")

class Sheeps(Animals):
    def __init__(self):
        super().__init__("Sheep", "10-12 years", "yes", "Milk, meat, wool", "Dairy products, wool for clothes")

class Farm():
    def __init__(self):
        self.animals=[]

    def add_animals(self,animal):
        self.animals.append(animal)
        print(animal.name + "has been added to the farm.")

    def remove_animals(self,animal):
        self.animals.remove(animal)
        print(animal.name + "has been removed from the farm.")  

farm= Farm()
while True:
    choice=0
    input(print("Choose 1-3 options, 1: Add animals, 2: Remove animals, 3: Print Existing Animals"))
    if choice== 1:
        print("Add an animal")
    elif choice== 2: 
        print("Remove an animal")
    elif choice== 3:
        print(Animals)  
    else:
        print("Invalid input, please try again")



