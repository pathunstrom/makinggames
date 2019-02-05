The other way to respond to user input is callback functions.

These can take one of two major forms, depending on the framework you're
working with. The first is an explicit publisher-subscriber relationship where
the object watching called a method on the object its watching and provides it
a callable which gets called when the event happens.

Anyone who has worked in javascript would recognize this pattern from the
addHandler method on most objects.

    class Board:
        
        def __init__(self):
            self.current_symbol = "X"
            self.squares = []
            for x, y in product(range(3), range(3)):
                square = Square(x, y)
                square.listen(ClickEvent, self.set_symbol)
                self.squares.append(square)
        
        def set_symbol(self, click_event):
            event.square.symbol = self.symbol
            if self.symbol == "X":
                self.symbol == "O"
            else:
                self.symbol == "X"

In this sample when I make a square, I also register through this listen
function for a `ClickEvent` so I can set the value for that square.

Alternatively, some frameworks have you name your handlers something specific,
like on_update, and pass in the relevant parameters for the event type.

This model is neat because you more or less get (almost) instant access to
event results and mostly don't need to worry about when and where in your loop
you check your events.

It adds a complication though, in that you must coordinate your responses
somewhere other than in your callbacks.

A handy pattern I like to use is a Controller object that handles your hardware
events and provides attributes to control various bits of the game.

