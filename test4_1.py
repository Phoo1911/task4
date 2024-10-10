import matplotlib.pyplot as plt

# Coordinates of shape (a) based on visual approximation
shape_a = [
    (0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3),
    (1, 3), (1, 4), (0, 4), (0, 5), (2, 5), (2, 4), (3, 4), (3, 3), (4, 3), (4, 2), (3, 2), (3, 1), (2, 1), (2, 0)
]

# Coordinates for shape (b) - based on visual approximation
shape_b = [
    (3, 0), (3, 2), (2, 2), (2, 1), (1, 1), (1, 2),
    (0, 2), (0, 3), (2, 3), (2, 4), (1, 4), (1, 5), (2, 5), (2, 6), (3, 6), (3, 4), (4, 4), (4, 5),
    (5, 5), (5, 4), (6, 4), (6, 3), (4, 3), (4, 2), (5, 2), (5, 1), (4, 1), (4, 0)
]

# Coordinates for shape (c) - based on visual approximation
shape_c = [
    (3, 0), (3, 1), (2, 1), (2, 3), (1, 3), (1, 1),
    (0, 1), (0, 4), (1, 4), (1, 5), (2, 5), (2, 4), (3, 4), (3, 6),
    (4, 6), (4, 4), (5, 4), (5, 3), (4, 3), (4, 2), (5, 2), (5, 1), (4, 1), (4, 0)
]


# Function to plot shapes and projections
def plot_shapes_and_projections(shapes):
    plt.figure(figsize=(12, 18))

    for idx, shape in enumerate(shapes):
        x_coords, y_coords = zip(*shape)

        # Plot Original Shape
        plt.subplot(len(shapes), 3, idx * 3 + 1)
        plt.plot(x_coords + (x_coords[0],), y_coords + (y_coords[0],), marker="o")
        plt.title(f"Original Shape {(chr(97 + idx)).upper()}")
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')

        # Horizontal Projection
        plt.subplot(len(shapes), 3, idx * 3 + 2)
        plt.plot(x_coords, [0] * len(x_coords), 'ro', label="Horizontal Projection")
        plt.title(f"Horizontal Projection Shape {(chr(97 + idx)).upper()}")
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')

        # Vertical Projection
        plt.subplot(len(shapes), 3, idx * 3 + 3)
        plt.plot([0] * len(y_coords), y_coords, 'bo', label="Vertical Projection")
        plt.title(f"Vertical Projection Shape {(chr(97 + idx)).upper()}")
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')

    plt.tight_layout()
    plt.show()


# Combine the shapes for plotting
shapes = [shape_a, shape_b, shape_c]

# Call the function to plot all shapes and their projections
plot_shapes_and_projections(shapes)