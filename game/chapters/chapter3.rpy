label chapter3:
#Сцена 12.
###############################################################################

scene bg_black with Dissolve(1)
#f21 + шляпа

$ unlock_achievement("second_chapter")
call time_passed("15 минут спустя") from _call_time_passed_6
pause 1
show bg_hall
show f 21 hat at enter_c_left(4)
show paket_f at enter_c_left(4) 
with Dissolve(1)

play music music_hover
#Холл F и к появляются все в саже с птицами(ломом) в руках.
window show
F "Что только что произошло?"

#+ мешок под рукой
show k 11 at enter_c_right(4), flip
show paket_k at enter_c_right(4), flip

pause 4.0

show k 11 at c_right, flip
show paket_k at c_right, flip

K "Вы сделали хорошее дело. Тем идиотам давно пора было навалять."
F "Я спалил половину улицы, а потом, как вор, бежал через весь город…"
show paket_k
show k 02
#+ мешок под рукой
K "Да вы преувеличиваете. Почему вор? Вы же вернули своё."
F "Да, моё…"
F_m "А остальное не отрицает…"
#к выпрямляет руки, бросая птиц на пол.

hide paket_k
show k 03 at put_down(offset=-10)
#+ мешок вниз падает
F "Эй, ты что творишь?!"
#использует силу на себе, чтобы стереть сажу. Мб что-то типа облака из пены, что проходит по лицу.
show k 05 #flip
K "Они же сломаны. Потом всё равно почините."
F "Да, но… это как-то грубо."
#Подходит к Ф и использует на нём.
K "Не дёргайтесь."
#F тоже роняет птиц, пытаясь поднять руки
hide paket_f
show f 10 at put_down(offset=10)
F "Ай-ай-ай!"
show k 11 #flip
K "Да уже всё, я же аккуратно."
show f 14
F "Да как можно использовать способность на ком-то без спросу?!"
show k 14 #flip
K "А что такого? Я постоянно так делаю."
K "Помните нашу первую встречу?"
show f 14
show k 15 #flip
F "Да! Ты меня тогда чуть не убила!"
show k 05 #flip
K "Но не убила же."
show f 14
F "Ты мне больше зубы не заговоришь! Куда только смотрел Секретарь, когда нанимал тебя?!"
show k 02 #flip
K "Секретарь? Вы не знаете имени мужика, который на вас работает?"
F "Да, не знаю! И твоё не знаю! И мне всё равно! Я всегда остаюсь один!"
show k 14 #flip
K "А если я останусь с вами?"
show f 10
F "ЧТО?!"
show f 17
F_m "Я понял. {w} Это очередная её ложь. Никто не остается со мной. {w}Нет. Мне никто и не нужен."
show f 14
F "Зачем мне такая, как ты? Ты ужасно некомпетентная! Постоянно грубишь! Постоянно хватаешь меня…"
show k 15 #flip
K "Ага, продолжайте."
show f 21
F "А ещё… ещё…."
#холл начинает заполняться водой.
F "А ещё – это что такое?"
show k 12 #flip
K "Упси!"

stop music fadeout 2
#pause 2
#ё

#Сцена 13.
###############################################################################

scene bg_podval 
show f 22 hat:
    xpos -140
show k 06 at flip:
    xpos 1200
with Dissolve(2)
#котельная - игра?
play music music_trouble
F "Почему тут вода повсюду?"
F "Это точно ты устроила…"
K "Я ничего не делала!"
show k 12
K "Только прибралась немного… не знаю, как так получилось."
F "Почему-то я не удивлён."
default pipe_result = False
window hide
menu:
    "Чинить самой":
        K "Сейчас всё исправлю. Наверное…"
        $ pipe_result = renpy.call_screen("pipe_game")
        if pipe_result:
            "Ура! Получилось!"
            $unlock_achievement(PIPE_MASTER)
        else:
            "Никак не выходит! Давайте лучше вы..."
        jump ch14

    "Попросить помощи":
        K "Вы же в этом лучше разбираетесь. А я помогу!"
        jump ch14

