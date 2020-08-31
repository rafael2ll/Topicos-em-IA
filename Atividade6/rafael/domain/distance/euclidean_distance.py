import math

from domain.distance.abs import Distance


class EuclideanDistance(Distance):
    def calc_dist(self, p1, p2) -> float:
        return math.sqrt(sum([(p1[i] - p2[i]) * (p1[i] - p2[i]) for i in range(len(p1))]))
