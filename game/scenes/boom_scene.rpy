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

scene roofs with fade:
    zoom 1.1
    linear 0.5 zoom 1.0
pause 2

show boom at hide_after_pause(0.7)

pause 0.1
show roofs with hpunch
pause 0.6

pause 4

return
