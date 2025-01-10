# Игра начинается здесь:
label start:

    scene bg room

    show f angry at left
    fe "test"

    show f angry at face_left, exit_left(3.0)
    fe "я ухожу медленно"

    call screen time_passed("На следующий день...")

    show f normal at face_left, enter_right(3.0)
    fe "я вернулся медленно"

    hide f
    fe "пропал"

    show f sad at face_left, enter_right(1)
    fe "я вернулся быстро"

    return
