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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player_input:
                mouse.move(event.pos)
                square = pygame.sprite.spritecollide(mouse, board, False)[0]
                square.selected(CROSS_IMG)
                player_input = False
        elif event.type == AI_MOVED:
            player_input = True
        elif event.type == GAME_WON:
            running = False
            winner = event.winner

On every game loop, we're going to ask the event system for a list of events
that have arrived since the last call. *'* Then we check each for the events we
care about. Most of them are going to be based on the SDL events, but you can
also extend the system and define your own event types, like in this sample
where the AI tells me when it makes moves and when the game ends an event is
raised. *'*

In general, you'll use these events to tell objects to change their state, like
in this example selecting a square on the tic-tac-toe board or take some global
action like ending the game loop.
