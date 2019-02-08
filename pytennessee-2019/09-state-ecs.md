Once you've mastered that, or when you start building bigger games and get
bitten by deep inheritance trees, you'll want to look into one more style of
state models: Entity *'*-Component *'*-System *'*, or ECS.

To break it down into its components, an Entity is each of your game objects.
They function as basic containers, think of either a dictionary or name space as
both work. Every _thing_ that makes up your game is an entity. *'*

Components are _also_ simple objects with data attached. An entity is made up of
its internal components. So if you have a collection of game objects that are
Alive,

perhaps your Alive class will have hit points so you can determine 
when to kill the object.

Similarly, a Flier component might include data on how high, or fast, your
character can go while in the air. *'*

Systems act on objects with the right combination of components. In general,
it's the systems that do things like move your objects around.

I am no master of this pattern, but it's an incredibly useful one that is used
by professional game developers regularly. If you move from Python games into
something like Unity, you'll recognize this pattern.

There's a library written by Katie Silverio called Braga to check out if this
sounds interesting to you.
