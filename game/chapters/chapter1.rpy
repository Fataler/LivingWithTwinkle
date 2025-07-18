label chapter1:
#Сцена 1.
################################################################################

#фон с часами → фон со входом в башню*

scene bg_black 
show bg_bashnya
show bg_bashnya_arrow:
    xpos 1161
    ypos 625
    block:
        pause 3.0
        linear 0.1 xoffset 1.1 yoffset -1.1 
        linear 0.1 xoffset 0 yoffset 0
        repeat
with dissolve

#play music music_tower loop fadein 2.0 fadeout 2.0

#show fel at c_left

"Каждому в этом мире повезло родиться со способностями, но не Феликсу." 
"Нет, способность-то у него была, но она отравляла каждую минуту его существования." 
'"Почему мне не досталась способность — разговаривать с жуками, как тому чудаку с Каретной улицы..."'
"Такие мысли не посещали Феликса уже лет двадцать."
"Теперь он лишь иногда вздыхает, когда очередная обугленная муха падает на его плечо."
"Не считая этих мелких неурядиц, жизнь в огромной часовой башне шла размеренно."
"И как будто бы ничто не могло нарушить её привычное течение…"
#window hide

#Клик после текста запускает заевшую стрелку - она щелкает на следующий штрих и сцена меняется
#фон с часами → фон со входом в башню*

#Сцена 2.
################################################################################

#кабинет, гг сидит за столом в шляпе, аккуратно подписывает бумаги, секретарь стоит поодаль.

#scene bg room with Dissolve(1)

$ unlock_achievement("first_steps")
show bg_kabinet 
show fel_table 01 hat at fel_table_pos
show kabinet_table at fel_table_pos
show s at c_right, flip
with Dissolve(2)
play music music_felix

pause 1.0

F "Она уже приехала?"
S "Да."
F "И ты передал ей список?"
S "Да."
F "Хм…"
F "Она хоть нормальная?"
S "Да… {w=0.5} за кого вы меня принимаете?"
S "Думаете, я стал бы подбирать первую попавшуюся нищенку на базаре, только потому что у меня с завтрашнего дня отпуск?!"
F "..."
F "Полагаю, что нет."
# гг отдает документы

S "Вы закончили с бумагами?"

show s at step_left(3.0, step_time=0.5)

pause 2

show s at flip, step_right(3.0, step_time=0.5)
#show s at flip
show fel_table 02
F "Кстати,{w=0.5} я сейчас работаю над одной моделью, у неё скорость выше на семнадцать процентов, и мы могли бы…"
show s at flip
S "При всём уважении, сэр, но это перестанет входить в мои обязанности через {i}двадцать{/i} минут."
show fel_table 04 hat
F "А…{w=0.5} ну да…"
S "Тогда на этом я прощаюсь."

show s at face_left, step_right(2.0)
pause 1.0

F "Всё-таки, это печально."
show s at face_right, step_left(1.0)
pause 0.5

S "Вы жалеете, что дали мне отпуск?"
show fel_table 02 hat
F "Что? Нет."
F "Я... {w=0.5} про смерть моей прежней служанки."
show s at face_right, step_left(1.0)
S "Вы даже не помните, как её зовут?"
F "Она хорошо справлялась со своими обязанностями."
show s brow at c_right
S "А как {i}меня{/i} зовут?"

F "..."
pause 1
F "Удачного тебе отпуска."

show s normal at flip, step_right(20, step_time=0.25, step_size=100)
pause 5
hide s
#секретарь вздыхает и уходит
F "..."
show fel_table 04 hat
F "Как же сложно общаться с людьми…"
stop music fadeout 4

scene bg_black with Dissolve(1)

#Сцена 3.
#################################################################################


#к с ведром и шваброй плетётся по коридору и осматривается
scene bg_koridor:
    xpos -1920
show k 01 at center, flip
with Dissolve(1)
play music music_trouble
K "Не могу поверить, что я нашла эту работу на базаре…" 

show bg_koridor at background_step(-1920, 200)

show k 01 at step_up

K "Это же самое таинственное и легендарное место в городе…"

show bg_koridor at background_step(-1720, 200)

show k 02 at step_up

K "В основном, легенды жуткие… {w=0.5}Но всё же!"

