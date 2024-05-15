from abc import ABC, abstractmethod

class Shape(ABC):
        @abstractmethod
        def sides(self):
                pass


class Rectangular(Shape):
        def sides(self):
                print("My opposite sides are equal")

class Tringle(Shape):
        def sides(self):
                print("My sides are can be equal or not")


triangle = Tringle()
triangle.sides()

rectangle  = Rectangular()
rectangle.sides()