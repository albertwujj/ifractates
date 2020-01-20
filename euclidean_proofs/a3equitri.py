from manimlib import *

from euclidean_proofs.a1equitri import get_intersection

class ToPlaceAtAGivenPointAStraightLineEqualToAGivenStraightLine(Scene):
    def construct(self):
        leg1 = Elbow()
        leg2 = Elbow(angle=-45.)