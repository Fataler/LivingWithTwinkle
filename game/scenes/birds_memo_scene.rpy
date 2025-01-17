image memo1 = "images/memo_1.png"
image memo2 = "images/memo_2.png"
image memo3 = "images/memo_3.png"

define memo_time = 3
define animation_time = 2

transform memo_transform:
    yanchor 0.5
    xanchor 0.5
    xalign 0.5
    yalign 0.5
    alpha 0
    yoffset 50
    zoom 0.9
    linear 1.0 alpha 1.0 zoom 1 yoffset 0 
    pause memo_time
    linear 1.0 alpha 0 zoom 0.9 yoffset -50 

label birds_memo_scene:

show bg_black_t_50 at alpha_in(1)

pause 1

show memo1 at memo_transform
pause memo_time + animation_time
hide memo1

show memo2 at memo_transform
pause memo_time + animation_time
hide memo2

show memo3 at memo_transform
pause memo_time + animation_time
hide memo3

show bg_black_t_50 at alpha_out(1)
pause 1
hide bg_black_t_50

return