label ch14:
window show
stop music fadeout 3
pause 1
show bg_black with Dissolve(2)
#Сцена 14.
###############################################################################
#scene bg_white with Dissolve(1)
#Коридор F и к медленно идут влево
scene bg_koridor
show f 22 hat at c_left, flip
show k 10 at c_right, flip
with Dissolve(1)
play music music_hover
$ renpy.block_rollback()
K "Не понимаю, чего вы так злитесь. Всё же хорошо закончилось."
K "Сами посудите, мы остановили потоп."
if pipe_result:
    F "Но ты сперва его и устроила"  # два ответа
else:
    F "Устроила ты, а останавливал – я." # два ответа

show k 14 #flip
K "Спасли ваших птиц."
F "Но я сжёг переулок…"
show k 05 #flip
K 'Ага, круто вышло! И те отбросы больше не подумают шутить с "хозяином вороньей башни".'
F "Как у тебя всё легко."
show k 01 #flip
K "Зато у вас – тяжело. Не надоело еще трястись, как заячий хвост?"
#останавливаются
show f 07 #flip
F "Надоело?"
F_m "Я так давно живу с этим, что, кажется, перестал задумываться."
F_m "Разве может надоесть привычное повседневное существование?"
show k 03 #flip
K "Почему бы вам не начать пользоваться своей силой?"
#F поворачивается к К
show f 08
F "Что ты имеешь в виду?"
K "Вы же просто боялись её до сих пор, разве нет?"
F_m "Хах?"
show f 22
F_m "Появилась тут меньше недели назад, и думает, что всё про меня знает?!"
#Поворачивается влево и идет дальше
show f 22 #flip
show k 10 #flip
F "Ты ничего обо мне не знаешь."
F "Так что перестань делать вид, что у тебя есть ответы на все вопросы."

show bg_black with Dissolve(2)
pause 2

#call time_passed("5 минут спустя") from _call_time_passed_7
# Сцена 15.
###############################################################################
#Ф22*
scene bg_kabinet 
show f 22 at enter_c_left(from_right=True), flip
with Dissolve(1)

