One of the first things most game tutorials teach you is how to move objects 
around. By updating the position of an object, you can animate movement. Easy, 
right?

{ Slide v }

The problem is almost every single one teaches you to do things per frame. So 
move the pong ball five pixels on the x axis and 5 pixels on the y axis every 
time the simulation runs. The problem with this pattern is that it's strictly 
dependent on managing how fast the frames run. If you're not rate limiting, a 
faster computer will move the objects faster.

The solution to this pattern is pretty simple though: parameterize everything.
The key parameter is time, often referred to as the time delta, or simply 
delta.

{ Slide v }

Replacing our example code, we now have a movement function 
that takes a length of time, and updates position based on a calculation of
time and speed. This lets use express movement in terms of distance over time,
in this case in pixels, which are a terrible unit.

{ Slide v }

This is another anti-pattern many tutorials teach. It makes sense for a simple
example, but will quickly limit the accuracy of your simulations. The problem 
with pixels is they're discrete units. You can't render at half a pixel (We're 
not going into high density displays and points) so you either have to track 
the portions and convert to integers when rendering, or you end up with 
rounding errors that can slowly add up and affect how the game looks.

The fix is to use two different coordinate systems. You have "game" units, set
to whatever measurement is convenient. In my case, I literally just think of 
them as units, though the scale is often equal to a play avatar's space counts 
as a unit circle. The other system is, of course, the pixel grid.

{ Slide v }

Now your continuous movement calculation can stay as a float or fixed point 
number that you convert to the pixel grid when getting ready to render.

Of course, saving this set of calculations each frame doesn't help if your 
simulation and rendering are happening at the same rate. Remember our basic
game loop?

{ Slide v }

Notice that every loop we're calling the simulation and the rendering. In some 
cases you might sleep the loop to enforce a frame rate. But if you change the 
pattern a little, you can enforce your render rate and let your simulation 
update much faster.

{ Slide v }

By only running the rendering if enough time has passed to keep the frame rate 
where you want it, you can continue simulating without wasting time on 
preparing the new frame and then getting the buffer onto the screen.

Another option, though I won't be showing how it works, is running your 
rendering in a separate process from your game simulation. It's a neat trick, 
but more advanced, especially in Python. 

But while we're talking about game loops, another antipattern one should avoid
as much as possible is `while True:`. The problem with `while True` is that the
only way out of the loop is via break or a return, which means if you need to 
keep a consistent state by finishing your simulation loop, you're out of luck.

{ ^ Slide v }

By adding a `running` variable to the loop, you can end the loop in a graceful 
way. Your simulation finishes the current loop, ends it via the False value, 
and then can do any clean up that particular game loop needed.

The last antipattern is nested loops. We all know in Python flat is better than
nested but in some ways, nesting things is still easier in its own way. That 
is, until your game scenes get more complicated. Then managing when you enter 
and exit various loops can become a nightmare.

The solution is a full repertoire of possible design patterns for your game
scenes.
