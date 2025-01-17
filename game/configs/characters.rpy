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


image fel_fire_fast:
    "images/characters/felix/fire_01.png"
    pause 0.06
    "images/characters/felix/fire_02.png"
    pause 0.06
    "images/characters/felix/fire_03.png"
    pause 0.06
    repeat

image fel_table_fire:
    "images/characters/felix/table_fire_01.png"
    pause 0.13
    "images/characters/felix/table_fire_02.png"
    pause 0.13
    "images/characters/felix/table_fire_03.png"
    pause 0.13
    repeat

image fel_fire_long:
    "images/characters/felix/fo2_1.png"
    pause 0.13
    "images/characters/felix/fo2_2.png"
    pause 0.13
    "images/characters/felix/fo2_3.png"
    pause 0.13
    repeat

# Композитные изображения для fel_table
image fel_table_composite_01 = Composite((970, 1080),
    (0, 0), "images/characters/felix/f_l_15.png",
    (0, 0), "images/characters/felix/f_l_19.png")

image fel_table_composite_02 = Composite((970, 1080),
    (0, 0), "images/characters/felix/f_r_8.png",
    (0, 0), "images/characters/felix/f_l_16.png")

image fel_table_composite_03 = Composite((970, 1080),
    (0, 0), "images/characters/felix/f_r_8.png",
    (0, 0), "images/characters/felix/f_l_17.png")

image fel_table_composite_03_fire = Composite((970, 1080),
    (0, 0), "images/characters/felix/f_r_8.png",
    (0, 0), "images/characters/felix/f_l_18.png")

image fel_table_composite_04 = Composite((970, 1080),
    (0, 0), "images/characters/felix/f_r_9.png",
    (0, 0), "images/characters/felix/f_l_16.png")

image fel_table_composite_05 = Composite((970, 1080),
    (0, 0), "images/characters/felix/f_r_9.png",
    (0, 0), "images/characters/felix/f_l_16.png")

layeredimage fel_table:
    always:
        "images/characters/felix/f_b_2.png"

    group pose:
        attribute 01: #write
            "fel_table_composite_01"
        attribute 02:
            "fel_table_composite_02"
        attribute 03:
            "fel_table_composite_03"
        attribute 03_fire:
            "fel_table_composite_03_fire"
        attribute 04:
            "fel_table_composite_04"
        attribute 05:
            "fel_table_composite_05"
    
    group head:
        attribute head_base default:
            "fel_table_fire"
        attribute hat:
            "images/characters/felix/gg_hat_table.png"

# layeredimage fel:
#     always:
#         "images/characters/felix/gg_main.png"
#     always:
#         "fel_fire"

#     group hands:
#         attribute base_hands default:
#             "images/characters/felix/gg_hands.png"
    
#     group face:
#         attribute base_face default:
#             "images/characters/felix/gg_face_norm.png"

# изображения для Феликса
image f_composite_06 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_1.png",
    (0, 0), "images/characters/felix/f_l_1.png")

image f_composite_07 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_2.png",
    (0, 0), "images/characters/felix/f_l_1.png")

image f_composite_08 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_2.png")

image f_composite_11 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_3.png")

image f_composite_12 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_4.png")

image f_composite_13 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_5.png")

image f_composite_22 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_6.png")

image f_composite_24 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_7.png")

image f_composite_25 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_3.png",
    (0, 0), "images/characters/felix/f_l_8.png")

image f_composite_10 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_4.png",
    (0, 0), "images/characters/felix/f_l_9.png")

image f_composite_14 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_4.png",
    (0, 0), "images/characters/felix/f_l_10.png")

image f_composite_16 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_5.png",
    (0, 0), "images/characters/felix/f_l_6.png")

image f_composite_17 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_5.png",
    (0, 0), "images/characters/felix/f_l_11.png")

image f_composite_18 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_5.png",
    (0, 0), "images/characters/felix/f_l_12.png")

image f_composite_19 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_5.png",
    (0, 0), "images/characters/felix/f_l_13.png")

image f_composite_21 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_6.png",
    (0, 0), "images/characters/felix/f_l_14.png")

image f_composite_23 = Composite((750, 1080),
    (0, 0), "images/characters/felix/f_r_7.png",
    (0, 0), "images/characters/felix/f_l_5.png")

layeredimage f:
    always:
        "images/characters/felix/f_b_1.png"
    # always:
    #     "fel_fire"

    group pose:
        # attribute 01:#table_default default:
        #     "images/characters/felix/f01.png"
        # attribute 02:#table_write:
        #     "images/characters/felix/f02.png"
        # attribute 03:#table_panic:
        #     "images/characters/felix/f03.png"
        # attribute 04:#table_think:
        #     "images/characters/felix/f04.png"
        # attribute 05:#table_point:
        #     "images/characters/felix/f05.png"
        attribute f02_fire: #table_fire:
            "images/characters/felix/f02_fire.png"
        
        attribute 06:#write:
            "f_composite_06"
        attribute 07:#think:
            "f_composite_07"
        attribute 08:#crossed default:
            "f_composite_08"
        attribute 11:#crossed_shy:
            "f_composite_11"
        attribute 12:#crossed_away:
            "f_composite_12"
        attribute 13:#crossed_shock:
            "f_composite_13"
        attribute 22:#crossed_angry:
            "f_composite_22"
        attribute 24:#crossed_smile:
            "f_composite_24"
        attribute 25:#crossed_laugh:
            "f_composite_25"
        
        # attribute 09:#relax:
        #     "images/characters/felix/f09.png"
        attribute 10:#scared:
            "f_composite_10"
        attribute 14:#angry:
            "f_composite_14"
        # attribute 15:#scold:
        #     "images/characters/felix/f15.png"
        attribute 16:#angry_leave:
            "f_composite_16"
        attribute 17:#horror:
            "f_composite_17"
        attribute 18:#terror:
            "f_composite_18"
        attribute 19:#tired:
            "f_composite_19"
        # attribute 20:#glasses:
        #     "images/characters/felix/f20.png"
        attribute 21:#hands:
            "f_composite_21"
        attribute 23:#caught:
            "f_composite_23"

    group head:
        attribute head_base default:
            "fel_fire"
        attribute hat:
            "images/characters/felix/gg_hat.png"
        attribute fire_fast:
            "fel_fire_fast"
        attribute bald:
            null
        attribute long_hair:
            "fel_fire_long"


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
            "images/characters/klem/k_b_18.png"
            
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

        attribute 28:#paper in fire:
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
