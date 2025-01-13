## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Пропуск")
                    textbutton _("Прочитанный текст") action Preference("skip", "seen")
                    textbutton _("Весь текст") action Preference("skip", "all")

                ## Дополнительные vbox'ы типа "radio_pref" или "check_pref"
                ## могут быть добавлены сюда для добавления новых настроек.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость текста")

                    bar value Preference("text speed")

                    label _("Скорость авточтения")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Громкость голоса")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Без звука"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

                vbox:

                    label _("Font Override")

                    null height 10

                    textbutton _("Стандартный"):
                        action Preference("font transform", None)
                        style_suffix "radio_button"
                        tooltip _("Обычный шрифт игры")

                    textbutton _("DejaVu Sans"):
                        action Preference("font transform", "dejavusans")
                        style_suffix "radio_button"
                        tooltip _("Шрифт в Ren'Py по умолчанию")

                    textbutton _("Opendyslexic"):
                        action Preference("font transform", "opendyslexic")
                        style_suffix "radio_button"
                        tooltip _("Специальный шрифт для людей с дислексией")

                    null height 10

                    label _("Text Size Scaling")

                    null height 10

                    textbutton _("Обычный"):
                        action Preference("font size", 1.0)
                        style_suffix "radio_button"

                    textbutton _("Большой"):
                        action Preference("font size", 1.1)
                        style_suffix "radio_button"

                    textbutton _("Огромный"):
                        action Preference("font size", 1.2)
                        style_suffix "radio_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
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

style pref_vbox:
    xsize 338

style tooltip:
    padding (10, 5)
    background "#222222"
    xalign 0.5
    yalign 1.0
    yoffset -50

style tooltip_text:
    size 16
    color "#ffffff"
    text_align 0.5
    xalign 0.5