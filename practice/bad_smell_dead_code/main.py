class Unit:
    def __init__(self, name: str):
        self.name = name

    def step_on(self, unit):
        pass

class Field:
    def set_unit(self, x, y, unit):
        pass

class Main:
    def __init__(self):
        self.field = Field()
        self.unit = GameItem(name="Unit")
        self.unit.step_on(unit=self.unit)

if __name__ == "__main__":
    main = Main()
