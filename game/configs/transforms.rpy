#common
transform c_left:
    xalign 0.1
    yalign 1.0

transform c_right:
    xalign 0.95
    yalign 1.0

transform face_left:
    xzoom -1.0

transform face_right:
    xzoom 1.0

transform move_by(x_offset=0, y_offset=0, duration=0.3):
    ease duration xoffset (self.xoffset + x_offset) yoffset (self.yoffset + y_offset)

transform move_to(x_offset=0, y_offset=0, duration=0.3):
    ease duration xoffset x_offset yoffset y_offset

# Уход персонажа за левый край экрана
transform exit_left(time=2.0):
    parallel:
        ease time xpos -1000
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

# Уход персонажа за правый край экрана
transform exit_right(time=2.0):
    parallel:
        ease time xpos 1000
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

# Вход персонажа слева
transform enter_left(time=1.0):
    xpos -1000
    parallel:
        ease time xalign 0.2
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

# Вход персонажа справа
transform enter_right(time=1.0):
    xpos 1920 + 1000
    parallel:
        ease time xalign 0.8
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform jumping(times = 1):
    yoffset 0
    linear 0.1 yoffset 10
    repeat times

transform step_right(steps=1, step_time=0.3, step_size=50):
    parallel:
        xoffset 0
        linear steps * step_time xoffset steps * step_size
    parallel:
        yoffset 0
        ease step_time/2 yoffset 10
        ease step_time/2 yoffset 0
        repeat steps

transform step_left(steps=1, step_time=0.3, step_size=50):
    parallel:
        xoffset 0
        linear steps * step_time xoffset steps * -step_size
    parallel:
        yoffset 0
        ease step_time/2 yoffset 10
        ease step_time/2 yoffset 0
        repeat steps

transform panic_run(times=4, run_time=0.5, distance=150):
    parallel:
        xoffset 0
        xzoom 1
        linear run_time xoffset distance
        xzoom -1
        linear run_time xoffset -distance
        repeat times
    parallel:
        yoffset 0
        ease run_time/2 yoffset 10
        ease run_time/2 yoffset 0
        repeat (times * 2)

transform flip:
    xzoom -1

transform flip_back:
    xzoom 1

transform menu_board_drop:
    ypos -900
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform menu_items_appear:
    alpha 0.0
    pause 0.7
    linear 0.3 alpha 1.0