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
transform alice_blink:
    parametric_blink("images/sprites/alice/1.png", "images/sprites/alice/2.png")

# Определение спрайтов с помощью LayeredImage
layeredimage alice:
    group base:
        attribute base default at alice_blink
        attribute talking:
            "images/sprites/alice/normal.png"

#Определение изображений Феликса
layeredimage f:
    group pose:
        attribute normal default:
            "images/characters/felix/normal.png"
        attribute angry
        attribute sad

    group state:
        attribute base default:
            "images/characters/felix/normal.png"
        attribute glass:
            "images/characters/felix/glass.png"
        attribute cat:
            "images/characters/felix/cat.png"

    group if_angry:
        attribute base if_any "angry":
            "images/characters/felix/angry.png"
        attribute glass if_any "angry":
            "images/characters/felix/angry_talking.png"
        attribute cat if_any "angry":
            "images/characters/felix/angry_cat.png"

    group if_sad:
        attribute base if_any "sad":
            "images/characters/felix/sad.png"
        attribute glass if_any "sad":
            "images/characters/felix/sad_talking.png"
        attribute cat if_any "sad":
            "images/characters/felix/sad_angry.png"

# Клементина
layeredimage k:
    group pose:
        attribute normal

    group state:
        attribute base default:
            "images/characters/klem/normal.png"
        attribute shvabra:
            "images/characters/klem/shvabra_1.png"

# Секретарь
image s:
    "images/characters/secretary/normal.png"


# Бандит 1

image b1:
    "images/characters/bandits/b1.png"

# Бандит 2

image b2:
    "images/characters/bandits/b2.png"
