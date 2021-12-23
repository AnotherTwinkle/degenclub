# Brief- Flugel greets the player.
# Characters used- fgl
init python:
    config.debug_sound = True

label arc_intro:
    call .greets
    return

label .greets:

    scene bg school classroom
    show fgl neutral
    pause .5
    show fgl neutral left
    pause .3
    show fgl neutral right
    pause .3
    show fgl neutral
    show fgl at right with move
    pause .5
    play music "audio/flx.mp3" fadeout 1
    "Hello"
    pause 1
    show flx happy at left
    flx 'Welcome to the unfinished classroom.'
    return
    