#images 

## Определения фоновых изображений
image bg_bashnya   = "images/bg/bashnya.png"
image bg_vhod      = "images/bg/vhod.png"
image bg_koridor   = "images/bg/koridor.png"
image bg_podval    = "images/bg/podval.png"
image bg_kabinet   = "images/bg/kabinet.png"
image bg_hall      = "images/bg/hall.png"
image bg_ptichnik  = "images/bg/Ptici_1.png"
image bg_ptichnik2 = "images/bg/Ptici_2.png"
image bg_pereulok  = "images/bg/pereulok.png"
image bg_krishi    = "images/bg/krishi.png"

image cg_1         = "images/cg_1.png"
image cg_2         = "images/cg_2.png"

image bg_bashnya_arrow:
    "images/bg/clock_arrow_1.png"
    xanchor 1.0
    yanchor 1.0

image kabinet_table:
    "images/bg/table.png"

## Общие изображения
image bg_black = Solid("#000")
image bg_white = Solid("#fff")

image bg_black_t_10 = Solid("#0000001a")
image bg_black_t_20 = Solid("#00000033")
image bg_black_t_30 = Solid("#0000004d")
image bg_black_t_40 = Solid("#00000066")
image bg_black_t_50 = Solid("#00000080")
image bg_black_t_60 = Solid("#00000099")
image bg_black_t_70 = Solid("#000000b3")
image bg_black_t_80 = Solid("#000000cc")
image bg_black_t_90 = Solid("#000000e6")

image d1 = "images/d1.png"

image menu_drop:
    "gui/menu_drop.png"
    xanchor 0
    yanchor 0

image screen_board:
    "gui/game_screen_drop.png"
    xanchor 0
    yanchor 0

## Эффекты
transform darken:
    matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

transform lighten:
    matrixcolor TintMatrix("#ffffff") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное затемнение
transform fade_to_dark:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)

# Анимированное осветление
transform fade_to_light:
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.7)
    linear 1.0 matrixcolor TintMatrix("#000000") * ColorMatrix(1.0, 1.0, 1.0, 0.0)

# Цветные заглушки для титров
image credits_img_1 = "images/credits/c1.png" # Красный
image credits_img_2 = "images/credits/c2.png" # Зеленый
image credits_img_3 = "images/credits/c3.png" # Синий
image credits_img_4 = "images/credits/c4.jpg" # Желтый

image paket_f = "images/characters/felix/m_1.png"
image paket_k = "images/characters/felix/m_2.png"


layeredimage letter:
    group postion:
        attribute 07:
            "images/characters/felix/p_f07.png"
        attribute 08:
            "images/characters/felix/p_f08.png"
        attribute 11:
            "images/characters/felix/p_f08.png"
        attribute 22:
            "images/characters/felix/p_f08.png"
        attribute 10:
            "images/characters/felix/p_f10.png"
        attribute 14:
            "images/characters/felix/p_f10.png"
        attribute 17:
            "images/characters/felix/p_f17.png"
        attribute 19:
            "images/characters/felix/p_f17.png"
        attribute 21:
            "images/characters/felix/p_f21.png"