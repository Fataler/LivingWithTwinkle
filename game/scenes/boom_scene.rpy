image boom:
    block:
        "images/boom/boom_1.png"
        pause 0.1
        "images/boom/boom_2.png"
        pause 0.1
        "images/boom/boom_3.png"
        pause 0.1
        "images/boom/boom_4.png"
        pause 0.1
        "images/boom/boom_5.png"
        pause 0.1
        "images/boom/boom_6.png"
        pause 0.1
        "images/boom/boom_7.png"
        pause 0.1

image roofs:
    "images/boom/roofs.png"
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5

label boom_scene:
    $ _skipping = False

    play sfx ["<silence 1.9>", sfx_explosion]

    scene roofs with fade:
        zoom 1.3
        linear 2 zoom 1.0
    pause 2

    show boom:
        pause 0.4
        linear 1 ypos -70 alpha 0.0

    pause 0.1
    show roofs at punch_h(0.4, 8):
        zoom 1.0
        linear 0.1 zoom 1.1
        linear 0.1 zoom 1
        repeat 1

    pause 0.6

    pause 3
    $ _skipping = True
    return
