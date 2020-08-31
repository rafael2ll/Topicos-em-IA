from domain.distance.abs import Distance


class ManhattanDistance(Distance):
    def calc_dist(self, p1, p2) -> float:
        return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])
