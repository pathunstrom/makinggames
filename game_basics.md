A video game has all the features of a long running process. If you've worked 
with GUIs or a server the basics should come fairly naturally.

Every game is an infinite loop. Inside the loop, you have three major concerns:
handling player inputs, updating the simulation, and rendering.

Handling player input tends to be the first step in your loop so that you can 
have that information when you get into the simulation step. The key point here
is that this is how a player interacts with your game. In an object oriented 
sense, this input IS your player.

Player input is a complex problem. Your first concern when considering input is
how a player interacts with the game. If you make a web game, it could be HTTP 
requests or api calls, or it could use javascript to get various system events 
you get from the document api, like keyboard input, mouse movement, or clicks. 
For a native game, like you would program with python, it will depend 
directly on the engine or framework you're using what tools you have for 
interaction. For example Unity Engine includes an input tool that lets you 
define various controls and let's you operate on the provided values. It also 
includes UI widgets that can handle click events for you. Assuming you're in 
Python, each framework gives you some sort of access to the input hardware.
Pygame has a keyboard module, and PySDL gives you access to the SDL keyboard
functions.

Even after you've defined where your input is coming from, you have a handful
of options on how to use the information. A common pattern you'll find in books
like Inventing Games With Python and Pygame is to use variables to catch every 
input event, modifying the value each time the key state changes. 
WASD movement is a very common tool, in this case you would have variables 
determining if these keys are active, setting and unsetting them as events come 
in. For some purposes, like text input or setting input keys, this is a 
desirable pattern, but it results in many operations each game loop that won't 
be used if you're using it during the simulation. So be cautious in your use of 
this pattern, and realize that sometimes checking state at the time you need 
the information isenough.

The simulation is the fun part. You want to solve problems, this is the place
most of them crop up.

The first thing to focus on is how you're going to model your game. Almost all 
games are object oriented in some sense, but whether you write explicit models 
with methods for movement and other things or write functions that operate on
arrays or maps is going to be a largely personal decision. Most tutorials will 
start you using dictionaries, which is a great place to start.

Once you have your data model picked out and built, you can worry about the
functions involved in simulating. One of the most common of which is going to
be moving objects by updating their positions. There's a lot of decisions to be
made here, specifically if you're using a physics model for movement, which
means forces and torque, mass, velocity and lots of math. The other option is 
called kinematic movement. Instead of a proper physics model, you use code to
program movement directly. A lot of games use some combination of the two.

After movement, the next most common function is going to be collision 
detection. Almost every game uses some sort of collision, even if it's only
used for input. There are a number of different kinds of collision detection,
but for 2D games you'll tend to either circle collisions or axis-aligned 
bounding box based collisions. For higher levels of precision you can also use 
polygon, mask or pixel perfect collision.

Finally you're going to need to define your interactions. If state should
change based on collision, this is where it happens. In general, behaviors will
be based on a small number of game objects and affect their state in some way.

This is a bit abstract, but it's also one of the least likely places you can 
reuse code. To give you more concrete example, my first game was an arcade 
shooter with zombie enemies. Movement could trigger enemies to chase you, but
so could firing a gun. So during the simulation I modeled the sound profile of 
these actions and when the sound was close enough to wake the enemies, I'd 
change their state from wandering to chasing.

The final bit of a game loop is going to be rendering. This includes updating 
the graphics in memory and then actually rendering to the hardware. Simple
games you can do the image updating as part of your simulation, but try not to 
get too used to that. You'll generally be using your library to do this with
various blit and draw functions. Rendering in Python will almost exclusively be
done by an outside library, but note that depending on your choice, this will 
be one of the major bottlenecks to your rendering speed.

So that's the basics of a video game. With this knowledge and a little bit of
experimentation you have enough to build a single screegn game.