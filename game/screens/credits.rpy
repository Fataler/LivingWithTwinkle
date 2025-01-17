init python:
    class Credits(renpy.Displayable):
        def __init__(self, content, duration=25.0):
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
            
            # скорость на основе общей длительности
            speed = (self.height) / self.duration
            
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

Команда:

{size=45}Разработчик{/size}
Руслан Кучеренко

{size=45}Сценарист{/size}
Zabava

{size=45}Дизайн мини игр{/size}
Инна Кучеренко

{size=45}Музыка{/size}
Remi

Отдельная благодарность:

Разработчица новелы "Инцелотред"
Редактура
Тестирование

{size=45}Коты Тигр и Лиса{/size}
Катание по клавиатуре
Громкое мяуканье
Моральная поддержка



Продолжение слудует...
""", duration=40.0)
    
    fixed:
        xfill True
        yfill True
        at show_screen_transform
        
        add "bg_black"
        
        # Картинки
        timer 2.0 action Show("credits_image", img_name="credits_img_1", is_left=True)
        timer 7 action Hide("credits_image")

        timer 8.0 action Show("credits_image", img_name="credits_img_2", is_left=False)
        timer 13 action Hide("credits_image")

        timer 14.0 action Show("credits_image", img_name="credits_img_3", is_left=True)
        timer 19 action Hide("credits_image")

        timer 20.0 action Show("credits_image", img_name="credits_img_4", is_left=False)
        timer 26.0 action Hide("credits_image")
        
        # Бегущий текст
        add credits_obj xalign 0.5

        if credits_obj.finished:
            timer 0.1 action Show("credits_end")
        
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
            $ xpos = 0.1 if is_left else 0.9
            $ trans = credits_left_appear if is_left else credits_right_appear
            add img_name at trans xalign xpos yalign 0.5 xsize 400 ysize 300

transform credits_left_appear:
    alpha 0.0 xoffset -50
    ease 3 alpha 1.0 xoffset 0

transform credits_right_appear:
    alpha 0.0 xoffset 50
    ease 3 alpha 1.0 xoffset 0
