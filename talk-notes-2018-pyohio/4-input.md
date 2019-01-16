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
(A clean example of this won't really fit on a slide.)