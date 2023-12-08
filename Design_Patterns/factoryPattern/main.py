from shape_factory import ShapeFactory
from shape import Shape


def main():
    geometryShape: str = str(input("Enter the geometry shape: "))
    geometryObject = ShapeFactory(geometryShape)
    shapeObject: Shape | None = geometryObject.getShape()
    if shapeObject:
        shapeObject.draw()
    else:
        print("Unknown shape")


if __name__ == "__main__":
    main()