play music music_hover
pause 1.0
show k 03 at enter_c_right, flip
#кабинет, сначала заходит Ф, потом К
K "Да послушайте меня."
K "Когда я была маленькой, от страха всегда икала пузырями."
show f 22 at flip, angry, c_left
F "Какое отношение это имеет ко мне и использованию силы?"
show k 02 #flip
K 'Я понаблюдала за вами, и, похоже, ваша способность непроизвольно "включается" от сильных эмоций.'
show k 03 #flip
K "Так вот. Просто перестаньте бояться – и всё пройдёт!"
show f 13 at flip, angry, c_left
F "Ты издеваешься надо мной?"
show k 05 #flip
K "У меня же прошло – вариант безотказный."
show f 12
F "Не смей сравнивать себя со мной!"
show k 04 #flip
F "Пара жалких пузырей и огонь, испепеляющий всё на своём пути, – у нас совершенно разные ситуации!"
F "Сколько себя помню, я боялся каждую секунду каждого дня!"
show f 22
F 'А теперь ты мне говоришь "просто перестать"?!'
K "Так, а чего вы боитесь?"
show f 14
F "Чего-чего, что превращусь в ходячую катастрофу!"
show k 01 #flip
K "Но за всё это время ничего так и не произошло."
show k 02 #flip
show f 14 at flip, angry, c_left
F "Да я только сегодня поджёг два дома и навредил людям!"
K "Да какое там, вы подожгли разве что пару прошлогодних листовок. А те скользкие типы всё равно улизнули до взрыва."
show k 05 #flip
K "Но должна признать, что смотрелось эпично, хоть и эффекта особо никакого."
show f 08 #flip
F "..."
F "Опять обращаешь всё в шутку. Чувства других для тебя – шутка?"
show k 06
K "Слушайте. Я правда не знаю, что у вас там случилось."
K "Но дерьмо в жизни случается у каждого. Не стройте из себя человека с самой печальной предысторией."
show k 23 #flip
K "Ну да, навредили вы кому-то. Но сколько лет назад это было?!"
K "Сколько ещё вы будете хоронить себя? Не пора ли простить себя?"
F_m "Простить?"
F_m "Заслуживаю ли я прощения?"
show k 04 #flip
K "А пофиг, не прощайте."
K "Кто я такая в конце концов – нищая оборванка с базара. Вы всегда сможете найти десять таких."
show f 12
F_m "Больше никогда не попрошу Секретаря нанимать мне кого-либо…"
K "Но скажите честно. Разве вам не было легче в последние дни?"
show f 13
F_m "Легче? Что она имеет в виду?"
F_m "Она же раздражала меня каждый раз, как открывала рот."
show k 05 #flip
K 'Сколько раз вместо пересчитывания возможных источников пожара вы пересчитывали процент моей "убийственности"?'
show f 11
F "Чего?"
show k 11 #flip
K "Да-да, я про вот эту вашу отдельную доску."
F "На то были основания – ты вела себя слишком подозрительно."
show k 14 #flip
K "Так что, не признаетесь?"
show f 07
F_m "Она всерьёз предлагает оценить, что страшнее – пожар или предполагаемый убийца в моём доме?"
F "Скорее, стало тяжелее. Я боялся, что меня убьют в собственном доме."
show k 04 #flip
K "Э?"
show k 05 #flip
K "Но сейчас же вы не считаете меня убийцей?!"
F "Не уверен. Надо учесть все факторы и вновь пересчитать…"
show k 26
K "Ладно! Проехали!"
show k 03
K "Но вы же начали сами читать письма!"
show f 08
F "Это было один раз, и ты всучила мне их насильно. Не уверен, что эффект будет долговременным…"
K "Погодите! Но вы ведь даже сами вышли на улицу!"
show f 12
F "Ты вытолкала меня против воли…"
show k 02
K "Как так-то…"
show k 06
K "Разве я не должна была стать героиней, спасшей человека из затворничества…"
show f 13
F_m "Что это с ней?"
F_m "Это в первый раз, когда всё идёт не так, как она задумала?"
show f 24
F_m "Хех!"
K "Вы смеётесь? Неужели дошла шутка про налёт?"
F "Пф-ф!"
show f 07
F_m "Почему мне так смешно от вида её растерянного лица?"
show f 11
F_m "Я заразился её безумием?"
show k 12
F "Кхм-кхм. Налёт… то есть, это дело. Думаю, я могу признать, что ты помогла мне найти птиц и предотвратить новые пропажи."
show k 05
K "Ага! Я так и знала!"
show f 08
F_m "Она стала прежней в мгновение ока…"
show k 03
K "К тому же, раз теперь я буду всё время рядом с вами, чтобы устранить любые возникающие пожары…"
show k 16
K "То вы точно обязаны повысить мне зарплату!"
show f 13
F "Что?! Как ты опять всё свела к этому?!"
K "Вы признали, что я была полезна."
show f 07
F "Но я могу также признать, что из-за тебя сломался бойлер. И если вычесть его стоимость из твоей зарплаты…"
show k 09
K "Ой! А времени уже сколько, мне пора готовить обед!"
#к выскальзывает за дверь.
show k 10 at exit_right(1), flip_back
pause 3
hide k

show f 25 at giggle(repeats=10)
F "Аха-ха-ха-ха-ха!"
F "Это был самый безумный разговор за всю мою жизнь…"
show f 07
F "..."
show f 24 at exit_left
pause 1
hide f 24
#садится за стол
show fel_table 04 at fel_table_pos
show kabinet_table
with dissolve
F_m "Перестать бояться?"
F_m "Использовать свою силу?"
show fel_table 02
F_m "Смогу ли я когда-нибудь…"
F "..."
show fel_table 03_fire  # + рука с огнем
pause 2

