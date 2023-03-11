class Rectangle:

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = (self.width * self.height)
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter

    def get_diagonal (self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return self.diagonal

    def get_picture(self):
        if (self.width or self.height) > 50:
            return f"Too big for picture."
        else:
            pic = ""
            for i in range(self.height):
                pic += "*" * self.width + "\n"
            return pic 

    def get_amount_inside(self, shape):
        if self.width < shape.width or self.height < shape.height:
            return 0
        return (self.width // shape.width) * (self.height // shape.height)

class Square(Rectangle):

    def __init__(self, side):
        super(Square, self).__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
