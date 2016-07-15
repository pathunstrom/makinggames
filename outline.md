1. while True: Your first game
    1. Long running process
    2. Basic loop
        1. Respond to events
        2. Update positions
        3. Draw to the screen
    3. Using seperate x and y positons
2. Loops within loops: You can have a menu?
    1. Loops within loops
    2. Lots of break statements
    3. Same loop as before, just nested
3. Using other opinions: Pygame and others
    1. Sprites
    2. Collision
4. Object Orientation is great: Scenes and Game Objects
    1. The Scene
        1. Object
            1. Set up
            2. App loop
            3. Tear down
        2. System Stack
            1. Call new scenes from inside other scenes.
            2. Manage outer loops with stack frames
    2. Game Objects (Pygame Sprites)
5. The Game Loop Is a Lie: Seperating Concerns
    1. Why fix your simulation to your rendering?
    2. MVC
        1. Listeners
        2. Publishers
        3. Events
6. My First Game Engine: Reusable Code is Awesome
    1. Engine
        1. The common core
        2. Send events to the Engine
        3. Engine manages its own callbacks and sends information to a 
           publisher
    2. Scenes
        1. A publisher
        2. Manages initialization of game objects
        3. Publishes to game objects underneath it.
    3. View (Just another game object)
    4. Controllers (Objects that manipulate other objects)
    5. Game Objects (Don't need to know about other objects.)