show bg_koridor at background_step(-1520, 200)

show k 03 at step_up

show bg_koridor at background_step(-1320, 200)

K "И что это за карта?"

show bg_koridor at background_step(-1120, 200)

show k 04 at step_up
#Нарисованная от руки карта башни, где на её вершине изображен злой демон
K "Будто ребёнок рисовал."

show bg_koridor at background_step(-920, 200)
show k 04 at step_up

#убирает карту
K "Тот человек точно тут работает? А вдруг меня обманули?"
show bg_koridor at background_step(-720, 200)
show k 04 at step_up

K "Хотя вёл он себя весьма по-хозяйски…"
show k 03
K "Ладно, в любом случае, доберусь до самой верхней комнаты и наверняка встречусь с хозяином!"
show k 04
K "Кто так нанимает прислугу, даже не встретившись с ней?!"
show bg_koridor at background_step(-520, 200)
show k 03 at step_up
K "Да, притворюсь, что мою тут пол, а потом всё выскажу!"
show bg_koridor at background_step(-320, 200)
show k 04 at step_up
K "Стоп. Мне же нужна эта работа."

show bg_koridor at background_step(-120, 100)
show k 03 at step_up, c_left with dissolve
play sound sfx_knock
K "О, а вот и нужная дверь!"
#стучит в дверь

show k 06 at jumping(2), center
K "Кхм-кхм, пардоньте."
show k 06 at step_left(20, 0.4, 200)
pause 3
scene bg_black with Dissolve(1)
# тут как раз должна быть та длинная цг-шка, где на одном конце она открывает дверь, а на другом гг без шляпы.

#Сцена 4. 
################################################################################

scene bg_kabinet
show fel_table 01 at fel_table_pos
show kabinet_table at fel_table_pos
show k at c_right
with Dissolve(1)
#кабинет
#к смотрит в пол и мнется
show k 06 at enter_c_right, flip
K "Я тут мыла пол, и…"
#F в шоке вскрикивает
show fel_table 03 at jumping(4)
F "ЭЙ!"
show fel_table 03 at scared
F_m "Где же шляпа?" #не знаю, как помечать мысли, может маленькой "м"?
show fel_table 03 at face_right
# тут надо включить экшон, где он оборачивается в поисках шляпы, а она замечает огонь и бросается его тушить. В итоге он падает на пол и страдает от побочек своей силы.
#show k 10 at jumping(4)

play sound music_klementine
#pause 2
show k 07
stop music fadeout 2
pause 2
K "Огонь!"
#тут думаю на спрайтах сделать — она подъезжает к нему и выливает ведро (или использует силу), а он заваливается за стол. 

scene bg_black
hide k
hide f
with Dissolve(1)
#window hide
pause 2
show bg_black
show cg_1 with Dissolve(1)

play sound sfx_water_and_fire
#А потом уже цг - где она трясёт его за грудки.

window hide
stop music fadeout 2
pause 2
play music music_felix
window show
show cg_1 at punch_h(0.2, 20)
K "Он же не умер?"
F_m "Сдавило грудь…"
F_m "Не могу дышать…"
show cg_1 at punch_h(0.2, 20)
K "Эй, ты же не умер?!"
F_m "Умер? {w=1}Я умер?"
show cg_1 at punch_h(0.2, 20)
K "Кто мне зарплату будет платить?!"
F_m "Что? Какая ещё зарплата…"
#огонь на голове снова загорается, он открывает глаза
F "Ты меня… {w=1}трогаешь?"
K "Нет…"
#отпускает его, он падает на пол.
#фон с кабинетом, сначала появляется только К, (F лежит на полу)
scene bg_kabinet 
show k 01 at c_right, flip
with dissolve
K 'Сразу бы так и сказали, что увлекаетесь "горяченьким", зачем людей пугать.'
#смотрит на несуществующие часы на руке
show k 09 at flip_back
K "А времени уже сколько, мне ещё обед готовить."
#убегает
show k 09 at step_right(20, 0.2, 100)
pause 3
hide k 09

