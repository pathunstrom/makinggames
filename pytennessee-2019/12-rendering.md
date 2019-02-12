All right, we've covered handling input, we discussed ways to manage your model,
so let's get into rendering.

Before we go far, I'm going to note that I have never done any direct work with
OpenGL, so this is primarily about raster graphics. *'* I'm also leaving text
based games as an exercise for all of you.

Rendering has a handful of concepts you're going to run into, so let's start
at the lowest level. You'll see words like buffer *'*, canvas *'*, and
surface *'*, depending on which rendering library you're looking at. At the
lowest level, this is memory or an object that is where the pixel data lives
for a given image. From here forward, we're going to use pygame's term for them.

When you set up your pygame game, you call pygame.display.set_mode and that
returns a special Surface that represents the actual render space. (the window)
*'* Anything on
this surface will be rendered to the screen when you call pygame.display.update
(or flip). *'*

There's a handful of ways to change what is on this surface. The first is the
fill method. Give it a color tuple, and it fills the entire surface with that
color. If you're drawing the frames "manually", you'll usually start that
process by blanking your display surface with fill.

The next thing you might do is your library's drawing module. This gives you
some  drawing primitives like
* circles
* lines
* rectangles
* polygons more generally

In the case of pygame, you pass the draw function the surface you want to draw
to and the parameters to draw and it'll put down things like lines.

Moving on to blitting, which is taking the contexts of one Surface and putting
them on another. Keeping Pygame as an example, when you call the blit method on
the destination surface, *'* pass it the source surface, *'* then optionally a
point or rectangle for where on the destination to put it, *'* and finally a
rectangle telling what portion of the source surface to take.

The last way you might handle rendering is an extension of blitting, but you
allow your library to handle it. In ppb, any game object that does not declare
itself a non-rendering object will get either its image file or a generated
color block.

In Pygame, you can use sprite groups to do the drawing for you through their
draw methods, and get some cool performance bonuses if you use DirtySprites and
LayeredDirty sprite groups.

    (Extra Credit: go research Dirty Rect Rendering.)
