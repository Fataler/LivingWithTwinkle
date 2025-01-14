################################################################################
## Экран паузы
################################################################################

init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu():
    modal True

    add Solid("#00000080")  # Затемнение фона

    # Доска меню
    frame:
        style_prefix "pause_menu"
        background "gui/menu_drop.png"
        at pause_menu_board_drop
        xsize 450
        ysize 900
        xalign 0.5
        yalign 0

        # Кнопки меню
        vbox at pause_menu_items_appear:
            spacing 30
            xalign 0.5
            ypos 200

            text "ПАУЗА" size 40 xalign 0.5 color "#ffffff"
            
            textbutton _("Сохранить") action [Hide("pause_menu"), ShowMenu("save")]
            textbutton _("Загрузить") action [Hide("pause_menu"), ShowMenu("load")]
            textbutton _("История") action [Hide("pause_menu"), ShowMenu("history")]
            textbutton _("Настройки") action [Hide("pause_menu"), ShowMenu("preferences")]
            textbutton _("Главное меню") action [Hide("pause_menu"), MainMenu()]
            textbutton _("Вернуться") action Return()

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

transform pause_menu_board_drop:
    ypos -900
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform pause_menu_items_appear:
    alpha 0.0
    pause 0.5
    easein 0.3 alpha 1.0