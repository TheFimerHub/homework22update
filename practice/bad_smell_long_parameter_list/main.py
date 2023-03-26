class Unit:
    def __init__(self, speed=1, is_fly=False, crawl=False):
        self.speed = speed
        self.is_fly = is_fly
        self.crawl = crawl

    def get_speed(self):
        if self.is_fly:
            return self.speed * 1.2
        elif self.crawl:
            return self.speed * 0.5
        else:
            return self.speed

    def move(self, field, x, y, direction):
        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        speed = self.get_speed()
        if direction == 'UP':
            new_y = y + speed
            new_x = x
        elif direction == 'DOWN':
            new_y = y - speed
            new_x = x
        elif direction == 'LEFT':
            new_y = y
            new_x = x - speed
        elif direction == 'RIGHT':
            new_y = y
            new_x = x + speed

        field.set_unit(x=new_x, y=new_y, unit=self)
