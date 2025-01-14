define POS_1 = (928, 126)
define POS_2 = (709, 434)
define POS_3 = (875, 914)
define POS_4 = (1176, 918)
define POS_5 = (1319, 437)
define POS_6 = (1204, 51)
define POS_7 = (590, 37)
define POS_8 = (417, 409)
define POS_9 = (564, 900)
define POS_10 = (1501, 930)
define POS_11 = (1636, 481)
define POS_12 = (1500, 77)
define POS_13 = (296, 44)
define POS_14 = (102, 411)
define POS_15 = (277, 870)
define POS_16 = (1787, 918)
define POS_17 = (1907, 432)
define POS_18 = (1811, 37)
define POS_19 = (20, 51)

define POS_FINAL = (1046, 520)

# Скорости анимации
define SLOW_MOVE_DURATION = 3.0   # Медленное движение
define FINAL_RUSH_DURATION = 0.1  # Финальный рывок
define WAVE_AMPLITUDE = 5         # Амплитуда волнообразного движения

define ALPHA_IN_TIME = 0.3

image bg_houses = "images/horror/horror_bg.png"

image b_fire:
    xanchor 0.5
    yanchor 0.5
    block:
        "images/horror/b_fire_1.png"
        pause 0.15 + renpy.random.random() * 0.1
        "images/horror/b_fire_2.png"
        pause 0.15 + renpy.random.random() * 0.1
        repeat

image r_fire:
    xanchor 0.5
    yanchor 0.5
    block:
        "images/horror/r_fire_1.png"
        pause 0.15 + renpy.random.random() * 0.1
        "images/horror/r_fire_2.png"
        pause 0.15 + renpy.random.random() * 0.1
        repeat

transform shake(force = 1):
    zoom 1
    block:
        linear 0.2 * force zoom 1.1
        linear 0.2 * force zoom 1
        repeat

transform at_pos(xpos, ypos):
    xpos xpos
    ypos ypos

transform move_to_final(start_x, start_y, mid_x, mid_y):
    parallel:
        ease SLOW_MOVE_DURATION xpos mid_x ypos mid_y
        pause 2
        ease FINAL_RUSH_DURATION xpos POS_FINAL[0] ypos POS_FINAL[1]
    parallel:
        ease 0.5 yoffset WAVE_AMPLITUDE
        ease 0.5 yoffset -WAVE_AMPLITUDE
        repeat (int(SLOW_MOVE_DURATION * 2))
        ease 0.1 yoffset 0

transform big_text:
    xalign 0.5 yalign 0.5
    zoom 3.0

init python:
    def calc_sub_point(start_x, start_y):
        mid_x = int(start_x + (POS_FINAL[0] - start_x) / 3)
        mid_y = int(start_y + (POS_FINAL[1] - start_y) / 3)
        return (mid_x, mid_y)

