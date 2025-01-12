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
                # Показываем нотификацию
                #renpy.play("audio/achievement.ogg", channel="sound")
                renpy.show_screen("achievement_popup", achievement=self)
                renpy.restart_interaction()

    ACHIEVEMENT_ICON_SIZE = 96  # размер иконки в списке (96x96 пикселей - стандартный размер для иконок достижений)
    ACHIEVEMENT_POPUP_ICON_SIZE = 64  # размер иконки в уведомлении (64x64 пикселя - компактнее для уведомления)

    # Список всех достижений
    achievements = {
        "first_steps": Achievement(
            "first_steps",
            "Первые шаги",
            "Добро пожаловать в игру!",
            False,
            "images/achievements/achievement.png"
        ),
        "kish": Achievement(
            "kish",
            "Фанат Король и Шут",
            "Послушайте все треки Короля и Шута"
        ),
        "wolf_hunter": Achievement(
            "wolf_hunter",
            "Логово найдено",
            "Найдите логово собирателя волчьих хвостов",
            False,
            icon = "images/achievements/wolf.png"
        ),
        "snake_master" : Achievement(
            "snake_master",
            "Игрок",
            "Наберите в змейке больше 5 очков",
        ),
        "secret_ending": Achievement(
            "secret_ending",
            "???",
            "Найдите секретную концовку",
            True
        )
    }

    def unlock_achievement(id):
        """Простая функция для разблокировки достижения по ID"""
        if id in achievements:
            achievements[id].unlock()
            
    def reset_achievements():
        """Сброс всех достижений"""
        persistent._achievement_unlocked.clear()
        renpy.save_persistent()
        renpy.restart_interaction()