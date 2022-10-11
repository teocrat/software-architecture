import PoligonalModel
import Flash


class Scene:
    def __init__(self, id):
        self.type_1 = None
        self.type_2 = None
        self.id = id
        self.Models = PoligonalModel
        self.Flashes = Flash

    def method_1(self, type_1):
        self.type_1 = type

    def method_2(self, type_1, type_2):
        self.type_2 = type
