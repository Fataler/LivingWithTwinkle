# Музыка
define music_trouble = "audio/bg/And Here Comes the Trouble.ogg"
define music_nostalgy = "audio/bg/Bird Nostalgy.ogg"
define music_klementine = "audio/bg/Clementine Theme.ogg"
define music_felix = "audio/bg/Felix Theme.ogg"
define music_gratification = "audio/bg/Gratification.ogg"
define music_hover = "audio/bg/Hover.ogg"
define music_poultry = "audio/bg/Poultry house.ogg"
define music_tower = "audio/bg/The Tower.ogg"
define music_bandits = "audio/bg/Two Bandits.ogg"

# Игра
define sfx_nightmare = "audio/sfx/01 Nightmare.ogg"
define sfx_knock = "audio/sfx/02 Knock.ogg"
define sfx_agressive_knock = "audio/sfx/03 Agressive Knock.ogg"
define sfx_body_fall = "audio/sfx/04 Body Fall.ogg"
define sfx_letter = "audio/sfx/05 Letter.ogg"
define sfx_water_and_fire = "audio/sfx/06 Water and Fire.ogg"
define sfx_disassemble = "audio/sfx/07 Disassemble.ogg"
define sfx_knocked_down_door = "audio/sfx/08 Knocked Down Door.ogg"
define sfx_hat = "audio/sfx/09 Hat.ogg"
define sfx_timeskip = "audio/sfx/10 Timeskip.ogg"
define sfx_blackboard = "audio/sfx/11 Blackboard.ogg"

define sfx_chains = "audio/sfx/UI 06 Blackboard Down.ogg" #
define sfx_explosion = "audio/sfx/12 Explosion.ogg" #
define sfx_lever = "audio/sfx/13 Lever.ogg"

# Интерфейс
define sfx_ui_over = "audio/sfx/UI 01 Over.ogg" #
define sfx_ui_click = "audio/sfx/UI 02 Click.ogg" #
define sfx_ui_pipe_click = "audio/sfx/UI 03 Pipe Click.ogg" #
define sfx_ui_win = "audio/sfx/UI 04 Win.ogg" #
define sfx_ui_achieve = "audio/sfx/UI 05 Achive.ogg" #

# каналы
init python:
    renpy.music.register_channel("ui", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)
    renpy.music.register_channel("sfx", mixer="sfx", loop=False, stop_on_mute=True, tight=True, buffer_queue=True)