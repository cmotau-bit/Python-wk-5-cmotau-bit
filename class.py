# Base class for Wonder Woman
class WonderWoman:
    def __init__(self, name, origin, weapon, strength, compassion, mission):
        self.name = name
        self.origin = origin
        self.weapon = weapon
        self.__strength = strength  # Private attribute for strength (Encapsulation)
        self.compassion = compassion
        self.mission = mission

    def introduce(self):
        return f"I'm {self.name}, a warrior of {self.origin}. My weapon is the {self.weapon}, and my mission is to {self.mission}."

    def wield_weapon(self):
        return f"{self.name} wields the {self.weapon} with unmatched skill!"

    def get_strength(self):
        # Controlled access to the private strength attribute
        return f"{self.name}'s strength rating is {self.__strength}."

    def set_strength(self, new_value):
        if new_value > 0:
            self.__strength = new_value
        else:
            print("Strength must be a positive value!")

    def inspire(self):
        return f"{self.name} showcases compassion and justice, uplifting those she defends."

# Derived class for enhanced Hero Mode
class WonderWomanHeroMode(WonderWoman):
    def __init__(self, name, origin, weapon, strength, compassion, mission, armor, ability):
        super().__init__(name, origin, weapon, strength, compassion, mission)
        self.armor = armor
        self.ability = ability

    def wield_weapon(self):
        # Overriding the base class method
        return f"In Hero Mode, {self.name} uses her {self.weapon} and manifests her {self.ability}."

    def activate_armor(self):
        return f"{self.name} dons the {self.armor}, gaining superior protection in combat."

# Creating objects for interaction
base_wonder_woman = WonderWoman("Diana", "Themyscira", "Lasso of Truth", 95, "Infinite", "protect humanity")
hero_mode_diana = WonderWomanHeroMode("Diana", "Themyscira", "Lasso of Truth", 120, "Infinite", "safeguard peace", "Golden Eagle Armor", "Divine Strength")

# Sample interactions
print(base_wonder_woman.introduce())
print(base_wonder_woman.wield_weapon())
print(base_wonder_woman.inspire())
print(base_wonder_woman.get_strength())

base_wonder_woman.set_strength(100)
print(base_wonder_woman.get_strength())

print(hero_mode_diana.introduce())
print(hero_mode_diana.wield_weapon())
print(hero_mode_diana.activate_armor())
