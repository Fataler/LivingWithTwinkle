#images 

## Определения фоновых изображений
image bg_bashnya = "images/bg/bashnya.jpg"
image bg_vhod = "images/bg/vhod.jpg"
image bg_koridor = "images/bg/koridor.jpg"
image bg_kabinet = "images/bg/kabinet.jpg"
image bg_hall = "images/bg/hall.jpg"
image bg_ptichnik = "images/bg/golubi.png"
image bg_pereulok = "images/bg/pereulok.jpg"
image bg_krishi = "images/bg/krishi.jpg"

## Общие изображения
image bg_black = Solid("#000")
image bg_white = Solid("#fff")

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