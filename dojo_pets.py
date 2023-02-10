import ninja
import pets


# make a instance of Pet
pet_1 = pets.Pet("Molly", "dog", ["sit", "down", "shake", "stand"])
# make an instance of Ninja
ninja_1 = ninja.Ninja("Zach", "Carrera", "Freeze Dried Beef", "Kibble", pet_1)

# call methods on ninja_1
ninja_1.feed().walk().bathe()

# print out pet_1 info
print(pet_1.health, pet_1.energy)

# make an instance of Dog, a child class of Pet
dog_1 = pets.Dog("Juneau", "dog", ["sit"], "Alaskian Malamute", False)