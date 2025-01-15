# Создаем анимацию для индикатора
image ctc_rotate:
    "gui/cog.png"
    size (32, 32)
    anchor (0.5, 0.5)  # центр вращения
    alpha 1
    linear 1 alpha 0.8
    linear 1 alpha 1
    #rotate 0
    #linear 8.0 rotate 360
    repeat

define ctc_indicator = Animation("ctc_rotate")

image ctc_mind:
    "gui/ctc_mind.png"
    size (50, 50)
    anchor (0.5, 0.5)  # центр вращения
    alpha 1
    linear 2 alpha 0.6
    linear 2 alpha 1
    repeat

define ctc_mind_indicator = Animation("ctc_mind")

# Определение персонажей
define F = Character("Феликс", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,      
    ctc_position="nestled",
    what_slow_abortable=False
)

define F_m = Character("Феликс", 
    what_prefix="{i}(",
    what_suffix="){/i} ",
    ctc=ctc_mind_indicator,      
    ctc_position="nestled",
    what_slow_abortable=False
)

define S = Character("Секретарь", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_abortable=False
)

define K = Character("Клементина", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_abortable=False
)

define R1 = Character("Аркан", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_abortable=False
)

define R2 = Character("Мундштук", 
    what_prefix="",
    what_suffix="",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_abortable=False
)

style ctc_text is text:
    size 24
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

# трансформ для моргания
transform parametric_blink(open_img, closed_img, min_wait=2.0, max_wait=4.0, blink_speed=0.15, double_blink_chance=0.03):
    open_img
    block:
        choice:
            pause min_wait
        choice:
            pause (min_wait + max_wait) / 2
        choice:
            pause max_wait
        closed_img
        pause 0.1
        open_img
        repeat

# Трансформ для конкретного персонажа
# transform alice_blink:
#     parametric_blink("images/characters/alice/1.png", "images/characters/alice/2.png")

# Определение спрайтов с помощью LayeredImage
# layeredimage alice:
#     group base:
#         attribute base default at alice_blink
#         attribute talking:
#             "images/characters/alice/normal.png"

#Определение изображений Феликса
# layeredimage f:
#     group pose:
#         attribute normal default:
#             "images/characters/felix/normal.png"
#         attribute angry
#         attribute sad

#     group state:
#         attribute base default:
#             "images/characters/felix/normal.png"
#         attribute glass:
#             "images/characters/felix/glass.png"
#         attribute cat:
#             "images/characters/felix/cat.png"

#     group if_angry:
#         attribute base if_any "angry":
#             "images/characters/felix/angry.png"
#         attribute glass if_any "angry":
#             "images/characters/felix/angry_talking.png"
#         attribute cat if_any "angry":
#             "images/characters/felix/angry_cat.png"

#     group if_sad:
#         attribute base if_any "sad":
#             "images/characters/felix/sad.png"
#         attribute glass if_any "sad":
#             "images/characters/felix/sad_talking.png"
#         attribute cat if_any "sad":
#             "images/characters/felix/sad_angry.png"

# Клементина
# layeredimage k:
#     group pose:
#         attribute normal

#     group state:
#         attribute base default:
#             "images/characters/klem/normal.png"
#         attribute shvabra:
#             "images/characters/klem/shvabra_1.png"

# Секретарь
# image s:
#     "images/characters/secretary/normal.png"


# Бандит 1

image b1:
    "images/characters/bandits/b1.png"

# Бандит 2

image b2:
    "images/characters/bandits/b2.png"

