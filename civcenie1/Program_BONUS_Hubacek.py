class Shape:
    def __init__(self):
        pass

    def draw(self):
        raise NotImplementedError(
            "Not implemented yet. Please implement this method in the subclass."
        )


class Pyramid(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        for i in range(1, self.size + 1):
            print(" " * (self.size - i) + "*" * (2 * i - 1))


class InvertedPyramid(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        for i in range(self.size, 0, -1):
            print(" " * (self.size - i) + "*" * (2 * i - 1))


class Square(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        for i in range(self.size):
            print("* " * self.size)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        for i in range(self.height):
            print("* " * self.width)


def main():
    print("Choose a shape to draw:")
    print("1. Pyramid")
    print("2. Inverted Pyramid")
    print("3. Square")
    print("4. Rectangle")

    choice = int(input("Enter the number of the shape: "))

    if choice in [1, 2, 3]:
        size = int(input("Enter the size of the shape: "))

    if choice == 1:
        shape = Pyramid(size)
    elif choice == 2:
        shape = InvertedPyramid(size)
    elif choice == 3:
        shape = Square(size)
    elif choice == 4:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        shape = Rectangle(width, height)
    else:
        print("Invalid choice!")
        return

    shape.draw()


if __name__ == "__main__":
    main()
