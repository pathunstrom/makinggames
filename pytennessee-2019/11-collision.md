Almost everything you do will need to measure collision, even if it's
just checking if the mouse clicked an object.
There's a few really simple collision checks that are available in 2d
games.

The first is circle to circle collision.
The math for this is really
simple:
Given two objects with bounding circles, if the distance
between them is less than the combined length of their radii, then
they've collided.

This only requires two pieces of information from both objects:
* their center points
  (you probably have this because it's the position of your objects)
* the radius needed to contain them

And then one measurement for the distance between them
quick addition to get the combined radii
and one comparison.

    return (c1.center - c2.center).length < c1.radius + c2.radius

Quick and easy, but it's got a failure point:
A circle almost definitely has more space than the object itself.

A slightly more accurate solution is axis aligned bounding boxes,
or AABBs for short.
This is slightly more complex:
Given two objects with AABBs, they are colliding if:
the combined height of the boxes is less than the distance from the
highest side of the higher object to the lower side of the lower object
and
the combined width of the boxes is less than the distance from the
furthest left side of the most left box to the most right side of the
rightmost box.

Mouthful, right?

Thankfully, the code is a bit simpler.
Assuming a standard coordinate plane:

    vertical_distance = abs(max(b1.top, b2.top) - min(b1.bottom, b2.bottom))
    combined_height = b1.height + b2.height
    horizontal_distance = abs(max(b1.right, b2.right) - min(b1.left, b2.left))
    combined_width = b1.width + b2.width
    return vertical_distance < combined_height and horizontal_difference < combined_width

Extending both of these, you can treat single points as circles with a radius of 0
or a box with a width and height of 0, and plug your point into these equations.