from actors import Creature, Wizard
import random
import time


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------------------------')
    print('                 WIZZARD GAME APP')
    print('--------------------------------------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The Wizard returns revitalized.")

        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:')
            for creature in creatures:
                print(creature)
        else:
            print('OK, exiting the game...')
            break


if __name__ == '__main__':
    main()
