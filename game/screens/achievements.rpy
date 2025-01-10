init -2 python:
    # Версия системы достижений
    ACHIEVEMENTS_VERSION = 1

    # Проверка версии и сброс при необходимости
    if not hasattr(persistent, '_achievements_version') or persistent._achievements_version != ACHIEVEMENTS_VERSION:
        persistent._achievements_version = ACHIEVEMENTS_VERSION
        persistent._achievement_unlocked = {}

init -1 python:
    # Инициализация persistent для достижений
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
            "Начните свое приключение",
            False,
            "images/achievements/achievement.png"
        ),
        "kish": Achievement(
            "kish",
            "Фанат Король и Шут",
            "Послушайте все треки Короля и Шута"
        ),
        "camera_pro": Achievement(
            "camera_pro",
            "Режиссёр",
            "Попробуйте все эффекты камеры"
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

# Экран достижений
screen achievements_screen():
    tag menu
    
    use game_menu(_("Достижения"), scroll="viewport"):
        
        vbox:
            spacing 10
            
            # Статистика достижений
            frame:
                style "achievements_stats_frame"
                
                python:
                    total = len(achievements)
                    unlocked = sum(1 for ach in achievements.values() if ach.unlocked)
                    percentage = (unlocked * 100) // total
                
                vbox:
                    spacing 10
                    xfill True
                    
                    text "Прогресс достижений: [unlocked]/[total] ([percentage]%)" style "achievements_stats_text"
                    
                    bar:
                        value percentage
                        range 100
                        xfill True
                        style "achievements_progress_bar"
            
            # Группируем достижения
            python:
                unlocked_achievements = [ach for ach in achievements.values() if ach.unlocked]
                locked_achievements = [ach for ach in achievements.values() if not ach.unlocked]

            if unlocked_achievements:
                text "Полученные достижения:" style "achievements_group_header"
                
                for ach in unlocked_achievements:
                    frame:
                        style "achievement_item_frame"
                        
                        hbox:
                            spacing 10
                            xfill True
                            
                            frame:
                                style "achievement_icon_frame"
                                xsize ACHIEVEMENT_ICON_SIZE + 20
                                ysize ACHIEVEMENT_ICON_SIZE + 20
                                
                                add ach.icon:
                                    size (ACHIEVEMENT_ICON_SIZE, ACHIEVEMENT_ICON_SIZE)
                                    fit "contain"
                                    xalign 0.5
                                    yalign 0.5
                            
                            vbox:
                                spacing 5
                                xfill True
                                hbox:
                                    spacing 5
                                    text ach.name style "achievement_name"
                                    text "✓" style "achievement_check"
                                text ach.description style "achievement_description"

            if locked_achievements:
                text "Неполученные достижения:" style "achievements_group_header"
                
                for ach in locked_achievements:
                    frame:
                        style "achievement_item_frame"
                        
                        hbox:
                            spacing 10
                            xfill True
                            
                            frame:
                                style "achievement_icon_frame"
                                xsize ACHIEVEMENT_ICON_SIZE + 20
                                ysize ACHIEVEMENT_ICON_SIZE + 20
                                
                                add ach.gray_icon:
                                    size (ACHIEVEMENT_ICON_SIZE, ACHIEVEMENT_ICON_SIZE)
                                    fit "contain"
                                    xalign 0.5
                                    yalign 0.5
                            
                            vbox:
                                spacing 5
                                xfill True
                                if ach.hidden:
                                    text "???" style "achievement_name"
                                    text "Секретное достижение" style "achievement_description"
                                else:
                                    text ach.name style "achievement_name"
                                    text ach.description style "achievement_description"

style achievements_stats_frame:
    background Frame("gui/frame.png", 40, 40)
    padding (20, 20)
    margin (0, 0, 0, 20)
    xfill True

style achievements_stats_text:
    color "#fff"
    size 24
    xalign 0.5
    text_align 0.5

style achievements_progress_bar:
    ysize 20
    left_bar Frame("gui/slider/horizontal_hover_bar.png", 10, 10)
    right_bar Frame("gui/slider/horizontal_idle_bar.png", 10, 10)
    thumb None
    thumb_offset 0
    xalign 0.5

style achievement_item_frame:
    background Frame("gui/frame.png", 40, 40)
    padding (20, 20)
    xfill True
    margin (0, 0, 0, 10)
    
style achievement_name:
    color "#fff"
    size 24

style achievement_description:
    color "#aaa"
    size 18

style achievements_group_header:
    size 36
    color "#fff"
    outlines [(2, "#000", 0, 0)]
    padding (0, 20, 0, 10)

style achievement_popup_frame:
    xalign 1.0
    yalign 0.0
    xsize 400
    background Frame("gui/frame.png", 40, 40)
    padding (10, 10)

style achievement_popup_title:
    color "#0f0"
    size 20

style achievement_popup_name:
    color "#fff"
    size 24

style achievement_popup_description:
    color "#aaa"
    size 18

style achievement_icon_frame:
    background Frame("gui/frame.png", 10, 10)
    padding (0, 0)
    margin (0, 0)

style achievement_icon:
    xalign 0.5
    yalign 0.5

style achievement_check:
    color "#0f0"
    size 30
    yoffset -5

# Экран всплывающего уведомления о достижении
screen achievement_popup(achievement):
    modal False
    zorder 100
    style_prefix "achievement_popup"
    
    timer 6 action Hide("achievement_popup")
    
    frame:
        at achievement_popup_appear
        style "achievement_popup_frame"
        xalign 1.0
        yalign 0.5
        xsize 400
        
        hbox:
            spacing 10
            
            frame:
                style "achievement_icon_frame"
                xsize ACHIEVEMENT_POPUP_ICON_SIZE
                ysize ACHIEVEMENT_POPUP_ICON_SIZE
                
                add achievement.icon:
                    size (ACHIEVEMENT_POPUP_ICON_SIZE, ACHIEVEMENT_POPUP_ICON_SIZE)
                    fit "contain"
                    xalign 0.5
                    yalign 0.5
            
            vbox:
                spacing 5
                text "Достижение разблокировано!" style "achievement_popup_title"
                text achievement.name style "achievement_popup_name"
                text achievement.description style "achievement_popup_description"

# Анимация появления уведомления
transform achievement_popup_appear:
    xoffset 400  # Начинаем за пределами экрана
    alpha 0.0    # Полностью прозрачный
    parallel:
        easein 0.5 xoffset 0  # Выезжаем
    parallel:
        easein 0.5 alpha 1.0  # Появляемся
    pause 4                 # Ждем
    parallel:
        easeout 0.5 xoffset 400  # Уезжаем
    parallel:
        easeout 0.5 alpha 0.0    # Исчезаем
