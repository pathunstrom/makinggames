I'm Piper Thunstrom:

* software developer at GLG
* author of PursuedPyBear, a python game framework
* games enthusiast.

I've been an enthusiast for as long as I can remember.
Tabletop, video games, LARP, you name it, I've probably tried it.
That clearly doesn't stop at _playing_ games.
I used to experiment with my brother and build card games.
I build board games as class assignments.
When I started programming, I started building video games.

I can confidently state that video games are why I'm a developer today.
I jumped in feet first, and used games as a platform to learn.
I learned some math I didn't get in school, like trig, calc, and
linear algebra.
I've taught myself physics to better model games.
I even spent a week learning the ins and outs of fireworks for a game I
wanted to build.

On top of all of that, though: I was learning software engineering.
If you have any questions:
* find me in the hall
* tweet me @pathunstrom,
* email me at pathunstrom@gmail.com

You can find my talk notes on github at pathunstrom/making-games.

You can find the source to `ppb` at github.com/ppb.
Contributions encouraged, we need docs, examples, tests, and we're
working on the event system.

Thanks everyone for your time!I've organized this talk like a how I'd write a video game.
Here, we're setting up for the talk proper.
We'll cover a couple details you'll need to follow along.

After that, we talk about video games and how you make them.
We'll cover player input.
Then modeling and simulation.
At the tail end of that section, we'll cover rendering and graphics.

