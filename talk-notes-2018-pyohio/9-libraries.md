I can't cover every game related library here, because there are a lot,
but I'm going to highlight a few.
Two of them are included because they've been around a while
(longer than I've been coding).
The others are libraries I know are in active development.

The first is Pygame, because everyone in this room has heard of pygame.
At it's core, Pygame is one of the most stable SDL1 wrappers we've got
in Python. On top of that, it provides an _amazing_ AABB class called
Rect. Then you've got Sprites and Groups that provide a very
opinionated way to build your games. Definitely give this one a spin,
it's the one I learned my earliest tricks on.

The second one I want to talk about is pyglet. I've only used pyglet
for hello world level projects. Just experiments to kind of get a feel
for it. That said, pyglet runs on OpenGL and gives you bindings into
that tool kit. Also very simple, it's got a different selection of game
tools available to you.

From there, I'll move onto Arcade which I have to admit I've not had
_any_ time to experiment with being led by Paul Craven, but I know
Paul Everit who introduced me also works on it. There is a sprint today
so definitely check it out!

The last game framework I'm going to plug is mine: PursuedPyBear.
Based on pygame and SDL, ppb is a little more opinionated in how you
put games together. Providing you an engine to run your code, you can
write your game with a focus on your objects, instead of worrying about
wiring the pieces together.

Another thing to check out, if you want to explore ECS a bit more, is
Braga by Katie Silverio.
Built originally to help them write a text based adventure.
(Not actually a different process from what we've discussed).
The bonus is they do some Python magic so you don't need to reach
inside components to get at a given attribute.

My last plug is actually a book:
_Invent Your Own Computer Games with Python_ by Al Sweigart.
Al's books are awesome and his Pygame books are part of what I learned
on.
So if you want more practical examination of this topic, definitely
the next place to look.
