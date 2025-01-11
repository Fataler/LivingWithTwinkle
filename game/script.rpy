# Игра начинается здесь:
label start:

    jump test_pipe_game
    scene bg room

    show f normal at left
    F "Он шел{w}, шел{w}, шел..."

    show f angry at face_left, exit_left(3.0)
    F "я ухожу медленно"

    call screen time_passed("На следующий день...")

    show f normal at face_left, enter_right(3.0)
    F "я вернулся медленно"

    hide f
    F "пропал"

    show f sad at face_left, enter_right(1)
    F "я вернулся быстро"

    return