After we break from the details, we'll cover some organization.
And finish up with some game libraries you can go try.
Games, like all graphical interface programs, including your web
browser are long running process.
I guarantee the entire room has used a tool or framework that uses one.
Django and Flask both require one.
Jupyter notebook has at least one (since it's also a web server).
The idea is fairly simple: your code keeps running, waiting for some
kind of input, and then responds to it.

In games though, we're responding every 60th of a second.

To do that, we use something that looks a lot like a busy loop.
While True, get any input, make updates, and show the user the
result.
Unlike web servers, in games:
* Our input tends to come from hardware
* Our state and models exist directly in memory
* Our output is rendered directly, instead of being sent to a remote
  user.

So a really basic game can look like this.

While true,
handle input,
update simulation,
render.

This is great for your first game, but `while True` will quickly get in
the way of things. In general, I prefer a boolean to handle my loop for
me. And that'd look more like this.
So we enter our game loop and start with player input.

We often call these "main" loops event loops as an extension of the
concept of events.
In game terms, we call key presses and mouse movement, touches and
swipes events.
In general, these are provided to your game library of choice via
interrupts at the hardware level.

Handling events can take a handful of forms.
The first is simple polling:
at this point in your game loop, you check a list of events that came
in and deal with them as you prefer.

The other option is to define callbacks.
A callback is a function to be called when a certain event happens.
These take a lot of forms, from naming them with a special pattern like
"on_event" or by registering the callback to another object using
something like the publish-subscribe pattern.

After you can take in the events, then you can start modifying state
using them.

With really simple games you can just set variables or object
attributes and then react to them during your updates.

Due to player preferences, it's nice to be able to rebind your
controls.
You can create an object to represent your controller.
On the outside this can provide your code a single interface to various
input.
Inside the class you can abstract the idea of specific keys by letting
a configuration file define what keys map to what particular input.
We advance our loop, and now we get to the _fun_ part.
In the simulation is where the game happens.
A bunch of objects moving and interacting according to the rules we
write.

So let's start with our objects.
We have to model the game space and there are many options for this.
In very simple games, we can use standard data structures to represent
our game objects, and use functions to change state inside your game
loop.
It's easy you can start building immediately, but it'll
eventually get messy.

We can use object orientation to model our game space.
This has the convenience of coupling behaviors directly to our game
objects, which makes it easy to track what's called where.
It also allows us to keep a lot of redundant calls out of our
framework.
In my experience, anywhere you can think of your mechanics as the
behavior of one or two objects, instead of the entire play space, the
better.

The last modeling technique I want to talk about is a design pattern
called Entity-Component-System.
The basic idea is:
* Your game objects are entitites, which are simple containers.
* Your attributes belong to components, which are objects your entities
  contain.
* Systems take entities, and act on them if they have the right
  components. These would be your systems.

The advantage of ECS is that you can build much large games with fewer
conflicts, but it has a larger learning curve if you're building on
your own.

The right modeling design depends on the game and your skill level.
Moving on to behaviors: so a behavior is literally what a game object
does.

These can be things like spawning objects, moving, defending,
grouping up: if you can do it, it's probably a behavior.

To make this concrete, let's use Gaunlet as an example.

Enemies and the player have a move behavior.
Enemies, the player, and spawners can be damaged.
The player can attack.
Spawners can spawn.

Behaviors can take a lot of forms, and depending on how you chose to
model your game, it'll affect some of how you program them.
It's harder, for example, to use the State or Strategy patterns when
your game objects are just data structures.

When you first start writing games, you'll probably use per frame
updates.
Effectively, every time your game loop ticks, you do the same behavior.
Think a ball bouncing left to right.
This style of update has a flaw, though: the speed of the game is based
on the computational cost of your game loop and the speed of the
processor it's running on.
That's a _lot_ of variability.

So the first thing you want to fix this is to parameterize all your
behaviors based on time.

The difference looks like this.
"dt" here stands for "delta time" and stands for the amount of time to
simulate.
By doing this, we can think of speed in real world terms:
Some distance per second.

In the engine itself, you need to start tracking run time, and inject
the delta every frame into the simulation.

A second trick is instead of injecting the full delta every loop is to
break up that time delta and update your objects with tiny fixed time
steps.
So if a game loop took 33 milliseconds, but you want the simulation to
be sixty updates per second, you split up that 33 into two 16 ms chunks.

Another pattern to know is the Update pattern, which is used in almost
every game library you have available to you.
How it works is that every game loop, the engine calls an update
function for every game object.
This gives a very obvious place to put your various behaviors.

So I've demonstrated how movement works, but let's talk about the other
thing you need: collision detection.

Almost everything you do will need to measure collision, even if it's
just checking if the mouse clicked an object.
There's two really simple collision checks that are available in 2d
games.

The first is circle to circle collision.
The math for this is really
simple:
Given two objects with bounding circles, if the distance
between them is less than the combined length of their radii, then
they've collided.

This only requires two pieces of information from both objects:
* their center points
  (you probably have this because it's the position of your objects)
* the radius needed to contain them

And then one measurement for the distance between them
quick addition to get the combined radii
and one comparison.

    return (c1.center - c2.center).length < c1.radius + c2.radius

Quick and easy, but it's got a failure point:
A circle almost definitely has more space than the object itself.

A slightly more accurate solution is axis aligned bounding boxes,
or AABBs for short.
This is slightly more complex:
Given two objects with AABBs, they are colliding if:
the combined height of the boxes is less than the distance from the
highest side of the higher object to the lower side of the lower object
and
the combined width of the boxes is less than the distance from the
furthest left side of the most left box to the most right side of the
rightmost box.

Mouthful, right?

Thankfully, the code is a bit simpler.
Assuming a standard coordinate plane:

    vertical_distance = max(b1.top, b2.top) - min(b1.bottom, b2.bottom)
    combined_height = b1.height + b2.height
    horizontal_distance = max(b1.right, b2.right) - min(b1.left, b2.left)
    combined_width = b1.width + b2.width
    return vertical_distance < combined_height and horizontal_difference < combined_width

And now you can determine when you hit things.
Moving on to rendering, we should start with screens.

Your screen is made up of a two dimensional array of pixels.
Each pixel can produce red, green, and blue light, in some mix.
How these pixels get lit depends on the tech in your monitor, but
unimportant to our topic.
To "draw" something you just tell every pixel what colors it should
display.
A screen typically refreshes from the top line of pixels to the bottom,
left to right.
Because of this, typical software libraries have you use the same
coordinates:
the origin is in the top left corner.

This is kind of abstract, but that's good because it's very similar to
how it works in code.

In any given game engine you'll be given a display object of some sort.
Sometimes called a window, the important part is this object is what
eventually gets drawn to the screen.

In 2D games, they'll be similar to a pixel array, where you can draw
various things to it, and then send it to the physical display.
This ability to use a pixel array to draw to leads to one bad habit
even I'm still breaking:
using the pixel grid as your simulation grid.

For very simple games, they might be close enough:
After all if your player can only move inside the limits of the
display, why not match them?

The biggest problem with this comes when you start trying to add camera
effects of any kind:
A camera that follows objects can have trouble if you only use full
pixels for movement.
Zooming is almost impossible as you try to add more game space, your
pixel grid has to become smaller somehow.
And a game developers favorite effect, screen shake, is _really_ hard if
you're only using your display space as game space.

To fix it, think in 'game units', which can be arbitrary scale.
Then add an object to be your camera, and use it's position and other
features to decide what, exactly, to draw to screen.

It takes some figuring out, but it opens up a whole work of
possibilities.

But to get to those possibilities, you need to know how to get images
in the right spot.

In general, your game library is going to give you two sets of
features for putting things on screen:
* drawing primitives
* blitting

Drawing primitives will be the most basic kinds of things: circles,
squares, triangles, and lines. Depending on your library you might get
other features, but you should be able to have these.

Each one gets applied to either the display object itself, or sometimes
to another object that is more like a canvas that you can use later.

All of these are paramterized, so you provide a location and size, and
usually color and you can put them on screen.
You can make some really simple game images this way, which is also one
of my favorite ways to develop.

Blitting, on the other hand, is taking a destination canvas, and
drawing a source image onto it.
The capabilities of the blit are going to depend on the library so I
don't want to go into too much detail.
The key thing to know is that you can:
* play with how the colors layer on existing colors, called blend mode
* experiment with how transparency works, using alpha channels or
  color keys.

The final thing I want to cover about rendering is a simple warning:
In Python rendering is probably the _most_ expensive thing you're going
to do in a game.
Pygame on some systems can take up to a full 33 ms to render a frame,
leaving you with negative time to maintain 30 frames per second.
So we're done with game loops, now onto some organizational thoughts.

How do you make a game with multiple different sections? You know,
menus, games, game over screens.

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

You'll probably want to experiment with all of these methods and find
what you like best because the cool part about Python game making:
there's a lot of opinions.
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
