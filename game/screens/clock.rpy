init python:
    import datetime

    def get_current_time():
        now = datetime.datetime.now()
        return now.hour, now.minute, now.second

## Экран с часами
screen real_clock():
    timer 0.1 action Function(renpy.restart_interaction) repeat True
    
    # Позиция часов
    $ clock_x = 1720
    $ clock_y = 200
    
    # Вычисляем углы для стрелок на основе текущего времени
    $ hour, minute, second = get_current_time()
    
    # Углы для всех стрелок (0 = вверх, 90 = вправо, 180 = вниз, 270 = влево)
    $ hour_angle = -90 + (360 * ((hour % 12) + minute / 60.0) / 12)
    $ minute_angle = -90 + (360 * (minute + second / 60.0) / 60)
    $ second_angle = -90 + (360 * second / 60)
    
    # фон
    add "gui/clock/bg.png" xpos clock_x ypos clock_y xanchor 0.5 yanchor 0.5 at clock_style

    # стрелки
    add "gui/clock/sec.png" xpos clock_x ypos clock_y xanchor 0.5 yanchor 0.5 rotate second_angle at clock_style
    add "gui/clock/min.png" xpos clock_x ypos clock_y xanchor 0.5 yanchor 0.5 rotate minute_angle at clock_style
    add "gui/clock/hour.png" xpos clock_x ypos clock_y xanchor 0.5 yanchor 0.5 rotate hour_angle at clock_style

transform clock_style:
    zoom 0.5
