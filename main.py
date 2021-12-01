class MyDog:
    def __init__(self, breed, name, age, color, is_asleep=False):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color

    def walk(self):
        return print(self.name, "is walking")

dog = MyDog("labrador", "Zelda", 7, "Yellow")
dog.walk()