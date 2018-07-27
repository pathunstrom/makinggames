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