label horror_scene:
    $ _skipping = False
    
    scene bg_houses:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        zoom 1.2
        linear 2.0 zoom 1
    
    $ renpy.pause(2.0, hard=True)
    
    # Синий огонь
    show b_fire at alpha_in(0.5):
        xpos POS_FINAL[0] ypos POS_FINAL[1]
    
    $ renpy.pause(2.0, hard=True)
    
    # Красные
    show r_fire at alpha_in(ALPHA_IN_TIME), at_pos(POS_1[0], POS_1[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r2 at alpha_in(ALPHA_IN_TIME), at_pos(POS_2[0], POS_2[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r3 at alpha_in(ALPHA_IN_TIME), at_pos(POS_3[0], POS_3[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r4 at alpha_in(ALPHA_IN_TIME), at_pos(POS_4[0], POS_4[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r5 at alpha_in(ALPHA_IN_TIME), at_pos(POS_5[0], POS_5[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r6 at alpha_in(ALPHA_IN_TIME), at_pos(POS_6[0], POS_6[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r7 at alpha_in(ALPHA_IN_TIME), at_pos(POS_7[0], POS_7[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r8 at alpha_in(ALPHA_IN_TIME), at_pos(POS_8[0], POS_8[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r9 at alpha_in(ALPHA_IN_TIME), at_pos(POS_9[0], POS_9[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r10 at alpha_in(ALPHA_IN_TIME), at_pos(POS_10[0], POS_10[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r11 at alpha_in(ALPHA_IN_TIME), at_pos(POS_11[0], POS_11[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r12 at alpha_in(ALPHA_IN_TIME), at_pos(POS_12[0], POS_12[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r13 at alpha_in(ALPHA_IN_TIME), at_pos(POS_13[0], POS_13[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r14 at alpha_in(ALPHA_IN_TIME), at_pos(POS_14[0], POS_14[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r15 at alpha_in(ALPHA_IN_TIME), at_pos(POS_15[0], POS_15[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r16 at alpha_in(ALPHA_IN_TIME), at_pos(POS_16[0], POS_16[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r17 at alpha_in(ALPHA_IN_TIME), at_pos(POS_17[0], POS_17[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r18 at alpha_in(ALPHA_IN_TIME), at_pos(POS_18[0], POS_18[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    show r_fire as r19 at alpha_in(ALPHA_IN_TIME), at_pos(POS_19[0], POS_19[1])
    $ renpy.pause(ALPHA_IN_TIME, hard=True)
    
    # Начало тряски
    show b_fire at shake
    
    # Движение к центру
    python:
        mid1 = calc_sub_point(POS_1[0], POS_1[1])
        mid2 = calc_sub_point(POS_2[0], POS_2[1])
        mid3 = calc_sub_point(POS_3[0], POS_3[1])
        mid4 = calc_sub_point(POS_4[0], POS_4[1])
        mid5 = calc_sub_point(POS_5[0], POS_5[1])
        mid6 = calc_sub_point(POS_6[0], POS_6[1])
        mid7 = calc_sub_point(POS_7[0], POS_7[1])
        mid8 = calc_sub_point(POS_8[0], POS_8[1])
        mid9 = calc_sub_point(POS_9[0], POS_9[1])
        mid10 = calc_sub_point(POS_10[0], POS_10[1])
        mid11 = calc_sub_point(POS_11[0], POS_11[1])
        mid12 = calc_sub_point(POS_12[0], POS_12[1])
        mid13 = calc_sub_point(POS_13[0], POS_13[1])
        mid14 = calc_sub_point(POS_14[0], POS_14[1])
        mid15 = calc_sub_point(POS_15[0], POS_15[1])
        mid16 = calc_sub_point(POS_16[0], POS_16[1])
        mid17 = calc_sub_point(POS_17[0], POS_17[1])
        mid18 = calc_sub_point(POS_18[0], POS_18[1])
        mid19 = calc_sub_point(POS_19[0], POS_19[1])

    show r_fire at move_to_final(POS_1[0], POS_1[1], mid1[0], mid1[1])
    show r_fire as r2 at move_to_final(POS_2[0], POS_2[1], mid2[0], mid2[1])
    show r_fire as r3 at move_to_final(POS_3[0], POS_3[1], mid3[0], mid3[1])
    show r_fire as r4 at move_to_final(POS_4[0], POS_4[1], mid4[0], mid4[1])
    show r_fire as r5 at move_to_final(POS_5[0], POS_5[1], mid5[0], mid5[1])
    show r_fire as r6 at move_to_final(POS_6[0], POS_6[1], mid6[0], mid6[1])
    show r_fire as r7 at move_to_final(POS_7[0], POS_7[1], mid7[0], mid7[1])
    show r_fire as r8 at move_to_final(POS_8[0], POS_8[1], mid8[0], mid8[1])
    show r_fire as r9 at move_to_final(POS_9[0], POS_9[1], mid9[0], mid9[1])
    show r_fire as r10 at move_to_final(POS_10[0], POS_10[1], mid10[0], mid10[1])
    show r_fire as r11 at move_to_final(POS_11[0], POS_11[1], mid11[0], mid11[1])
    show r_fire as r12 at move_to_final(POS_12[0], POS_12[1], mid12[0], mid12[1])
    show r_fire as r13 at move_to_final(POS_13[0], POS_13[1], mid13[0], mid13[1])
    show r_fire as r14 at move_to_final(POS_14[0], POS_14[1], mid14[0], mid14[1])
    show r_fire as r15 at move_to_final(POS_15[0], POS_15[1], mid15[0], mid15[1])
    show r_fire as r16 at move_to_final(POS_16[0], POS_16[1], mid16[0], mid16[1])
    show r_fire as r17 at move_to_final(POS_17[0], POS_17[1], mid17[0], mid17[1])
    show r_fire as r18 at move_to_final(POS_18[0], POS_18[1], mid18[0], mid18[1])
    show r_fire as r19 at move_to_final(POS_19[0], POS_19[1], mid19[0], mid19[1])

    $ renpy.pause(SLOW_MOVE_DURATION, hard=True)
    show b_fire at shake(2)
    
    $ renpy.pause(1.97, hard=True)
    
    scene black with Dissolve(0.1)
    $ renpy.pause(5.0, hard=True)
    
    return