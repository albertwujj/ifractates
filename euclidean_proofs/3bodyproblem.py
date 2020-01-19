from manimlib.imports import *

def construct(self):
    G = 9.8
    Gm2 = 42
    Gm3 = 69

    r1 = [1, 1]
    r2 = [2, 2]
    r3 = [3, 3]

    for i in range(10):
        r1 = -Gm2(r1-r2)/(r1-r2)**3 - -Gm2(r1-r2)/(r1-r2)**3
        r2 = -Gm3(r2-r3)/(r2-r3)**3 - -Gm1(r2-r1)/(r2-r1)**3
        r3 = -Gm2(r3-r1)/(r3-r1)**3 - -Gm1(r3-r2)/(r3-r2)**3
        circle1 = Circle(color=BLUE, radius=0.1, center_of_mass=r1)
        circle2 = Circle(color=RED, radius=0.1, center_of_mass=r2)
        circle3 = Circle(color=GREEN, radius=0.1, center_of_mass=r3)
        self.play(
            ShowCreation(circle1),
            ShowCreation(circle2),
            ShowCreation(circle3)
        )
