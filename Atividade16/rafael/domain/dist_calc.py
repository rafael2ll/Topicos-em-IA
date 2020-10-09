from domain.distance import Distance, EuclideanDistance, ManhattanDistance
from domain.models import VanillaDataset


def calc_dist(dataset: VanillaDataset, distance: Distance):
    dists = []
    for row in dataset.data:
        dists.append([distance.calc_dist(row, other_row) for other_row in dataset.data])
    return dists


if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(calc_dist(VanillaDataset(data, 3, 2, []), ManhattanDistance()))
