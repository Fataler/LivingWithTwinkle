transform bandit_c_left:
    xalign -0.2
    yalign 1.0

transform fel_table_pos:
    xpos 0

transform fel_board_pos:
    xpos -100
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
transform exit_right(time=4.0):
    parallel:
        ease time xpos 3000
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

# Вход персонажа слева
# transform enter_left(time=2.0, from_right=False):
#     xpos (2000 if from_right else -1000)
#     parallel:
#         ease time xalign 0.2
#     parallel:
#         block:
#             ease 0.2 yoffset 20
#             ease 0.2 yoffset 0
#             repeat (int(time * 2.5))

transform enter_c_left(time=2.0, from_right=False):
    xpos (2000 if from_right else -1000)
    parallel:
        ease time xalign 0.1
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform enter_c_right(time=2.0, from_left=False, xalign=0.95):
    xpos (-1000 if from_left else 2000)
    parallel:
        ease time xalign xalign
    parallel:
        block:
            ease 0.2 yoffset 20
            ease 0.2 yoffset 0
            repeat (int(time * 2.5))

transform step_up(steps=1, step_time=0.3, step_size=10):
    yoffset 0
    ease step_time yoffset step_size
    ease step_time yoffset 0
    repeat steps

transform move_step(xoffset=-100, time=0.3, steps = 1):
    parallel:
        xoffset 0
        linear time xoffset xoffset
    parallel:
        yoffset 0
        ease time yoffset 10
        ease time yoffset 0
        repeat steps

transform background_step(start=-1920, offset=100, time=0.5, yoffset=0):
    parallel:
        xpos start
        linear time xpos (start + offset)
    parallel:
        yoffset 0
        ease time yoffset yoffset
        ease time yoffset 0

# Вход персонажа справа
# transform enter_right(time=2.0, xalign = 0.8):
#     xpos 1920 + 1000
#     parallel:
#         ease time xalign xalign
#     parallel:
#         block:
#             ease 0.2 yoffset 20
#             ease 0.2 yoffset 0
#             repeat (int(time * 2.5))

transform jumping(times = 1, height = 20, speed = 0.3):
    yoffset 0
    linear speed yoffset height
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

transform put_down(speed=0.2, offset=-10):
    parallel:
        linear speed xoffset offset
        linear speed xoffset 0
    parallel:
        linear speed yoffset 50
        linear speed yoffset 0

transform punch_h(duration=0.1, strength=10):
    xoffset 0
    ease duration/4 xoffset strength
    ease duration/4 xoffset -strength
    ease duration/4 xoffset strength/2
    ease duration/4 xoffset 0

transform hide_after_pause(time = 1, alpha_time = 0.1):
    pause time
    linear alpha_time alpha 0.0

transform giggle(height=5, shake=3, repeats=3, speed=0.15):
    parallel:
        ease speed yoffset height
        ease speed yoffset 0
        repeat repeats
    parallel:
        ease speed*0.7 xoffset shake
        ease speed*0.7 xoffset -shake
        repeat (repeats + 1)

transform fear(height=10, shake=5, repeats=2, fade=0.2):
    parallel:
        ease 0.2 yoffset height
        ease 0.2 yoffset 0
        repeat repeats
    parallel:
        ease 0.15 xoffset shake
        ease 0.15 xoffset -shake
        repeat (repeats + 1)

transform joy(height=10, shake=3, repeats=2, speed=0.15):
    parallel:
        ease speed yoffset height
        ease speed yoffset 0
        repeat repeats
    parallel:
        ease speed*0.7 xoffset shake
        ease speed*0.7 xoffset -shake
        repeat repeats

transform scared(height=30, speed=0.15):
    yoffset 0
    ease speed yoffset height*0.7
    ease speed*1.5 yoffset 0
    ease speed*0.5 yoffset height*0.3
    ease speed yoffset 0

transform angry(height=8, shake=5, repeats=3, speed=0.1):
    parallel:
        ease speed yoffset height
        ease speed yoffset 0
        repeat repeats
    parallel:
        ease speed*0.5 xoffset -shake
        ease speed*0.5 xoffset shake
        repeat (repeats * 2)

transform flipping(repeats=3, pause_time=0.9, flip_time=0.3):
    xzoom 1.0
    block:
        pause pause_time
        xzoom -1.0
        pause pause_time
        xzoom 1.0
        repeat repeats
