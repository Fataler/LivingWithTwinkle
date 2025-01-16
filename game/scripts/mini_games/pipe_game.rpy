init python:
    PIPE_TYPES = {
        "straight": ["-", "|"],  # горизонтальная и вертикальная
        "corner": ["└", "┌", "┐", "┘"],  # угловые трубы, начиная с вниз-вправо
    }

    def get_shortest_rotation(current, target):
        diff = (target - current) % 360
        if diff > 180:
            diff -= 360
        return current + diff

    class ResetAnimation(Action):
        def __init__(self, game):
            self.game = game
            
        def __call__(self):
            self.game.is_animating = False

    class PipeGame:
        def __init__(self):
            self.size = 6
            self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
            self.solution = self._generate_solution()
            self.current_state = self._generate_initial_state()
            self.debug = False
            self.current_rotations = [[0 for _ in range(self.size)] for _ in range(self.size)]
            self.is_animating = False
        
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
                return PIPE_TYPES["straight"].index(pipe_type) * 90
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
            if self.is_animating:
                return
                
            self.is_animating = True
            current = self.current_state[x][y]

            renpy.play(sfx_ui_pipe_click, channel="ui")
            
            if current in PIPE_TYPES["straight"]:
                self.current_state[x][y] = PIPE_TYPES["straight"][(PIPE_TYPES["straight"].index(current) + 1) % 2]
            elif current in PIPE_TYPES["corner"]:
                self.current_state[x][y] = PIPE_TYPES["corner"][(PIPE_TYPES["corner"].index(current) + 1) % 4]
            
            if self.check_solution():
                renpy.play(sfx_ui_win, channel="ui")
                renpy.set_screen_variable("show_success", True)
                renpy.set_screen_variable("success_timer", 2.0)
        
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
    default show_success = False
    default success_timer = 0.0
    default animation_timer = 0.0
    
    if animation_timer > 0.0:
        timer animation_timer action [SetScreenVariable("animation_timer", 0.0), SetField(game, "is_animating", False)]
    
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        
        vbox:
            spacing 10
            
            # Сетка
            grid game.size game.size:
                spacing 0
                for i in range(game.size):
                    for j in range(game.size):
                        if game.current_state[i][j]:
                            $ pipe = game.current_state[i][j]
                            $ is_in_solution = game.solution[i][j] != "*"
                            $ is_correct = is_in_solution and game.current_state[i][j] == game.solution[i][j]
                            $ image_name, rotation = game.get_pipe_image(pipe)
                            $ current_rot = game.current_rotations[i][j]
                            
                            button:
                                xsize 150
                                ysize 150
                                action [
                                    Function(game.rotate_pipe, i, j),
                                    SetDict(game.current_rotations[i], j, game.get_pipe_rotation(game.current_state[i][j])),
                                    SetScreenVariable("animation_timer", 0.2)
                                ]
                                
                                if game.debug and is_in_solution:
                                    hover_background ("#00ff0022" if is_correct else "#ff000022")
                                
                                add image_name:
                                    xalign 0.5
                                    yalign 0.5
                                    at pipe_rotate(current_rot, game.get_pipe_rotation(game.current_state[i][j]))
                                    size (150, 150)
            
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "Сдаться":
                    action Return(False)

                # textbutton "Победить":
                #     action [
                #         SetScreenVariable("show_success", True),
                #         SetScreenVariable("success_timer", 2.0)
                #     ]
    
    if show_success:
        timer success_timer repeat False action Return(True)
        
        frame at success_appear:
            xfill True
            yfill True
            background "#0008"
            
            text "Успех!" at success_text size 75 color "#fff" xalign 0.5 yalign 0.5

transform success_appear:
    alpha 0.0 zoom 1.5
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        ease 0.5 zoom 1.0
        ease 0.15 zoom 1.1
        ease 0.15 zoom 1.0

transform success_text:
    alpha 0.0 zoom 1.5
    pause 0.3
    parallel:
        ease 0.3 alpha 1.0
    parallel:
        ease 0.3 zoom 1.0
        ease 0.1 zoom 1.2
        ease 0.1 zoom 1.0

transform pipe_rotate(old_rotation, new_rotation):
    rotate old_rotation
    linear 0.2 xzoom 0.9 yzoom 0.9
    linear 0.2 rotate get_shortest_rotation(old_rotation, new_rotation) xzoom 1.0 yzoom 1.0

# Для тестирования
label test_pipe_game:
    $ result = renpy.call_screen("pipe_game")
    if result:
        "Отлично! Вы правильно соединили трубы!"
        $ renpy.pause(2.0, hard=True)
    else:
        "Трубы соединены неправильно."
    return
