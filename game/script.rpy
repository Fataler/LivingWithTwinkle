# Игра начинается здесь:
label start:

    # menu:
    #     "Трубы":
    #         jump test_pipe_game
    #     "Cюжет":
    #         jump chapter1
    
    scene bg room

    show f normal glass at left
    F "Он шел{w}, шел{w}, шел... В своих крутых очках"

    show f normal base at face_left, exit_left(3.0)
    F "Сняв очки, я ухожу медленно"

    #call screen time_passed("На следующий день...")

    show f normal cat at face_left, enter_right(3.0)
    F "я вернулся c котом"

    hide f
    F "пропал"

    show f sad at face_left, enter_right(1)
    F "я вернулся быстро"

    return
