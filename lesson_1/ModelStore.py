import IModelChangeObserver
import PoligonalModel
import Scene
import Flash
import Camera


class ModelStore:
    def __init__(self):
        self.models = PoligonalModel
        self.scenes = Scene
        self.fleshes = Flash
        self.cameras = Camera
        self.__changeObservers = IModelChangeObserver

    def get_scene(self, scene):
        pass

    def notify_change(self, i_model_change_observer):
        pass
