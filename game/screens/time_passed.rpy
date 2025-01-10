## Экран "Прошло времени" #####################################################
##
## Ипользуется для перебивки между сценами.
##

transform time_passed_transform:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

transform loading_move:
    xpos -128 yalign 0.95  # начальная позиция слева
    linear 7.0 xpos 1920+128   # движение вправо за 7 секунд (время показа экрана)

init python:
    # Создаем список кадров анимации загрузки
    loading_frames = []
    for j in range(2):  # по вертикали
        for i in range(2):  # по горизонтали
            loading_frames.append(
                Transform(
                    "gui/loading2.png",
                    crop=(128 * i, 128 * j, 128, 128)
                )
            )

image loading_animation:
    size (128, 128)
    block:
        loading_frames[0]
        0.1
        loading_frames[1]
        0.1
        loading_frames[2]
        0.1
        loading_frames[3]
        0.1
        repeat

screen time_passed(text="Прошло времени..."):
    modal True
    
    fixed:
        xfill True
        yfill True
        at time_passed_transform
        
        add Solid("#000000")
        # add "gui/overlay/ctc.png"
        
        vbox:
            align (0.5, 0.5)
            spacing 50
            
            text text:
                size 80
                color "#ffffff"
                text_align 0.5
                at transform:
                    alpha 0.0
                    pause 1.0
                    ease 2.0 alpha 1.0
            
            add "ctc_rotate":
                xalign 0.5
                size (64, 64)
                at transform:
                    alpha 0.0
                    ease 2.0 alpha 1.0

        text "(Место для чибби-приколов)":
            size 60
            color "#ffffff"
            text_align 0.5
            xalign 0.5
            yalign 0.7

        add "loading_animation":
            at loading_move
            at transform:
                alpha 0.0
                ease 2.0 alpha 1.0

    timer 7.0 action Return()