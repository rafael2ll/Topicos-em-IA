import abc


class Distance(abc.ABC):

    @abc.abstractmethod
    def calc_dist(self, p1, p2) -> float:
        return NotImplemented
