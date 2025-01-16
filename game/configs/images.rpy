#images 

## Определения фоновых изображений
image bg_bashnya   = "images/bg/bashnya.png"
image bg_vhod      = "images/bg/vhod.jpg"
image bg_koridor   = "images/bg/koridor.jpg"
image bg_kabinet   = "images/bg/kabinet.png"
image bg_hall      = "images/bg/hall.jpg"
image bg_ptichnik  = "images/bg/golubi.png"
image bg_pereulok  = "images/bg/pereulok.png"
image bg_krishi    = "images/bg/krishi.jpg"

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
image credits_img_1 = Solid("#FF0000")  # Красный
image credits_img_2 = Solid("#00FF00")  # Зеленый
image credits_img_3 = Solid("#0000FF")  # Синий
image credits_img_4 = Solid("#FFFF00")  # Желтый