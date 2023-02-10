class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 40
        self.energy = 40

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print("WOOOOF")
        return self


class Dog(Pet):
    def __init__(self, name, pet_type, tricks, breed, is_hypoallergenic):
        super().__init__(name, pet_type, tricks)
        self.breed = breed
        self.is_hypoallergenic = is_hypoallergenic
    
