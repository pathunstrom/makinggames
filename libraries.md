Now that you have a grasp of how to make a game, I'm going to talk about some
of the Python libraries available to you. I want to be clear: These are not an
exhaustive list. I won't be talking about Kivy or pyglet due to lack of direct 
experience with these libraries. I also don't have more traditional game 
engines like Cocos2d or Pandas3d.

The thing you know about game frameworks and engines is they're very
opinionated. Even well known engines, like Unreal, the Source Engine, and 
Unity, make certain kinds of games easier and harder. I often have talked to 
developers that point out Source is really good at making first person 
perspective games that take place in long corridors. It's an 
oversimplification, but a good example.

In the case of most game frameworks, they're more likely to enforce certain
design patterns over others.

Pygame's opinions are probably the hardest to pin down, but a handful of years 
of experience with the library has proven that while you can model your game in
many ways, using Sprites and Groups are the expected way to organize things.

A Sprite is a class provided by Pygame. It expects you to
include an image, a rect, and an update function. An image is a pygame.Surface
instance. Surface is basically a software buffer for pixel arrays. You can 
manipulate it pixel by pixel, but more likely you're using the draw functions 
and load functions to get the right image on the Surface. A rect is a 
Pygame.Rect which is the most useful class available to you in Pygame. It's an 
implementation of an axis aligned bounding box, with a number of convenience 
functions which makes coding behaviors much nicer. The update function is 
specifically used as a callback during your game loop, and is where all of your
behaviors are expected to be.

You put your sprite objects, which will represent everything from player 
characters to enemies to items and background props, into sprite Groups. A 
group is just a container class, and offers a handful of conveniences. To start 
with: a Group has an update and draw function that operate on every sprite in 
the group. Update lets you call all the update functions with arbitrary 
parameters. Draw will take the rect and image of your Sprites and blit them to
a given surface. The other tool that groups give you is the ability to do 
collision detection against every sprite in the group with one function call, 
returning all the sprites that have collided with the given object.

The last major opinion of pygame is its Clock class. This is the way you rate 
limit your games. Its tick method can take an integer for frames per second, 
which it will to add sleep cycles to maintain the given FPS. The tick method 
also returns the milliseconds since the last call to tick.

Another framework is PySDL2's ext modules. Here, the primary opinion is 
separating your code in game objects and systems. Game objects for PySDL are 
strictly built through composition, each bit of data you need to add will be 
its own container class. If you want to give your game objects a velocity, you 
need to give them a Velocity class as an attribute. A position will need its
own class. An important note is none of these classes can inherit from each 
other or from the same parent class as they will overwrite references to each 
other in the map that PySDL builds for each object.

Systems, on the other hand, are definitions of behavior and are handed game 
objects by the engine. If the object has all of the components the system needs
to operate, the system will update the object, otherwise it ignores it.

The other thing that PySDL does that actually confused me in regards to Python 
is the use of factory patterns for creating sprites, which are components, not 
objects in the PySDL paradigm.

I have far less exprience with PySDL's extension and am not sure exactly how 
well it takes to scenes as I described before, but I am sure that it is 
possible to use those patterns, I just don't know how much effort it will 
require.

The last framework I'm going to discuss is my own: PursuedPyBear.

I designed ppb as a response to Pygame and PySDL because I wanted an engine 
that did the kinds of things I like to do when I write games. As such, ppb is 
designed with a scene managed called engine. This singleton is the central 
dispatch for a Publisher-Subscriber model. Game objects and scenes can send 
event classes to the engine, and the the engine will send them to the 
appropriate scene. Those events are then passed from the Scenes (Which are just 
specialized Publishers) to the game objects that are listening for those
events.

The important thing here is that the Publisher-Subscriber model and a modified
Model-View-Controller is enforced by this engine. You can work around some of
these expectations, but it's going to be a lot more effort.

Your Model will be made up of various game objects, which use a Mix-in pattern
to add necessary attributes to the objects. You can define many objects by 
simply inheriting from the provided mix-ins. The other part of Game Objects are
behaviors, which are function callbacks to be used by the Scenes. A behavior 
can be as simple as updating an attribute on the object, or as complex as 
asking another object for the result of interacting with it.

The goal is to make objects and behaviors very simple to put together so you 
can get to the point of working on your systems as soon as possible.