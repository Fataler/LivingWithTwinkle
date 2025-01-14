## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.

screen navigation():
    
    # Доска меню
    add "gui/menu_drop.png" at menu_board_drop:
        xpos 10  # Отступ слева
        
    # Кнопки меню
    vbox at menu_items_appear:
        style_prefix "navigation"
        xpos 40  # Отступ для текста от левого края
        yalign 0.5
        spacing gui.navigation_spacing
        

        if main_menu:
            textbutton _("Начать") action Start()
        else:
            textbutton _("История") action ShowMenu("history")
            textbutton _("Сохранить") action ShowMenu("save")

        textbutton _("Загрузить") action ShowMenu("load")
        
        textbutton _("Достижения") action ShowMenu("achievements_screen")

        textbutton _("Настройки") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("Завершить повтор") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        if renpy.variant("pc"):
            textbutton _("Выход") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound "audio/button_hover.ogg"
    activate_sound "audio/button_click.ogg"
    xminimum 400
    xalign 0.5

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    color "#000"  # Черный цвет для текста
    hover_color "#8B0000"  # Темно-красный при наведении
    size 40
    xalign 0.5

transform menu_board_drop:
    ypos -900
    easein 0.5 ypos 0
    easeout 0.2 ypos -50
    easein 0.15 ypos 0

transform menu_items_appear:
    alpha 0.0
    pause 0.5
    easein 0.3 alpha 1.0