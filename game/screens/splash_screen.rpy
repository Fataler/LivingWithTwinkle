################################################################################
## Сплешскрин
################################################################################
init -2 python:
    renpy.music.register_channel("video", loop=False, stop_on_mute=True, tight=False, movie=True)
    renpy.music.register_channel("video1", "video", loop=False, stop_on_mute=True, tight=False, movie=True)


init:
    image logo_jam = Movie(channel='video1', play="video/jam4.ogv", loops=0, stop_music=True)

screen logo_jam:
    add "logo_jam"
        
label splashscreen:

    if not splash_enabled:
        return

    scene black
    with Dissolve(1.0)

    stop music
    scene bg_white

    show screen logo_jam
    if persistent.first_start:
        $renpy.pause(4.85, hard=True)
    else:
        $renpy.pause(4.85)
    $renpy.music.stop(channel='video1', fadeout=None)
    hide screen logo_jam
    
    if persistent.first_start:
        $persistent.first_start = False
    
    return
