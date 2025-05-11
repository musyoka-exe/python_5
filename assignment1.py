# Base class
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self._power = power  
        self.health = health

    def display_info(self):
        print(f"Name: {self.name}, Power: {self._power}, Health: {self.health}")

    def attack(self):
        print(f"{self.name} attacks with {self._power}!")

# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def attack(self):
        print(f"{self.name} swoops down at {self.flight_speed} mph and attacks with {self._power}!")

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph!")

# Creating objects
hero1 = Superhero("ThunderMan", "Lightning", 100)
hero2 = FlyingSuperhero("SkyWing", "Wind Blast", 120, 300)

hero1.display_info()
hero1.attack()

print()

hero2.display_info()
hero2.attack()
hero2.fly()
