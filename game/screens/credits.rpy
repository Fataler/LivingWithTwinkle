define credits_duration = 60.0

init python:    
    class Credits(renpy.Displayable):
        def __init__(self, content, duration=credits_duration):
            super(Credits, self).__init__()
            self.content = content
            self.duration = duration
            self.height = 0
            self.time = 0
            self.finished = False
            
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            
            text = Text(self.content, text_align=0.5, size=35)
            text_render = renpy.render(text, width, height, st, at)
            
            self.height = text_render.height + height
            
            speed = (self.height + height) / (self.duration * 1.5)
            
            y = height - (st * speed)
            
            # фиксируем сли текст полностью ушел вверх
            if y < -text_render.height:
                self.finished = True
                y = -text_render.height 
                
            render.blit(text_render, (width//2 - text_render.width//2, y))
            
            if not self.finished:
                renpy.redraw(self, 0)
            return render

screen credits():
    modal True
    default credits_obj = Credits("""{size=65}Жизнь с огоньком{/size}

{size=65}Команда:{/size}



{size=45}Zabava{/size}

сценарий
фоны


{size=45}Zella{/size}

фоны
персонажи
CG


{size=45}Remi Prochet{/size}

музыка
звуки
тестирование


{size=45}Featharine{/size}

концепт персонажей
дизайн мини игр
персонажи
CG


{size=45}Fataler{/size}

оригинальная идея
код
мини игры
верстка
анимации

{size=45}HolieKay{/size}

дизайн UI




{size=65}Отдельная 
благодарность:{/size}

{size=45}Разработчица новелы 
"Инцелотред"{/size}

Редактура


{size=45}Коты Тигр и Лиса{/size}

катание по клавиатуре
моральная поддержка
тестирование





Продолжение слудует...
""")
    
    fixed:
        xfill True
        yfill True
        at show_screen_transform
        
        add "bg_black"
        
        # Картинки
        timer (credits_duration * 0.08) action Show("credits_image", img_name="credits_img_1", is_left=True)
        timer (credits_duration * 0.28) action Hide("credits_image")

        timer (credits_duration * 0.32) action Show("credits_image", img_name="credits_img_2", is_left=False)
        timer (credits_duration * 0.52) action Hide("credits_image")

        timer (credits_duration * 0.56) action Show("credits_image", img_name="credits_img_3", is_left=True)
        timer (credits_duration * 0.76) action Hide("credits_image")

        timer (credits_duration * 0.80) action Show("credits_image", img_name="credits_img_4", is_left=False)
        timer (credits_duration * 0.95) action Hide("credits_image")
        
        # Бегущий текст
        add credits_obj xalign 0.5

        timer credits_duration+5 action Show("credits_end")
        
        textbutton "Пропустить" action Return() xalign 0.95 yalign 0.05

screen credits_end():
    text "Спасибо за игру!" size 65 xalign 0.5 yalign 0.5 at credits_thanks
    timer 3.0 action Return()

transform credits_thanks:
    alpha 0.0
    ease 1.0 alpha 1.0

screen credits_image(img_name=None, is_left=True):
    fixed:
        xfill True
        yfill True
        at show_screen_transform
            
        if img_name:
            $ xpos = 0.01 if is_left else 0.99
            $ trans = credits_left_appear if is_left else credits_right_appear
            add img_name at trans xalign xpos yalign 0.5 xsize 640 ysize 360

transform credits_left_appear:
    alpha 0.0 xoffset -50
    ease 3 alpha 1.0 xoffset 0

transform credits_right_appear:
    alpha 0.0 xoffset 50
    ease 3 alpha 1.0 xoffset 0
