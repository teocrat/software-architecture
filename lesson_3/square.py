from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, width=height)
        assert isinstance(height, object)
        self.height = height
