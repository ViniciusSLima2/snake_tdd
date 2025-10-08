import os
import keyboard
import time


class io_handler:
    
    x_size: int
    y_size: int
    game_speed = float
    last_input: str
    matrix = []

    def __init__(self, dim, speed):
        self.x_size = dim[0]
        self.y_size = dim[1]
        
        self.game_speed = speed
        self.last_input = 'w'

        for i in range (self.y_size): 
            self.matrix.append([0]*self.x_size)

    def record_inputs(self):
        keyboard.add_hotkey('w', lambda: setattr(self, "last_input", 'w'))
        keyboard.add_hotkey('a', lambda: setattr(self, "last_input", 'a'))
        keyboard.add_hotkey('s', lambda: setattr(self, "last_input", 's'))
        keyboard.add_hotkey('d', lambda: setattr(self, "last_input", 'd'))
        keyboard.add_hotkey('esc', lambda: setattr(self, "last_input", 'end'))

    def display(self):
        def display_h_line(self):
            print ('+', end='')
            print ('--'* len(self.matrix[0]), end='')
            print ('+')
        
        def display_content_line(line):
            print ('|', end='')
            for item in line: 
                if item == 1:
                    print ('[]', end='')
                elif item == 2:
                    print ('<>', end='')
                elif item == 3:
                    print ('()', end='')
                else:
                    print ('  ', end='')

            print ('|')

        os.system('cls' if os.name == 'nt' else 'clear')
        display_h_line(self)
        for line in self.matrix:
            display_content_line(line)
        display_h_line(self)


# Continuação da classe SnakeGame da Etapa 2
class SnakeGame:
    DIRECTIONS = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    OPPOSITES = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake_body = [(height // 2, width // 2)]
        self.direction = 'w'
        self.game_over = False
        self.pending_direction = 'w'

    def change_direction(self, new_direction):
        self.pending_direction = new_direction

    def update(self):
        if self.pending_direction != self.OPPOSITES.get(self.direction):
            self.direction = self.pending_direction

        dy, dx = self.DIRECTIONS[self.direction]

        head_y, head_x = self.snake_body[0]

        # Lógica de wrapping
        new_head_y = (head_y + dy) % self.height
        new_head_x = (head_x + dx) % self.width
        new_head = (new_head_y, new_head_x)

        self.snake_body.insert(0, new_head)
        self.snake_body.pop()

if __name__ == "__main__":
    # exemplo do uso da classe io_handler — só executa quando rodamos o arquivo diretamente,
    instance = io_handler((10, 15), 0.5)
    instance.matrix[0][0] = 1  # corpo
    instance.matrix[0][1] = 2  # cabeça
    instance.matrix[0][2] = 3  # fruta

    def game_loop():
        instance.record_inputs()
        while True:
            instance.display()
            print("mova com WASD, saia com esc. Ultimo botão:", end=' ')
            print(instance.last_input)
            if instance.last_input == 'end':
                exit()
            time.sleep(instance.game_speed)

    game_loop()