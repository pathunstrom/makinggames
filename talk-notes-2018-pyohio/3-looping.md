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
* Our input tends to come from hardware interupts
* Our state and models exist directly in memory instead of a DB
* Our output is rendered directly, instead of being sent via the
  internet.

So a really basic game can look like this.

While true,
handle input,
update simulation,
render.

This is great for your first game, but `while True` will quickly get in
the way of things. In general, I prefer a boolean to handle my loop for
me. And that'd look more like this.
