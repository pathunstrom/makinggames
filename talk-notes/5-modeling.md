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