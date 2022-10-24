import abc


class MoveRotate:
    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def rotate(self):
        pass


class Flash(MoveRotate):

    def __init__(self):
        pass

    def rotate(self):
        pass

    def move(self):
        pass


class Camera(MoveRotate):

    def __init__(self):
        pass

    def rotate(self):
        pass

    def move(self):
        pass


class FabricElements:
    def create_element(self, name):

        if name == "Flash":
            return Flash()

        if name == "Camera":
            return Camera()


def fabric_element(name):
    fabric_element = FabricElements()
    return fabric_element.create_element(name)


print(type(fabric_element('Flash')))
print(type(fabric_element('Camera')))
a = fabric_element('Flash')
a.rotate()
a.move()
b = fabric_element('Camera')
b.move()
b.rotate()
