## Экран главного меню
screen main_menu():
    tag menu

    # Фон главного меню
    add gui.main_menu_background

    # Затемнение
    add "gui/overlay/main_menu.png"

    # Навигация
    use navigation

    use real_clock

    imagebutton idle "gui/chapel.jpg":
        action OpenURL('https://vk.com/chapel_jam')
        xalign 0.95
        yalign 0.8
        at hover_scale

    # Название игры
    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"

style main_menu_vbox is vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text is gui_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title is main_menu_text:
    properties gui.text_properties("title")

style main_menu_version is main_menu_text:
    properties gui.text_properties("version")

transform hover_scale:
    rotate 0
    on idle:    
        parallel:
            linear 0.1 xzoom 1.0 yzoom 1.0 rotate 0
    on hover:
        parallel:
            linear 0.1 xzoom 1.1 yzoom 1.1 rotate -5