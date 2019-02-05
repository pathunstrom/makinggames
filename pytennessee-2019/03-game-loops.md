So let's start small. Making your first game is easier than you might think.

Because every game is a long running process, you start with a simple loop:

    while True:
        do_input()
        update_state()
        render_result()

Clearly, this snippet won't do anything, but it shows the basic structure of
your first game:

- you're going to take some input from the player
- you'll make changes to the game state based on the player's input (or your AI)
- then you'll render the result for the player to react to.

With some of the game libraries available to you in python, your game loop is
done for you, but I encourage you to try building some little things where you
hand roll your event loop to get a feel for it.

Going forward, we'll discuss how to handle each of these in the context of
tic-tac-toe.
