class Unit:
    def move(self, field, x, y, direction, is_flying, is_sneaking, speed=1):
        if is_flying and is_sneaking:
            raise ValueError('Рожденный ползать летать не должен!')
        if is_flying:
            speed *= 1.2
            if direction == 'UP':
                y += speed
            elif direction == 'DOWN':
                y -= speed
            elif direction == 'LEFT':
                x -= speed
            elif direction == 'RIGHT':
                x += speed
        if is_sneaking:
            speed *= 0.5
            if direction == 'UP':
                y += speed
            elif direction == 'DOWN':
                y -= speed
            elif direction == 'LEFT':
                x -= speed
            elif direction == 'RIGHT':
                x += speed


#     ...
