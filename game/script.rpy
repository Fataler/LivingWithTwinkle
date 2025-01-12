# Игра начинается здесь:
label start:

    # menu:
    #     "Трубы":
    #         jump test_pipe_game
    #     "Cюжет":
    #jump chapter1

    window hide
    #$ renpy.call_screen("credits")
    
    jump chapter1

    scene bg room

    show f normal glass at left
    F "Он шел{w}, шел{w}, шел... В своих крутых очках"

    show f normal base at face_left, exit_left(3.0)
    F "Сняв очки, я ухожу медленно"

    scene bg_white with Dissolve(1)
    #pause(1)
    #scene bg castle with Dissolve(1)
    show f normal cat at face_left, enter_right(3.0)
    F "я вернулся c котом"
    F "И прошел всю игру..."

    call screen credits

    return
