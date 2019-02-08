So moving from basic data structures, now we'll talk about object oriented
state modeling.

Most game engines out there have the concept of scenes. A scene is simply a
single section of your game. Things like your menus,*'* or splash screens, *'*
or individual levels. Or if you're _really_ ambitious, sections of levels.

In ppb, you're provided with a BaseScene class that handles holding all of your
game's objects and provides easy access to its members. Otherwise, you'll
probably be hand-rolling a simple container class to keep things in order.

In general, you just want to keep all of the code (and objects) for one part of
your game away from the parts for another so you don't have unintended
interactions.

So that minor note out of the way, let's get into game objects proper. In most
Python game frameworks, we call them Sprites. In good OOP style, each sprite
represents a single game object, and includes hooks for its various behaviors.

        class Square(pygame.sprite.DirtySprite):
        
            def __init__(self, image, position, board, column, row, diagonals):
                super().__init__(board)
                self.image = image
                self.rect = self.image.get_rect(topleft=position)
                self.column = column
                self.row = row
                self.diagonals = diagonals
        
            def selected(self, symbol):
                self.image = symbol
                self.dirty = True

Here we have a square for our tic-tac-toe game. It's quite simple, but as a
sprite it needs an image and a Rectangle. I used the Pygame Surface's get_rect
to get the appropriately sized rectangle, and I tell it which row, column, and
diagonals the square lives on.

Then it has only one behavior we care about: We need to update it when it gets
selected.

This pattern is pretty common in Pygame, often with an included `update` method
(which aren't needed for squares in tic-tac-toe, so not in our example.)

    EXTRA CREDIT: Update Pattern

In general, this pattern is going to get you a long way. I've build games based
on shoot 'em ups, arcade games, board games, and even a miniature action rpg
using exactly this form of state modeling.
