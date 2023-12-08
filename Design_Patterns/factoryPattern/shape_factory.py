from circle import Circle
from rectangle import Rectangle
from shape import Shape


class ShapeFactory():
    def __init__(self, geometryShape: str):
        self.geometryShape = geometryShape.lower()

    def getShape(self) -> Shape | None:
        if self.geometryShape == "circle":
            return Circle()
        elif self.geometryShape == "rectangle":
            return Rectangle()
        else:
            return None
