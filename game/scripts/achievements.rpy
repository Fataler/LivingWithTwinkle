init -2 python:
    # Версия системы достижений
    ACHIEVEMENTS_VERSION = 1

    # Проверка версии и сброс при необходимости
    if not hasattr(persistent, '_achievements_version') or persistent._achievements_version != ACHIEVEMENTS_VERSION:
        persistent._achievements_version = ACHIEVEMENTS_VERSION
        persistent._achievement_unlocked = {}

init -1 python:
    if not hasattr(persistent, '_achievement_unlocked'):
        persistent._achievement_unlocked = {}
    elif persistent._achievement_unlocked is None:
        persistent._achievement_unlocked = {}

init python:
    class Achievement(object):
        def __init__(self, id, name, description, hidden=False, icon="images/achievements/achievement.png"):
            self.id = id
            self.name = name
            self.description = description
            self.hidden = hidden
            self.icon = icon
            
            # Создаем серую версию иконки при инициализации
            self.gray_icon = Transform(self.icon, matrixcolor=SaturationMatrix(0.0))
            
        @property
        def unlocked(self):
            return self.id in persistent._achievement_unlocked and persistent._achievement_unlocked[self.id]
            
        def unlock(self):
            if not self.unlocked:
                # Сохраняем состояние в persistent
                persistent._achievement_unlocked[self.id] = True
                renpy.play(sfx_ui_achieve, channel="ui")
                # Показываем нотификацию
                renpy.show_screen("achievement_popup", achievement=self)
                renpy.restart_interaction()

    ACHIEVEMENT_ICON_SIZE = 96
    ACHIEVEMENT_POPUP_ICON_SIZE = 64

    # ID достижений
    FIRST_STEPS = "first_steps"
    WOLF_HUNTER = "wolf_hunter"
    PIPE_MASTER = "pipe_master"
    FIRST_CHAPTER = "first_chapter"
    SECOND_CHAPTER = "second_chapter"
    GAME_COMPLETED = "game_completed"
    THANK_YOU = "thank_you"
    HOLD_THE_DOOR = "hold_the_door"

    # Список достижений
    achievements = {
        FIRST_STEPS: Achievement(
            FIRST_STEPS,
            "Первые шаги",
            "Добро пожаловать в игру!",
            False,
            "images/achievements/achievement.png"
        ),
        # WOLF_HUNTER: Achievement(
        #     WOLF_HUNTER,
        #     "Логово найдено",
        #     "Найдите логово собирателя волчьих хвостов",
        #     False,
        #     icon="images/achievements/wolf.png"
        # ),
        FIRST_CHAPTER: Achievement(
            FIRST_CHAPTER,
            "Первая глава",
            "Прочтите первую главу",
            False
        ),
        SECOND_CHAPTER: Achievement(
            SECOND_CHAPTER,
            "Вторая глава",
            "Прочтите вторую главу",
            False
        ),
        GAME_COMPLETED: Achievement(
            GAME_COMPLETED,
            "Третья глава",
            "Пройдите всю игру",
            False
        ),
        THANK_YOU: Achievement(
            THANK_YOU,
            "Посетить \"Об игре\"",
            "Спасибо за проявленный интерес!",
            True
        ),
        PIPE_MASTER: Achievement(
            PIPE_MASTER,
            "Марио?",
            "Самостоятельно разберитесь с трубами",
            True
        ),
        HOLD_THE_DOOR: Achievement(
            HOLD_THE_DOOR,
            "Затворник",
            "Игнорируйте Клем до последнего",
            True
        )
    }

    def unlock_achievement(id):
        if id in achievements:
            achievements[id].unlock()
            
    def reset_achievements():
        """Сброс всех достижений"""
        persistent._achievement_unlocked.clear()
        renpy.save_persistent()
        renpy.restart_interaction()