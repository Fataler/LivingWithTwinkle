init python:
    PIPE_TYPES = {
        "straight": ["-", "|"],  # горизонтальная и вертикальная
        "corner": ["└", "┌", "┐", "┘"],  # угловые трубы, начиная с вниз-вправо
    }

    class PipeGame:
        def __init__(self):
            self.size = 6
            self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
            self.solution = self._generate_solution()
            self.current_state = self._generate_initial_state()
            self.debug = False
        
        def _generate_solution(self):
            solution = [
                ["┐", "*", "*", "*", "*", "*"],
                ["└", "-", "┐", "┌", "-", "┐"],
                ["┌", "-", "┘", "|", "*", "|"],
                ["|", "*", "*", "|", "┌", "┘"],
                ["|", "*", "┌", "┘", "└", "┐"],
                ["└", "-", "┘", "*", "*", "└"]
            ]
            return solution
        
        def _generate_initial_state(self):
            initial_state = [
                ["┐", "|", "└", "|", "└", "┘"],
                ["┐", "-", "└", "┘", "-", "└"],
                ["└", "|", "┐", "|", "|", "-"],
                ["|", "┘", "┌", "-", "┘", "└"],
                ["-", "-", "┘", "└", "┐", "┘"],
                ["┐", "|", "┌", "|", "┘", "└"]
            ]
            return initial_state
        
        def get_pipe_rotation(self, pipe_type):
            # Возвращаем угол поворота в градусах для спрайта
            if pipe_type in PIPE_TYPES["straight"]:
                return 90 if pipe_type == "|" else 0
            elif pipe_type in PIPE_TYPES["corner"]:
                return PIPE_TYPES["corner"].index(pipe_type) * 90
            return 0
        
        def get_pipe_image(self, pipe_type):
            # Возвращаем имя спрайта и его поворот
            if pipe_type in PIPE_TYPES["straight"]:
                return "images/mini_games/pipes/pipe_straight.png", self.get_pipe_rotation(pipe_type)
            elif pipe_type in PIPE_TYPES["corner"]:
                return "images/mini_games/pipes/pipe_corner.png", self.get_pipe_rotation(pipe_type)
            return None, 0
        
        def rotate_pipe(self, x, y):
            current = self.current_state[x][y]
            if current in PIPE_TYPES["straight"]:
                self.current_state[x][y] = PIPE_TYPES["straight"][(PIPE_TYPES["straight"].index(current) + 1) % 2]
            elif current in PIPE_TYPES["corner"]:
                self.current_state[x][y] = PIPE_TYPES["corner"][(PIPE_TYPES["corner"].index(current) + 1) % 4]
            
            # Проверяем решение после каждого хода
            if self.check_solution():
                return True
        
        def check_solution(self):
            for i in range(self.size):
                for j in range(self.size):
                    if self.solution[i][j] != "*" and self.current_state[i][j] != self.solution[i][j]:
                        return False
            return True

# Экран
screen pipe_game():
    modal True
    
    default game = PipeGame()
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 10
        ypadding 20
        
        vbox:
            spacing 10
            
            # Сетка
            grid game.size game.size:
                spacing -70
                for i in range(game.size):
                    for j in range(game.size):
                        if game.current_state[i][j]:
                            $ pipe = game.current_state[i][j]
                            $ is_in_solution = game.solution[i][j] != "*"
                            $ is_correct = is_in_solution and game.current_state[i][j] == game.solution[i][j]
                            $ image_name, rotation = game.get_pipe_image(pipe)
                            
                            button:
                                action Function(game.rotate_pipe, i, j)
                                
                                if game.debug and is_in_solution:
                                    hover_background ("#00ff0022" if is_correct else "#ff000022")
                                
                                add image_name:
                                    rotate rotation
                                    size (128, 128)
                                
                                if game.debug:
                                    text "[i],[j]" size 12 xalign 0.5
                                    
                                    if is_in_solution:
                                        text ("✓" if is_correct else "✗") size 12 xalign 0.5 color ("#00ff00" if is_correct else "#ff0000")
            
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Сдаться":
                    action Return(game.check_solution())

# Метка для тестирования
label test_pipe_game:
    $ result = renpy.call_screen("pipe_game")
    if result:
        "Отлично! Вы правильно соединили трубы!"
        $ renpy.pause(2.0, hard=True)
    else:
        "Трубы соединены неправильно."
    return
