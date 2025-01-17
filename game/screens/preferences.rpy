## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

default mouse_xy = (0, 0)

define persistent.current_font = "default"
init python:
    if persistent.current_font is None:
        persistent.current_font = "default"

    def update_font_size():
        if (persistent.current_font == "default"):
            style.navigation_button_text.size = 55
            style.navigation_vbox.area = (0, 300, 700, 100)
        else:
            style.navigation_button_text.size = 40
            style.navigation_vbox.area = (0, 330, 700, 100)
        
        style.rebuild()
        renpy.restart_interaction()

    config.start_callbacks.append(update_font_size)

    def reset_preferences():
        _preferences.set_volume('music', 0.1)
        _preferences.set_volume('sfx', 0.1)
        _preferences.set_volume('voice', config.default_voice_volume if hasattr(config, 'default_voice_volume') else 1.0)

        _preferences.text_cps = config.default_text_cps if hasattr(config, 'default_text_cps') else 40
        _preferences.afm_time = config.default_afm_time if hasattr(config, 'default_afm_time') else 15
        _preferences.font_transform = None
        persistent.current_font = "default"
        _preferences.font_size = 1.0

        if renpy.variant("pc"):
            _preferences.fullscreen = config.default_fullscreen if hasattr(config, 'default_fullscreen') else False

        renpy.style.rebuild()
        renpy.restart_interaction()

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            xfill True
            xalign 0.5
            spacing 25

            vbox:
                xalign 0.5
                spacing 10
                label _("Режим экрана"):
                    xalign 0.5
                hbox:
                    xalign 0.5
                    box_wrap True
                    spacing 200
                    if renpy.variant("pc") or renpy.variant("web"):
                        style_prefix "radio"
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

            vbox:
                xalign 0.5
                spacing 15
                label _("Текст")
                hbox:
                    xalign 0.5
                    spacing 100
                    xsize 1000
                    vbox:
                        xalign 0.5
                        spacing 15
                        text _("Скорость текста") style "label_bar_text"
                        text _("Скорость авточтения") style "label_bar_text"
                        text _("Пропускать") style "label_bar_text"
                    vbox:
                        xalign 0.5
                        spacing 15
                        xsize 525
                        yoffset 8
                        bar value Preference("text speed")
                        bar value Preference("auto-forward time")
                        hbox:
                            xalign 0.5
                            spacing 20
                            style_prefix "check"
                            textbutton _("Прочитанный текст") action Preference("skip", "seen")
                            textbutton _("Весь текст") action Preference("skip", "all")

            vbox:
                xalign 0.5
                spacing 15
                label _("Звук")
                hbox:
                    xalign 0.5
                    spacing 100
                    xsize 1000
                    vbox:
                        xalign 0.5
                        spacing 15
                        if config.has_music:
                            text _("Громкость музыки") style "label_bar_text"
                        if config.has_sound:
                            text _("Громкость звуков") style "label_bar_text"
                        if config.has_voice:
                            text _("Громкость голоса") style "label_bar_text"
                    vbox:
                        xalign 0.5
                        spacing 15
                        xsize 525
                        xoffset 20
                        yoffset 8
                        if config.has_music:
                            hbox:
                                xalign 0.5
                                bar value Preference("music volume")
                                if config.sample_sound:
                                    textbutton _("Тест") action Play("sound", config.sample_sound)
                        if config.has_sound:
                            hbox:
                                xalign 0.5
                                bar value Preference("sound volume")
                                if config.sample_sound:
                                    textbutton _("Тест") action Play("sound", config.sample_sound)
                        if config.has_voice:
                            hbox:
                                xalign 0.5
                                bar value Preference("voice volume")
                                if config.sample_voice:
                                    textbutton _("Тест") action Play("voice", config.sample_voice)
                        if config.has_music or config.has_sound or config.has_voice:
                            hbox:
                                xalign 0.5
                                style_prefix "check"
                                textbutton _("Без звука") action Preference("all mute", "toggle")

            vbox:
                xalign 0.5
                spacing 10
                label _("Специальные возможности"):
                    xalign 0.5
                hbox:
                    xalign 0.5
                    box_wrap True
                    spacing 30
                    style_prefix "radio"
                    vbox:
                        xalign 0.5
                        spacing 10
                        label _("Шрифт")

                        textbutton _("Оригинальный"):
                            action [Preference("font transform", None), 
                                    SetField(persistent, "current_font", "default"),
                                    Function(update_font_size)]
                            style_suffix "radio_button"

                        textbutton _("DejaVu Sans"):
                            action [SetField(persistent, "current_font", "dejavusans"),
                                    Function(update_font_size),
                                    Preference("font transform", "dejavusans")]
                            style_suffix "radio_button"
                            tooltip "Шрифт, используемый в \nRen'Py по умолчанию"

                    vbox:
                        xalign 0.5
                        spacing 10
                        label _("Размер текста")
                        textbutton _("Маленький"):
                            action Preference("font size", 0.8)
                            style_suffix "radio_button"

                        textbutton _("Обычный"):
                            action Preference("font size", 1.0)
                            style_suffix "radio_button"

                        textbutton _("Большой"):
                            action Preference("font size", 1.2)
                            style_suffix "radio_button"
                            tooltip "Внимание! \nТекст может слегка выходить за рамки."

                    vbox:
                        xalign 0.5
                        spacing 10
                        label _("High Contrast Text")

                        textbutton _("Enable"):
                            action Preference("high contrast text", "enable")
                            style_suffix "radio_button"

                        textbutton _("Disable"):
                            action Preference("high contrast text", "disable")
                            style_suffix "radio_button"

    fixed:
        textbutton _("Сброс"):
            style "navigation_button"
            xpos 120
            ypos 30
            text_align 0.0
            action Function(reset_preferences)
            tooltip "Сбросить настройки\nна значения по умолчанию"


    $ tooltip = GetTooltip()

    if tooltip:
        $ mx = mouse_xy[0]
        $ my = mouse_xy[1]
        $ get_mouse()
        
        timer 0.1 repeat True action Function(get_mouse)
        $ mx = mouse_xy[0]
        $ my = mouse_xy[1]
        frame:
            pos(mx, my)
            offset 50, 0
            background Frame("gui/frame.png", gui.frame_borders)
            padding (20, 10)
            text tooltip:
                font gui.interface_text_font
                color gui.interface_text_color
                size 35

init -2 python:
    def get_mouse():
        global mouse_xy
        mouse_xy = renpy.get_mouse_pos()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style label_bar_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style label_bar_text:
    color gui.interface_text_color
    font gui.interface_text_font

style pref_vbox:
    xsize 338

style tooltip:
    padding (10, 5)
    background "#222222"
    xalign 0.5
    yalign 1.0
    yoffset -50

style tooltip_text:
    size 106
    color "#ffffff"
    text_align 0.5
    xalign 0.5