pause 1
#F встает — появляется его замученный спрайт за столом.
show fel_table 04 at fel_table_pos
show kabinet_table at fel_table_pos
with dissolve
F "Что сейчас произошло?"
F_m "Следуя очевидной логике, эта женщина – новая помощница, нанятая секретарём."
F_m "Скорее всего, кухарка. Да, зачем иначе она говорила бы про обед."
F_m "Но какой обед? Одиннадцатый час вечера…"
F_m "Может ли она быть подосланной убийцей?"
F_m "Хм, вряд ли. Кажется, она действительно испугалась…"
F_m "Но зачем она меня трогала? Пыталась забрать что-то в качестве доказательства моей смерти?"
F "Заметка: {w=0.5}не доверять Секретарю найм персонала."
F_m "Что она вообще тут делала? Она не получила список правил?"
F_m "Неужели и здесь я больше не смогу расслабиться…"
#громко вздыхает
show fel_table 04 at step_up(step_size=5)
F_m "Эх…"

stop music fadeout 2
pause 2

play sound sfx_knocked_down_door
pause 1
#звук выбитой с ноги двери, или удара двери о стену
show k 03 at flip, enter_c_right(1)
pause 1

show k 03 at c_right, joy
play music music_trouble
K "Чего так громко вздыхаете?"
show fel_table 03
#sh 03
F "Ай!"
#натягивает шляпу
show fel_table 03 hat with dissolve
show k 11
K "Ой, да чего я там у вас не видела."
show fel_table 02
#sh 01
F "Это мера предосторожности."
F "Зачем ты пришла? Хочешь закончить начатое?"
show k 06
K "Вообще-то да, я забыла..."
show fel_table 05
#sh 01
show k 12
F "Убить меня! Я так и знал!"
show k 06
K "Швабру."
show fel_table 02
#sh 01
F "Что?"
K "Швабру я забыла, говорю."
F "А…"
show fel_table 04
show k 12
F "Уверена, что не хочешь убить меня?"
show k 06
K "А зачем мне это? Кто тогда будет платить мне зарплату?"
show fel_table 02
#sh 01
F "Звучит логично."
show k 11
K "Хотя.."
show k 02
K 'Какой убийца, ответил бы "да"?'
show fel_table 05
F "Значит, ты признаёшься!"
F "Да?"
show k 16
K "Заплатите мне, тогда отвечу."
show fel_table 04
F "Сколько?"
show fel_table 03
show k 13
F "Так, стоп!"
show k 11
K "Если надумаете, знаете, где меня найти."
#к уходит за дверь
show k 10 at flip_back, exit_right(2)

pause 4

show fel_table 04
F "..."
F "Так, нужно провести расчёт."
#d1
#вскакивает со своего места, дергает за рычаг опускающий доску для мела
play sound sfx_lever

hide fel_table with dissolve
pause 0.5


show f 06 at flip:
    xpos -1080
    pause 1
    linear 1 xpos 100
show d1 at pause_menu_board_drop(-1080)

pause 1

play sound sfx_blackboard loop
#o2
F "Эта странная служанка… Она ведь уже призналась, что убийца?"
show f 07
F "Нет. Это было лишь предположение в форме вопроса."
show f 06
F "Но убийца мог так сказать, чтобы отвести от себя подозрения…"
F "Но зачем ей деньги? Странно."
F "Таким образом, она предлагает мне выкупить собственную жизнь?"
show f 07
F "И кто заказчик?"
F "Хм…"
F "Вероятность, что служанка – убийца, меньше трёх процентов."
show f 08
F "Глупо из-за этого переживать."
F_m "Пожалуй, стоит отдохнуть"
stop sound
play sound sfx_lever
show d1 at pause_menu_board_hide(-1080)
pause 2
hide d1
show f 07 at flip_back
F_m "Но спать в одном доме с трёхпроцентной убийцей…"
F_m "Запру дверь. Да…"
stop music fadeout 3

window hide
show bg_black with Dissolve(3)
#*Сцена 4.1 - кошмар
################################################################
call horror_scene from _call_horror_scene
window show
#Сцена 5. 
################################################################################
call time_passed("На следующее утро") from _call_time_passed
scene bg_ptichnik2 with Dissolve(1)

show f 24 at enter_c_left

