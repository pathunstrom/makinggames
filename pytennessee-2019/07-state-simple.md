So let's move on to state. No matter what game you make, you'll need some form
of state, and I'm going to show you three object oriented ways to handle it.

We'll start at the simplest: using basic data structures.

    class Player(NamedTuple):
        symbol: str
        is_human: bool
    
    
    board = [None] * 9
    players: Tuple[Player] = (Player(CROSS, True), Player(NAUGHT, False))

In this example, players are just NamedTuples that are marked which symbol they
play and whether it's a human player. *'* Remember these samples are
tic-tac-toe, so "X"s and "O"s or as I named the constants, NAUGHTs and CROSSes. *'*

This is a really great system when you're throwing something together. *'* I 
built the text based version of this in about an hour. It also allows most of 
your algorithms over arrays to be effective. You also get access to slice
syntax.

    def check_horizontal(first, board):
        if board[first] is None:
            return False
        return all(board[first] == space for space in board[first:first + 3])

This method of storing things in existing data structures is almost never a bad
idea, but extending those structures is often tricky, so eventually, you'll
want want to move onto something a little more built for the job.
