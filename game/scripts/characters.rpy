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

# Определение персонажей
define fe = Character("Феликс", 
    what_prefix="\"",
    what_suffix="\"",
    ctc=ctc_indicator,      
    ctc_position="nestled",
    what_slow_cps=30,
    what_slow_abortable=False
)

define se = Character("Секретарь", 
    what_prefix="\"",
    what_suffix="\"",
    ctc=ctc_indicator,
    ctc_position="nestled",
    what_slow_cps=30,
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

# Определение изображений персонажа Феликса
layeredimage f:
    # Базовые состояния
    group state:
        attribute normal default:
            "images/characters/felix/normal.png"
        attribute angry:
            "images/characters/felix/angry.png"
        attribute sad:
            "images/characters/felix/sad.png"

#image f = Placeholder("boy")