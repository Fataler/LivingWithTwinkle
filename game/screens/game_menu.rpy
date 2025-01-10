init python:
    # Отключаем стандартное меню по ПКМ
    config.game_menu_action = None
    
    # Состояние меню (открыто/закрыто)
    menu_is_open = False
    
    def toggle_game_menu():
        global menu_is_open
        menu_is_open = not menu_is_open
        if menu_is_open:
            renpy.show_screen("game_menu_panel")
        else:
            renpy.hide_screen("game_menu_panel")

# Определение стилей для персонажей
style game_menu_button:
    background "#2222224D"
    padding (20, 10)
    xsize 150
    
style game_menu_button_text:
    color "#ffffff"
    hover_color "#ffff00"
    size 18
    align (0.5, 0.5)
    outlines [(2, "#000000", 0, 0)]

# Трансформы для анимации
transform menu_appear:
    on show:
        ypos 1.2  # Начинаем за пределами экрана (120% высоты)
        linear 0.3 ypos 0.99  # Выезжаем почти до конца экрана (98% высоты)
    on hide:
        ypos 0.99
        linear 0.3 ypos 1.2  # Уходим за пределы экрана

# Кнопка вызова меню
screen menu_button():
    zorder 100
    
    imagebutton:
        idle "gui/button/menu_idle.png"
        hover "gui/button/menu_hover.png"
        xalign 0.85
        yalign 0.98
        action [ToggleScreen("game_menu_panel"), Function(toggle_game_menu)]

# Выезжающая панель с кнопками
screen game_menu_panel():
    zorder 99
    
    frame:
        at menu_appear
        background "#222222B3"
        xsize 900
        ysize 80
        xalign 0.5
        yalign 1.0
        
        hbox:
            spacing 30
            align (0.5, 0.5)
            
            textbutton _("Сохранить") style "game_menu_button" action ShowMenu("save")
            textbutton _("Загрузить") style "game_menu_button" action ShowMenu("load")
            textbutton _("Настройки") style "game_menu_button" action ShowMenu("preferences")
            textbutton _("История") style "game_menu_button" action ShowMenu("history")
            textbutton _("Меню") style "game_menu_button" action MainMenu()

# Переопределяем стандартный quick_menu screen, чтобы скрыть стандартные кнопки
screen quick_menu():
    pass

# Добавляем нашу кнопку меню на все экраны
screen overlay():
    # Добавляем обработчик ПКМ на весь экран
    key "mouseup_3" action Function(toggle_game_menu)  # mouseup_3 это ПКМ
    
    use menu_button
