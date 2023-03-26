class Warrior:
    def attack(self):
        print('Warrior attacks')

    def defense(self):
        print('Warrior defends')

    def move(self):
        print('Warrior moves')

class Healer:
    def attack(self):
        pass

    def defense(self):
        print('Healer defends')

    def move(self):
        print('Healer flees')

    def healer_defense(self):
        print('Healer can defend as well')

    def healer_move(self):
        print('Healer can move faster')

    def heal(self):
        print('Healer heals')


class Tree:
    def attack(self):
        pass

    def defense(self):
        print('Tree defends')

    def move(self):
        pass

    def tree_defense(self):
        print('Tree can defend even better')

    def on_fire(self):
        print('Tree is on fire')


class Trap:
    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass

    def trap_attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()