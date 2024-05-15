

class Truck:
        def __init__(self, brand, model):
                self.brand = brand
                self.moddel = model


        def move(self):
                print("Moves in the road")



class Ship: 
        def __init__(self, brand, model):
                self.brand = brand
                self.model = model

        def move(self):
                print("Moves in the water")



class Plane:
        def __init__(self, brand, model):
                self.brand = brand
                self.model = model

        def move(self):
                print("Moves in the air")

track = Truck("T", "t")
track.move()


# ship = Ship("S", "s")
# ship.move()


# plane = Plane("P", 'p')
# plane.move()


