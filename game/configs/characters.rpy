# Создаем анимацию для индикатора
image ctc_rotate:
    "gui/bubble.png"
    size (32, 32)
    anchor (0.5, 0.5)  # центр вращения
    alpha 1
    linear 2 alpha 0.6
    linear 2 alpha 1
    #rotate 0
    #linear 8.0 rotate 360
    repeat

define ctc_indicator = Animation("ctc_rotate")

image ctc_mind:
    "gui/ctc_mind.png"
    size (32, 32)
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

# Бандит 1

image b1:
    "images/characters/bandits/b1.png"

# Бандит 2

image b2:
    "images/characters/bandits/b2.png"

image fel_fire:
    "images/characters/felix/fire_01.png"
    pause 0.13
    "images/characters/felix/fire_02.png"
    pause 0.13
    "images/characters/felix/fire_03.png"
    pause 0.13
    repeat

image fel_table_fire:
    "images/characters/felix_table/fire_01.png"
    pause 0.13
    "images/characters/felix_table/fire_02.png"
    pause 0.13
    "images/characters/felix_table/fire_03.png"
    pause 0.13
    repeat

layeredimage fel_table:
    always:
        "images/characters/felix_table/gg_base.png"
    always:
        "fel_table_fire"

    group hands:
        attribute base_hands default:
            "images/characters/felix_table/gg_hands.png"
    
    group face:
        attribute base_face default:
            "images/characters/felix_table/gg_face_norm.png"

layeredimage fel:
    always:
        "images/characters/felix/gg_main.png"
    always:
        "fel_fire"

    group hands:
        attribute base_hands default:
            "images/characters/felix/gg_hands.png"
    
    group face:
        attribute base_face default:
            "images/characters/felix/gg_face_norm.png"

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

# Клементина
image k_composite_01 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_01.png",
    (0, 0), "images/characters/klem/k_01.png")

image k_composite_14 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_01.png",
    (0, 0), "images/characters/klem/k_02.png")

image k_composite_15 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_01.png",
    (0, 0), "images/characters/klem/k_03.png")

image k_composite_03 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_07.png",
    (0, 0), "images/characters/klem/k_04.png")

image k_composite_04 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_07.png",
    (0, 0), "images/characters/klem/k_05.png")

image k_composite_06 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_10.png",
    (0, 0), "images/characters/klem/k_06.png")

image k_composite_12 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_10.png",
    (0, 0), "images/characters/klem/k_07.png")

image k_composite_06_cry = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_10.png",
    (0, 0), "images/characters/klem/k_08.png")

image k_composite_06_letters = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_11.png",
    (0, 0), "images/characters/klem/k_06.png")

image k_composite_12_letters = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_11.png",
    (0, 0), "images/characters/klem/k_07.png")

image k_composite_21 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_07.png",
    (0, 0), "images/characters/klem/k_04.png")

image k_composite_28 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_16.png",
    (0, 0), "images/characters/klem/k_09.png")

image k_composite_29 = Composite((970, 1080),
    (0, 0), "images/characters/klem/k_b_17.png",
    (0, 0), "images/characters/klem/k_09.png")

layeredimage k:
    group pose:
        attribute 01:#look_around:
            "k_composite_01"
        attribute 14:#look_eyes:
            "k_composite_14"
        attribute 15:#look_laugh:
            "k_composite_15"
        attribute 23:#look_angry:
            "images/characters/klem/k_b_02.png"
            
        attribute 02:#think default:
            "images/characters/klem/k_b_03.png"
        attribute 05:#point:
            "images/characters/klem/k_b_04.png"
        attribute 11:#cheek:
            "images/characters/klem/k_b_05.png"
        attribute 13:#cheek_laugh:
            "images/characters/klem/k_b_06.png"
            
        attribute 03:#confident:
            "k_composite_03"
        attribute 04:#unhappy:
            "k_composite_04"

        attribute 09:#watch:
            "images/characters/klem/k_b_08.png"
        attribute 16:#money:
            "images/characters/klem/k_b_09.png"
            
        attribute 06:#shy default:
            "k_composite_06"
        attribute 12:#shy_smile:
            "k_composite_12"
        attribute 06_cry:#shy_cry: #найти где использовать
            "k_composite_06_cry"
        attribute 06_letters:#shy_letters: #найти где использовать
            "k_composite_06_letters"

        attribute 12_letters:# #найти где использовать
            "k_composite_12_letters"
            
        attribute 07:#scared: # не нарисованны
            "images/characters/klem/k07.png"
        attribute 08:#power: # не нарисованны
            "images/characters/klem/k08.png"
            
        attribute 10:#leave:
            "images/characters/klem/k_b_12.png"
        attribute 24:#pull:
            "images/characters/klem/k_b_12.png"
            
        attribute 17:#broom_down:
            "images/characters/klem/k_b_13.png"
        attribute 18:#broom_wave:
            "images/characters/klem/k_b_14.png"
            
        attribute 20:#watch_you:
            "images/characters/klem/k20.png" #не нарисованны
        attribute 25:#catch:
            "images/characters/klem/k25.png" # не нарисованны
        attribute 26:#facepalm:
            "images/characters/klem/k_b_15.png"
            
        attribute 21:#laugh:
            "k_composite_21"

        attribute 28:#laugh:
            "k_composite_28"
        attribute 29:#laugh:
            "k_composite_29"

# Секретарь

layeredimage s:
    group base:
        attribute normal default:
            "images/characters/secretary/normal.png"
        attribute brow:
            "images/characters/secretary/brow.png"
