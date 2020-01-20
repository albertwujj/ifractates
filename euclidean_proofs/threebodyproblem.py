from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Circle
from manimlib.animation import Animation
from manimlib.animation.creation import ShowCreation
from manimlib.constants import BLUE, RED, GREEN

import numpy as np

class ThreeBodyProblem(Scene):
    def construct(self):
        G = 9.8

        r1 = np.asarray([10, -10, 0])
        r2 = np.asarray([10, 10, 0])
        r3 = np.asarray([-10, -10, 0])

        for i in range(5):
            r1 = -G*(r1-r2)/(r1-r2)**3 - -G*(r1-r3)/(r1-r3)**3
            r2 = -G*(r2-r3)/(r2-r3)**3 - -G*(r2-r1)/(r2-r1)**3
            r3 = -G*(r3-r1)/(r3-r1)**3 - -G*(r3-r2)/(r3-r2)**3
            circle1 = Circle(color=BLUE, radius=.1, center_of_mass=r1)
            circle2 = Circle(color=RED, radius=.1, center_of_mass=r1)
            circle3 = Circle(color=GREEN, radius=.1, center_of_mass=r1)
            self.play(
                Animation(circle1),
                Animation(circle2),
                Animation(circle3),
            )
        print("ey")
