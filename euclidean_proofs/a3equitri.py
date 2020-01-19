from manimlib.imports import *

from euclidean_proofs.a1equitri import get_intersection

class ToPlaceAtAGivenPointAStraightLineEqualToAGivenStraightLine(Scene):
    def construct(self):
        circle1 = Circle(color=BLUE, radius=1.0)
        circle2 = Circle(color=BLUE, radius=1.2)
        meeting_of1 = circle1.get_boundary_point([.1, .1, 0])
        meeting_of2 = circle2.get_boundary_point([.1, .1, 0])
        offset = meeting_of1 - meeting_of2
        circle2.move_arc_center_to(circle1.get_center() - offset)

        whitelineradiiend = circle2.get_boundary_point([.9, .5, 0])
        redlineradiiend = circle2.get_boundary_point([0.754949, 0.10994949, 0])

        whiteline = Line(start=circle1.get_center(), end=whitelineradiiend, color=WHITE)
        redline = Line(start=circle2.get_center(), end=redlineradiiend, color=RED)

        greenline = Line(start=circle1.get_center(), end=circle1.get_boundary_point([.5, -.22, 0]), color=GREEN)

        print(get_intersection(whiteline, redline))

        finalline = Line(start=redline.start, end=[redline.start[0], redline.start[1] - 1.2, 0], color=PURPLE)

        self.play(
            ShowCreation(circle1),
            ShowCreation(circle2),
        )
        self.play(
            ShowCreation(redline),
        )

        self.play(
            ShowCreation(whiteline),
        )

        self.play(
            ShowCreation(greenline),
        )

        self.play(
            ShowCreation(finalline),
        )