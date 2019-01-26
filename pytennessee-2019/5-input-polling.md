So let's move on to events. *'*

What we mean by events is a message that _something_ happened. Things like

* mouse motion and clicks *'*
* key pressed *'*
* window resizing *'*
* hitting the close button on the window *'*

Usually, you can extend the input events with your own to note things like
enemies dying or points being accumulated.

There's two major strategies to interacting with an event system as I mentioned
earlier and we'll cover event polling first.

The basic idea with event polling is at some point in your event loop, you're
going to ask your event system for events and then handle them one at a time.

If you've seen pygame tutorials, you'll recognize this:

    import pygame as pg
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            board.square(event.pos).value = current_player
           