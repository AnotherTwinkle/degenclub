# Brief- Flugel greets the player.
# Characters used- fgl, flx

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

    "Hello"
    pause 1
    play music 'audio/flx.ogg'
    show flx happy at left
    flx 'Welcome to the unfinished classroom.'
    return
    