layeredimage f:
    # group base:
    #     attribute base default

    group pose:
        attribute 01:#table_default default:
            "images/characters/felix/f01.png"
        attribute 02:#table_write:
            "images/characters/felix/f02.png"
        attribute 03:#table_panic:
            "images/characters/felix/f03.png"
        attribute 04:#table_think:
            "images/characters/felix/f04.png"
        attribute 05:#table_point:
            "images/characters/felix/f05.png"
        attribute f02_fire: #table_fire:
            "images/characters/felix/f02_fire.png"
        
        attribute 06:#write:
            "images/characters/felix/f06.png"
        attribute 07:#think:
            "images/characters/felix/f07.png"
        attribute 08:#crossed default:
            "images/characters/felix/f08.png"
        attribute 11:#crossed_shy:
            "images/characters/felix/f11.png"
        attribute 12:#crossed_away:
            "images/characters/felix/f12.png"
        attribute 13:#crossed_shock:
            "images/characters/felix/f13.png"
        attribute 22:#crossed_angry:
            "images/characters/felix/f22.png"
        attribute 24:#crossed_smile:
            "images/characters/felix/f24.png"
        attribute 25:#crossed_laugh:
            "images/characters/felix/f25.png"
        
        attribute 09:#relax:
            "images/characters/felix/f09.png"
        attribute 10:#scared:
            "images/characters/felix/f10.png"
        attribute 14:#angry:
            "images/characters/felix/f14.png"
        attribute 15:#scold:
            "images/characters/felix/f15.png"
        attribute 16:#angry_leave:
            "images/characters/felix/f16.png"
        attribute 17:#horror:
            "images/characters/felix/f17.png"
        attribute 18:#terror:
            "images/characters/felix/f18.png"
        attribute 19:#tired:
            "images/characters/felix/f19.png"
        attribute 20:#glasses:
            "images/characters/felix/f20.png"
        attribute 21:#hands:
            "images/characters/felix/f21.png"
        attribute 23:#caught:
            "images/characters/felix/f23.png"

layeredimage k:
    # group base:
    #     attribute base default

    group pose:
        attribute 01:#look_around:
            "images/characters/clementine/k01.png"
        attribute 14:#look_eyes:
            "images/characters/clementine/k14.png"
        attribute 15:#look_laugh:
            "images/characters/clementine/k15.png"
        attribute 23:#look_angry:
            "images/characters/clementine/k23.png"
        attribute 27:#look_bit:
            "images/characters/clementine/k27.png"
            
        attribute 02:#think default:
            "images/characters/clementine/k02.png"
        attribute 05:#point:
            "images/characters/clementine/k05.png"
        attribute 11:#cheek:
            "images/characters/clementine/k11.png"
        attribute 13:#cheek_laugh:
            "images/characters/clementine/k13.png"
            
        attribute 03:#confident:
            "images/characters/clementine/k03.png"
        attribute 04:#unhappy:
            "images/characters/clementine/k04.png"
        attribute 09:#watch:
            "images/characters/clementine/k09.png"
        attribute 16:#money:
            "images/characters/clementine/k16.png"
            
        attribute 06:#shy default:
            "images/characters/clementine/k06.png"
        attribute 12:#shy_smile:
            "images/characters/clementine/k12.png"
        attribute 06_cry:#shy_cry:
            "images/characters/clementine/k06_cry.png"
        attribute 06_letters:#shy_letters:
            "images/characters/clementine/k06_letters.png"
            
        attribute 07:#scared:
            "images/characters/clementine/k07.png"
        attribute 08:#power:
            "images/characters/clementine/k08.png"
            
        attribute 10:#leave:
            "images/characters/clementine/k10.png"
        attribute 24:#pull:
            "images/characters/clementine/k24.png"
            
        attribute 17:#broom_down:
            "images/characters/clementine/k17.png"
        attribute 18:#broom_wave:
            "images/characters/clementine/k18.png"
            
        attribute 20:#watch_you:
            "images/characters/clementine/k20.png"
        attribute 25:#catch:
            "images/characters/clementine/k25.png"
        attribute 26:#facepalm:
            "images/characters/clementine/k26.png"
            
        attribute 21:#laugh:
            "images/characters/clementine/k21.png"
        attribute 22:#fake_scared:
            "images/characters/clementine/k22.png"

layeredimage s:
    group base:
        attribute normal default:
            "images/characters/secretary/normal.png"
        attribute brow:
            "images/characters/secretary/brow.png"
