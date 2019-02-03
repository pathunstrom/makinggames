The other way to respond to user input is callback functions.

These can take one of two major forms, depending on the framework you're
working with. The first is an explicit publisher-subscriber relationship where
the object watching called a method on the object its watching and provides it
a callable which gets called when the event happens.

Anyone who has worked in javascript would recognize this pattern from the
addHandler method on most objects.

Alternatively, some frameworks have you name your handlers something specific,
like on_update, and pass in the relevant parameters for the event type.

This model is neat because you more or less get (almost) instant access to
event results and mostly don't need to worry about when and where in your loop
you check your events.

It adds a complication though, in that you must coordinate your responses
somewhere other than in your callbacks.

A handy pattern I like to use is a Controller object that handles your hardware
events and provides attributes to control various bits of the game.

