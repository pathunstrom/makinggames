def aabb_collision(b1, b2):
    vertical_distance = abs(max(b1.top, b2.top) - min(b1.bottom, b2.bottom))
    combined_height = b1.height + b2.height
    horizontal_distance = abs(max(b1.right, b2.right) - min(b1.left, b2.left))
    combined_width = b1.width + b2.width
    return (vertical_distance < combined_height and
           horizontal_distance < combined_width)