stop music fadeout 3
show bg_black with Dissolve(3)
#F вытягивает руку перед собой ладонью вверх и зажигает на ней маленький синий огонёк.


# Сцена 16.
###############################################################################
call time_passed("Прошло 2 месяца") from _call_time_passed_8
hide k
hide f
hide bg_kabinet
show bg_black
scene bg_ptichnik2 with Dissolve(1)
show k at enter_c_left
play music music_poultry fadein 3

#Начинается трек "Poultry house ". Без fade in
#птичник спустя 2 месяца, к опять болтает с птицами
show k 05
K "Здорово, ребята, давно не общались."
show k 02
K "Загруженные деньки выдались…"
show k 03
K "Но можете поздравить, меня официально повысили!"
K 'Теперь я не какая-то там "служанка", а гордая "домоправительница". Да-да!'
show k 02
K "Что? Почему меня так долго не повышали?"
K "Думаю, поломка бойлера осела черным пятном в моём личном деле… Феликс такой дотошный…"
show k 03
K "Кстати, да! Прикиньте, я узнала, как его зовут, неделю назад!"
K "Это было довольно сложно! Этот толстяк всё никак не хотел говорить… Хотя, лучше вам не знать подробностей."
K "Уверена, Феликс всё ещё не знает, как меня зовут!"
show k 11
K "Будет повод дальше подшучивать над ним, хе-хе!"
K "Вижу номер 37, ты опять недоволен? Но я сегодня добрая и спущу тебе это с лап."
show k 14
K "Кстати, только не падайте, мы сегодня идём за покупками! Вместе!"
K 'Мне осталась совсем капелюшечка до звания "героини, спасшей жизнь человеку"!'
show k 11
K "Ведь только благодаря несравненной мне Феликс начал читать книги! Из бумаги!"
show k 13
K "Правда две из трёх он топит в ведре с водой, потому что ему показалось, что искра упала на страницу… Но мы работаем над этим."

K "Ладно, я уже опаздываю. Так что берегите себя, и до встречи."
show k 10 at flip, exit_left
pause 3
show k 05 at enter_c_left(1)
# к уходит
# быстро возвращается
K "Ладно, скажу только вам и по большому секрету. Меня зовут Клементина."
K "Чур, Феликсу ни слова!"
K "Всё, теперь точно ушла!"
stop music fadeout 4
show k 10 at jumping(4, 20, 0.2)
pause 1
show k 10 at flip, exit_left(1)
stop music fadeout 3
pause 1
show bg_white with Dissolve(2)
hide k
# к уходит

#Сцена 17.
###############################################################################

scene bg_white 
pause 2.0

play music music_gratification
show bg_hall
show f 08 bald at c_left
with Dissolve(3)

pause 1
show k 13 at enter_c_right, flip
#Холл, F стоит без шляпы и без огня, входит К
K "Что это так слепит?! Взошло второе солнце?"
show f 08 # (поворачивается к ней) + улыбается
K "Или это твоя лысина?"
show f 24 long_hair with dissolve
show k 11 
F "Хах! А так тебе больше нравится?"
#На голове появляется пламя в форме длинных, развевающихся волос
K "Ого! И надолго ли тебя хватит, супергерой?"
show f 07 #+ О4
F "Думаю, минут на двадцать…"
show k 10 
K "Тогда нам нужно поторопиться! Я не хочу ещё неделю питаться только картошкой!"
show k 24
show f 25 # (берёт его за руку) + улыбающееся лицо для Ф
F "Вперёд!"
show bg_black with Dissolve(1)

#Сцена 18 - конец.
###############################################################################
scene bg_krishi with Dissolve(1)
#Цг где они выходят в светящийся проход.
F "Но картошки мы всё равно ещё купим?"
K "Конечно."
window hide
$ persistent.game_completed = True
$ renpy.config.main_menu_music = music_gratification

$ renpy.block_rollback()

scene bg_black with Dissolve(5)
$ unlock_achievement(GAME_COMPLETED)
call screen credits

return