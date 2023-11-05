from HW_1.service import Point3D, Angle3D


class Texture:
    pass


class Poligon:
    def __init__(self, points: list[Point3D]):
        self.points = points


class PoligonModel:
    def __init__(self, poligons: list[Poligon], textures: list[Texture]):
        self.poligons = poligons
        self.textures = textures


class Flash:
    def __init__(self):
        self.Location = None
        self.Angle = None
        self.color = None
        self.Power = None

    def rotate(self, angle_action):
        pass

    def move(self, point_action):
        pass


class Scene:
    def __init__(self, id_scene: int, models: list[PoligonModel], flashes: list[Flash]):
        self.id_scene = id_scene
        self.models = models
        self.flashes = flashes

    def method1(self, type):
        return None

    def method2(self, type1, type2):
        return None


class PoligonalModel:
    def __init__(self, textures: list[Texture]):
        self.poligons = []
        self.textures = textures
        self.poligons.append(Poligon(Point3D()))


class Camera:
    def __init__(self):
        self.location = None
        self.angle = None

    def rotate(self, angle_action: Angle3D):
        pass

    def move(self, point_action: Point3D):
        pass
