from manimlib import *

def get_intersection(mob1, mob2):
    for p1 in mob1.points:
        for p2 in mob2.points:
            if np.abs(p1[0] - p2[0]) < 0.2 and np.abs(p1[1] - p2[1]) < 0.2:
                return np.array([p1[0], p1[1], 0])


class OnAGivenFiniteStraightLineToConstructAnEquilateralTriangle(Scene):
    def construct(self):
        circle1 = Circle(color=BLUE)
        circle2 = Circle(color=BLUE)
        oL = Line(start=ORIGIN, end=LEFT)
        oR = Line(start=ORIGIN, end=RIGHT)
        self.play(
            ShowCreation(circle1),
            ShowCreation(circle2),
        )
        self.play(
            MoveAlongPath(circle1, oL),
            MoveAlongPath(circle2, oR),
        )

        r1 = Line(start=circle1.get_center(), end=circle1.get_right())
        r2 = Line(start=circle2.get_center(), end=circle2.get_left())
        self.play(
            ShowCreation(r1),
            ShowCreation(r2),
        )
        rcircle1 = VGroup(circle1, r1)
        rcircle2 = VGroup(circle2, r2)
        halfr1 = Line(start=r1.get_start(), end=r1.get_center())
        halfr2 = Line(start=r2.get_start(), end=r2.get_center())
        self.play(
            MoveAlongPath(rcircle1, halfr1),
            MoveAlongPath(rcircle2, halfr2),
        )

        intersection_point = get_intersection(circle1, circle2)
        tri_l = Line(start=circle1.get_center(), end=intersection_point)
        tri_r = Line(end=circle2.get_center(), start=intersection_point)
        self.play(
            ShowCreation(tri_l),
            ShowCreation(tri_r)
        )


