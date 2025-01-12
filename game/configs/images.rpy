#images 

image bg_white = "#ffffff"
image bg_black = "#000000"

image zamok_top = "images/bg/zamok_top.png"
image zamok_vh = "images/bg/zamok_vh.png"
image zamok_mid_1 = At("images/bg/zamok_mid.png", Move((0, 1080), (0, 0), 0.5, repeat=True))
image zamok_mid_2 = At("images/bg/zamok_mid.png", Move((0, 0), (0, -1080), 0.5, repeat=True))

# Цветные заглушки для титров
image credits_img_1 = Solid("#FF0000")  # Красный
image credits_img_2 = Solid("#00FF00")  # Зеленый
image credits_img_3 = Solid("#0000FF")  # Синий
image credits_img_4 = Solid("#FFFF00")  # Желтый