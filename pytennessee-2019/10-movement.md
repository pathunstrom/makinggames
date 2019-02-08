While we discuss modeling, let's talk about how to do movement.

    pygame.sprite.Sprite.rect
    ppb.BaseSprite.position
    pyglet.sprite.Sprite.position

Every game object ends up with a position of some kind. In pygame, it's that
rect attribute *'*. In ppb and pyglet, it's the position attribute. To simulate
movement, you need to update this value a little bit over time.

In most tutorials, they have you use the framerate of your game.

    ppb
    
    def on_update(self, update_event, signal):
        self.position += (0, 1)

    pygame
    
    def update(self):
        self.rect.move_ip(0, 1)

In both of these examples, we're moving one unit to the right each frame. In
ppb, a unit is arbitrary by default, in pygame it is usually equivalent to one
pixel. *'*

This is fine, and will get you started, but it's has an extremely
subtle catch: If your game loop is running slow, *'* say because rendering is
slowing down your game loop, *'* your movement is going to be slower. And if
it's running fast, the opposite. 

This was a problem with some much older graphical computer games when moved to
newer hardware: As the clock speed accelerated, so did the games, to the point
of unplayability. *'* In fact, this behavior is part of why Space Invaders gets
harder as you play: Fewer enemies meant the loops ran faster.

So, unless you plan on leaning into this quirk, let's talk about a better way
that lets your simulation keep working even if you're on a significantly faster
or slower system.

    time delta

If anyone here knows basic physics, the solution should be obvious: We write our
code in context of time. In most tutorials, you'll come across a variable `td`
or `time_delta`. We tend to measure it in seconds, and usually this becomes a
parameter to your update function.

    pygame
    
    td = clock.tick(30)
    group.update(td)
    
    def update(self, td):
        self.rect.move_ip(0, 1 * td * self.speed)
    
    ppb
    
    def on_update(update_event, signal):
        self.position += Vector(0, 1).scale(self.speed * update_event.time_delta)

By doing this, you'll move the same distance in game based on time, instead of
by framerate, so slowing framerates don't ruin the experience you've designed.
