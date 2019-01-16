Moving on to rendering, we should start with screens.

Warning that the following description is _heavily_ simplified.
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
Zooming is almost impossible:
as you try to add more game space, your pixel grid has to become
more dense somehow.
Game developers favorite effect, screen shake, is _really_ hard if
you're only using your display space as game space.

To fix it, think in 'game units', which can be arbitrary scale.
(Meters is good)
Then add an object to be your camera, and use it's position and other
features to decide what, exactly, to draw to screen.

It takes some figuring out, but it opens up a whole world of
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
