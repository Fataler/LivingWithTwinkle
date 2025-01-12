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

transform step_right(steps=1, step_time=0.3, step_size=50):
    parallel:
        xoffset 0
        linear steps * step_time xoffset steps * step_size
    parallel:
        yoffset 0
        ease step_time/2 yoffset -10
        ease step_time/2 yoffset 0
        repeat steps

transform step_left(steps=1, step_time=0.3, step_size=50):
    parallel:
        xoffset 0
        linear steps * step_time xoffset steps * -step_size
    parallel:
        yoffset 0
        ease step_time/2 yoffset -10
        ease step_time/2 yoffset 0
        repeat steps