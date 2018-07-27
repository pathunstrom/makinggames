So I've used the term "scene" a number of times, and at this point I'm going to
step back and explain the idea.

A "scene" is one section of a game. In a simple example, Tetris had a Title 
screen, the game menu, the game itself, and a victory scene for B mode. All of 
these are scenes. Taking your classic JRPG, every map is a scene, the battle 
interface is a scene, the full screen menus were scenes, the title screen, 
the load screen, the game over screen. . . So as you can tell, this can be 
simple or extremely complex.

So instead of complex nested loops, we'll look at some other ways to organize 
your code.

The simplest way to organize it, and a good choice for your first few games is
to put each scene as a separate function. It's also an excellent choice for 
most arcade style games.

{ SLIDE }

With only a handful of scenes, and shallow nesting, it's very easy to keep 
track of where various functions need to be.

The nice thing here is that your scene stack is handled by the interpreter. 
Pushing is as simple as making a call, and a return pops. You lose some 
convenience functions you'll want for more complex games, like replace.

A primary disadvantage of this type of organization is that shared state 
between different functions and scenes has to exist in the parameters and 
return values, or you're using a lot of globals. This can make your name spaces
a bit ugly.

So instead you can use a Scene class. This lets you store shared state 
internally to the scene, separate the various parts of the game loop into their
own methods, and you still get the advantage of the interpreter stack working 
for you.

{ Slide }

There's not really a downside to using Scene objects, and almost every pattern 
I discuss going forward is built on this idea.

Another thing you can do, but I don't recommend, is use modules as your scenes. 
This is mostly a heavier handed version of class based scenes, but it enforces 
a singleton pattern. If you have a scene that should never have more than one 
instance, consider a module. A good choice here is a configuration menu that 
you might open from many places, but is also the canonical record for 
preferences.

The final pattern is a combination of the previous two. Instead of having a run
loop in every object you have a loop running in a single module that manages 
the disparate parts of your game. This game loop calls the functions you need 
in you basic game loop on whatever scene is currently active.

What this looks like is something like this.

{ SLIDE }

Your engine module runs, and has an internal stack that keeps track of which
scene is active. It then calls the relevant methods on the scene, passing any 
external information as needed. This way you have a single loop running your 
game and simple procedural code running the different parts.
