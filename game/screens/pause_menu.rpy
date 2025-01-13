################################################################################
## Экран паузы
################################################################################
init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu():
    tag menu
    modal True  # Блокируем взаимодействие с игрой

    add Solid("#00000080")  # Полупрозрачный фон

    frame:
        style_prefix "pause_menu"
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 500
        background "#222222B3"

        vbox:
            spacing 20
            align (0.5, 0.5)

            text "ПАУЗА" size 40 xalign 0.5 color "#ffffff"
            
            textbutton _("Сохранить") action ShowMenu("save")
            textbutton _("Загрузить") action ShowMenu("load")
            textbutton _("История") action ShowMenu("history")
            textbutton _("Настройки") action ShowMenu("preferences")
            textbutton _("Главное меню") action MainMenu()
            textbutton _("Вернуться") action Hide("pause_menu")

style pause_menu_button:
    xalign 0.5
    background "#2222224D"
    padding (20, 10)
    xsize 200

style pause_menu_button_text:
    xalign 0.5
    color "#ffffff"
    hover_color "#ffff00"
    size 24