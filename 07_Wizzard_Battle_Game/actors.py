import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature: {} of level {}'.format(self.name, self.level)



class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizzard {} attacks {}!'
              .format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You roll {}...'.format(my_roll))
        print('{} roll {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("the wizard has handily triuphed over {}"
                  .format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!")
            return False
