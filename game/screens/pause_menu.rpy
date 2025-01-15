################################################################################
## Экран паузы
################################################################################

init -2:
    $_game_menu_screen = "pause_menu"

screen pause_menu():
    modal True

    add Solid("#00000080")  # Затемнение фона

    add "menu_drop" at menu_board_drop:
        xalign 0.5

    # Доска меню
    frame:
        style_prefix "pause_menu"
        background None
        at pause_menu_board_drop
        xanchor 0.5
        xpos 0.5

        # Кнопки меню
        vbox at pause_menu_items_appear:
            spacing 30
            xpos 0
            ypos 210

            text "ПАУЗА" size 70 xalign 0.5 color "#ffffff" style "pause_menu_button_text"
            
            textbutton _("Сохранить") action [Hide("pause_menu"), ShowMenu("save")]
            textbutton _("Загрузить") action [Hide("pause_menu"), ShowMenu("load")]
            textbutton _("История") action [Hide("pause_menu"), ShowMenu("history")]
            textbutton _("Настройки") action [Hide("pause_menu"), ShowMenu("preferences")]
            textbutton _("Главное меню") action [Hide("pause_menu"), MainMenu()]
            textbutton _("Вернуться") action Return()

style pause_menu_button is navigation_button

style pause_menu_button_text is navigation_button_text:
    size 40

transform pause_menu_board_drop(start_pos = -900):
    ypos start_pos
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform pause_menu_board_hide(height = -900):
    ypos 0
    easeout 0.15 ypos -50
    easein 0.2 ypos 0
    easeout 0.5 ypos height

transform pause_menu_items_appear:
    alpha 0.0
    pause 0.5
    easein 0.3 alpha 1.0