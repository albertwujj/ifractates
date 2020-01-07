from manimlib.imports import *

class ToPlaceAtAGivenPointAStraightLineEqualToAGivenStraightLine(Scene):
    def construct(self):
        circle1 = Circle(color=BLUE, radius=1.0)
        circle2 = Circle(color=BLUE, radius=1.2)
        meeting_of1 = circle1.get_boundary_point([.1,.1,.1])
        meeting_of2 = circle2.get_boundary_point([.1,.1,.1])
        offset = meeting_of1 - meeting_of2
        circle2.move_arc_center_to(circle1.get_arc_center() - offset)
        self.play(
            ShowCreation(circle1),
            ShowCreation(circle2),
        )