## Экран "Прошло времени" #####################################################
##
## Ипользуется для перебивки между сценами.
##

transform show_screen_transform:
    on show:
        parallel:
            alpha 0.0
            linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

transform loading_move:
    xzoom -1.0
    parallel:
        xpos -128 yalign 0.95  # начальная позиция слева
        linear 7.0 xpos 1920+128   # движение вправо за 7 секунд
    parallel:
        block:
            ease 1 yoffset 20
            ease 1 yoffset 0
            repeat

# init python:
#     loading_frames = []
#     for j in range(3):  # по вертикали
#         for i in range(4):  # по горизонтали
#             loading_frames.append(
#                 Transform(
#                     "gui/loading.png",
#                     crop=(697 * i, 800 * j, 697, 800)
#                 )
#             )

# image loading_animation:
#     size (128, 128)
#     block:
#         loading_frames[0]
#         0.1
#         loading_frames[1]
#         0.1
#         loading_frames[2]
#         0.1
#         loading_frames[3]
#         0.1
#         loading_frames[4]
#         0.1
#         loading_frames[5]
#         0.1
#         loading_frames[6]
#         0.1
#         loading_frames[7]
#         0.1
#         loading_frames[8]
#         0.1
#         loading_frames[9]
#         0.1
#         loading_frames[10]
#         0.1
#         loading_frames[11]
#         0.1
#         repeat

screen time_passed(text="Прошло времени..."):
    modal True
    
    fixed:
        xfill True
        yfill True
        at show_screen_transform
        
        add Solid("#121212")
        
        vbox:
            align (0.5, 0.5)
            spacing 50
            
            text text:
                size 80
                color gui.text_color
                text_align 0.5
                at transform:
                    alpha 0.0
                    pause 1.0
                    ease 2.0 alpha 1.0

        add "b_fire":
            at loading_move
            at transform:
                alpha 0.0
                ease 2.0 alpha 1.0

    timer 7.0 action Return()

label time_passed(message = "Некоторое время спустя"):
    window hide
    stop music
    stop sound

    play sound sfx_timeskip
    call screen time_passed(message)
    scene bg_black
    pause 1
    stop sound
    window show
return