pause 0.5
show f 24 at c_left
#sh 02
#на следующее утро F в птичнике
F "Сегодня у вас всё спокойно?"
F "На вас всегда можно положиться."
#к выглядывает
show k 01 at enter_c_right, flip
show f 10 at scared
play music music_klementine
K "Разговариваете сами с собой? {w=0.5} Мило."
#налево
show f 11 
#sh 02
F "Нет, с птица-ми…"
show k 11
F "Я всегда так делал. Это абсолютно нормально!"

K 'А разве я говорила, что это "ненормально"?'
show f 08
F "Нет, но… В любом случае, что ты здесь делаешь?"
#F отворачивается от неё
show f 08 #flip
#sh 02 flip
F "Уверен, что в правилах, которые тебе выдали, первый пункт – не попадаться мне на глаза."
show k 14
K "Я как раз хотела узнать, зачем нужно это правило."
F "Я боюсь…"
F "Нет. Это опасно для кого бы то ни было – находиться рядом со мной."
F "Так что лучше нам не пересекаться."
show k 15
K "Но тогда как я узнаю, удовлетворены ли вы моей работой или нет?"
F "Я всем доволен."
show k 14 #шаг
K "Но я ничего не сделала."
F "Что?"
F "А, ну, ты же только вчера начала работать. Так что это нормально."
show k 15
F "Нормально же?"
show f 11
F_m "Что я несу?! Почему она не уходит?"
show k 14
K "Вы, должно быть, самый щедрый работодатель во всём мире."
show f 08
F "Раз ты поняла, как тебе повезло, можешь заняться делами."
#к встаёт перед лицом Ф
show k 14 #flip
show f 12
K "Значит, вы тут сидите целыми днями совсем один?"
F "На то есть причина…"
K "И даже служанок вам нанимает другой человек?"
F "Это входит в его обязанности."
K "А если вам понадобится что-то из города?"
F "Это уже входит в твои обязанности."
show k 03
K "Значит, без меня вы полностью беспомощны?"
show f 13
F "Что?! к чему ты клонишь?"
show k 14
K "Так что?"
show f 11
F "Вовсе не полностью…"
show k 05 #flip
K "Докажите!"
K "У вас на кухне одна картошка, нужно сходить на базар. Идёмте вместе."
show f 13
F "Что за глупости, с какой стати я должен что-то доказывать тебе?"
show k 16 at joy, c_right
K "Тогда повысьте мне зарплату."
show f 14
F "Это переходит все границы! Ты работаешь тут один день…"
show k 05 at joy, c_right
K "Второй день."
show f 07 
show k 02
F "Пусть так. Второй день…{w} и ничего не сделала!"
show k 05 #flip
K "Почему ничего, я окатила вас пеной."
show k 02 #flip
F "Да! Окатила… {w=0.5} меня…"
show f 14
F "Кстати, я ещё не снял с тебя подозрения!"
show k 06 #flip
K "Ага, понятно."
show f 07
F "..."
F "О чём, значит, я говорил?"
show k 12 at joy, c_right
K "О том, что хотите повысить мне зарплату."
show k 13 #flip
F "Да, повысить…"
show f 14 at angry, c_left
F "Что?! {w=0.5} Нет!"
show k 11
F "Ты ужасная! {w=0.5} Грубая. {w=0.5} Вопиющая…"
show k 12 #flip
K "И поэтому вы пойдёте и наймёте себе другую служанку?"
show f 14 at angry, c_left
F "Да! {w=0.5} Пойду! {w=0.5} И найму!"
show f 14 #flip
#sh 02
#проходит к двери
show f 17 at flip
F "..."
pause 1
# тут сделать анимацию "не страшно"
show f 18 at flip
F "..."
F_m "Я пойду…"
show f 18 at step_left 
F_m "Нет ничего страшного в том, чтобы пойти куда-то…"
show f 18
F_m "Мне совсем не страшно…"
# несколько раз повторяет "не страшно"
show f 17 at fear, c_left
F_m "...мне страшно…"
show k 02 #f
K "М?"
show f 19
F "Я не могу."
F "Можешь оставаться."
F "Но зарплату не повышу."
show f 19 at exit_left
stop music fadeout 2
pause 1
show bg_black with Dissolve(2)
#F уходит
jump chapter2
