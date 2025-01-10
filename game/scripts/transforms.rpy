#common
transform left:
    xalign 0.2
    yalign 1.0

transform right:
    xalign 0.8
    yalign 1.0

# Отзеркаливание
transform flip:
    xzoom -1.0

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

#ch1