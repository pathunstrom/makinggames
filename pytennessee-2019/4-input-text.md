So let's move on to input. There are numerous strategies and we'll cover a
handful. *'*

1. Text input *'*
2. Event polling
    * like pygame *'*
3. Event callbacks *'*
    * like pyglet, ppb, and arcade. *`*

Starting with a text-based game, we're going to just use the builtin `input`.
*'*

    input("What is your move?\n")

If you don't know how this works, input returns a string that is the response
to the prompt you passed as the parameter to the function. *'*

When doing text based input, you'll want to validate the input, and preferably
transform it into a value that you can use later in your program. A good pattern
for this looks kind of like this. *'*

    output = None
    while output is None:
        value = input("Please choose a square\n")

        try:
            x, y = value.split(",")
            x = ['a', 'b', 'c'].index(x)
            y = ['1', '2', '3'].index(y)
            output = x + (y * 3)
        except ValueError:
            print("Input should be look like 'a, 1'")
            print("X coordinate should be a letter: a, b, or c.")
            print("Y coordinate should be a numeral: 1, 2, or 3.")
    return output

So we:

1. Set an output variable. *'*
2. start a loop predicated on the output variable being set. *'*
3. set up a try/except block. *'*
4. Ask for input and transform it. *'*
5. If it fails, in the except block, we're going to tell the user what they
   should do. *'*

This is more or less all you need to know to start managing input for text
based games, but I also want to cover GUI based games. *'*
