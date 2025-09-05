import random
def modifier(value):
    return (value - 10)//2
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()

        # Hitpoints depend on constitution
        self.hitpoints = 10 + modifier(self.constitution)
    def ability(self):
            # Roll 4 dice, drop the lowest, sum the rest
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])

    
