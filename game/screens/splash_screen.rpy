################################################################################
## Сплешскрин
################################################################################
init:
    image logo = "gui/chapel.jpg"

label splashscreen:
    scene black
    with Dissolve(1.0)
    
    show logo at truecenter
    show text "{color=#ffffff}{size=60}Разработано в рамках Капелла джем 2 \n2025{/size}{/color}" at truecenter:
        ypos 0.7
    with Dissolve(1.0)
    
    $ renpy.pause(3.0, hard=True)
    
    scene black with Dissolve(1.0)
    $renpy.pause(1.0)
    
    return
