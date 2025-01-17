## Экран главного меню
init:
    image bg_white = Solid("#ffffff")
    image menu_background_image:
        "gui/menu_bg.png"
        anchor (0.5, 0.5)
        xsize 1.10
        ysize 1.10
    image menu_tower_image:
        "gui/menu_tower.png"
        anchor (0.5, 0.5)
        xsize 1.25
        ysize 1.25
    image menu_clouds_image:
        "gui/menu_clouds.png"
        anchor (0.5, 0.5)
        xsize 1.35
        ysize 1.35

screen main_menu():
    on "show" action Function(renpy.play, sfx_chains, channel="sfx")
    on "replace" action Function(renpy.play, sfx_chains, channel="sfx")

    tag menu

    add Parallax("menu_background_image", 3)
    add Parallax("menu_tower_image", 5)
    add Parallax("menu_clouds_image", 15)

    use navigation

    use real_clock

    imagebutton idle "gui/chapel.png":#im.Scale("gui/chapel.png", 50, 50):
        action OpenURL('https://vk.com/chapel_jam')
        xalign 0.95
        yalign 0.9
        at hover_scale

    if show_main_menu_fade:
        add "bg_white" at menu_alpha_out(1)
        timer 1 action SetVariable("show_main_menu_fade", False)

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
    anchor (0.5, 0.5)
    rotate 0
    on idle:    
        parallel:
            linear 0.1 xzoom 1.0 yzoom 1.0
    on hover:
        parallel:
            linear 0.1 xzoom 1.1 yzoom 1.1

transform menu_alpha_out(time=0.5):
    alpha 1
    linear time alpha 0

transform alpha_in(time=0.5):
    alpha 0
    linear time alpha 1

transform alpha_out(time=0.5):
    alpha 1
    linear time alpha 0
