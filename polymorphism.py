# Base class
class Creature:
    def transport(self):
        raise NotImplementedError("Subclasses must implement this method")

# Animal subclasses
class Canine(Creature):
    def transport(self):
        return "Running 🐕"

class Sparrow(Creature):
    def transport(self):
        return "Flying 🐦"

class Guppy(Creature):
    def transport(self):
        return "Swimming 🐟"

# Vehicle subclasses
class Sedan(Creature):
    def transport(self):
        return "Driving 🚗"

class Jet(Creature):
    def transport(self):
        return "Flying ✈️"

class Yacht(Creature):
    def transport(self):
        return "Sailing 🚤"

# Testing polymorphism
def test_creatures(creatures):
    for creature in creatures:
        print(f"{creature.__class__.__name__}: {creature.transport()}")

# Create a list of different creatures
creatures = [Canine(), Sparrow(), Guppy(), Sedan(), Jet(), Yacht()]

# Test the transport() method for each
test_creatures(creatures)
