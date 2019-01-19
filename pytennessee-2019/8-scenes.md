So we're done with game loops, now onto some organizational thoughts.

How do you make a game with multiple different sections? You know,
menus, multiple levels, game over screens.

In general, you'll find each of these things referred to as "scenes".
A scene is simply a single part of your game.
Your scene is where your game objects live.
Without the scene, they're bags of data with no context.

They can take the form of functions with while loops, with their own
set up, loop, and tear down. My very first game was built like this,
and it got messy _really_ fast.

They can be objects of their own, a slightly nicer solution than just
bare loops or run functions, but they require debugging that main loop
and can make it difficult to share things like behaviors or features
all of your scenes need.

In my game library, I changed scenes into (not so simple) container
classes.
The engine gives that scene to various subsystems that can perform
their jobs on it.

The neat part of this is that you don't need to use loops to test your
scene anymore.
You call the appropriate functions and can check the state on the far
side.
There's only one infinite loop in your entire program and you don't
have to debug it!

You'll probably want to experiment with all of these methods and find
what you like best because the cool part about Python game making:
there's a lot of opinions.
