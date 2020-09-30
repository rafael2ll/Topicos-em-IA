import numpy as np

from domain.distance import Distance, ManhattanDistance, EuclideanDistance
from domain.models import VanillaDataset, InstanceDataset

INF = 11111111111111111111111111111111111


def calc_dist(dataset: VanillaDataset, distance: Distance):
    dists = []
    for row in dataset.data:
        dists.append([distance.calc_dist(row, other_row) for other_row in dataset.data])
    return dists


def calc_dist_with_nearest(dataset: InstanceDataset, base_dist_matrix: np.array, changed: [],
                           only_changed: bool = False):
    distance = EuclideanDistance()
    print(
        "=" * 20)
    major_min_dist = (0, 0, INF)
    if not only_changed:
        for i in range(dataset.rows):
            min_dist = (i, 0, INF)
            for j in range(i, dataset.rows):
                d = distance.calc_dist(dataset.instances[i].row, dataset.instances[j].row)
                base_dist_matrix[i][j] = d
                base_dist_matrix[j][i] = d
                if min_dist[2] > d and i != j:
                    min_dist = (i, j, d)
            dataset.instances[i].set_nearest(min_dist)
            if min_dist[2] < major_min_dist[2]:
                major_min_dist = min_dist
    else:
        minor_changed = min(changed)
        major_changed = max(changed)

        base_dist_matrix[minor_changed][major_changed] = INF + 1
        base_dist_matrix[major_changed][minor_changed] = INF + 1

        print("Point:", changed)
        print(minor_changed)
        for i in range(dataset.rows):
            for j in range(i, dataset.rows):
                if i == j:
                    continue
                elif i == minor_changed:
                    cmp_minor_dist = min(base_dist_matrix[c][j] for c in changed)
                    base_dist_matrix[minor_changed][j] = cmp_minor_dist
                    base_dist_matrix[j][minor_changed] = cmp_minor_dist
                    dataset.instances[i].set_nearest((minor_changed, i, cmp_minor_dist))
                    major_min_dist = major_min_dist if cmp_minor_dist < major_min_dist[2] else (
                        minor_changed, j, cmp_minor_dist)
                elif j == major_changed:
                    cmp_minor_dist = min(base_dist_matrix[c][j] for c in changed)
                    original_minor = dataset.instances[i].get_nearest()
                    base_dist_matrix[i][j] = INF + 1
                    if cmp_minor_dist < original_minor[2]:
                        dataset.instances[i].set_nearest((minor_changed, i, cmp_minor_dist))
                    major_min_dist = major_min_dist if cmp_minor_dist < major_min_dist[2] else (
                        minor_changed, i, cmp_minor_dist)
                else:
                    dist = base_dist_matrix[i][j]
                    if dist < major_min_dist[2]:
                        major_min_dist = (i, j, dist)

        new_nearest_to_changed = min([a for a in enumerate(base_dist_matrix[minor_changed])], key=lambda a: a[1])
        dataset.instances[minor_changed].set_nearest(
            (minor_changed, new_nearest_to_changed[0], new_nearest_to_changed[1]))
        dataset.instances[new_nearest_to_changed[0]].set_nearest(
            (minor_changed, new_nearest_to_changed[0], new_nearest_to_changed[1]))
        # base_dist_matrix = np.delete(base_dist_matrix, major_changed, 0)
        # base_dist_matrix = np.delete(base_dist_matrix, major_changed, 1)

        # for i in range(dataset.rows):
        #     x0, x1, x2 = dataset.instances[i].get_nearest()
        #     if x0 > major_changed:
        #         x0 -= 1
        #     if x1 > major_changed:
        #         x1 -= 1
        #     dataset.instances[i].set_nearest((x0, x1, x2))
        # dataset.instances.remove(dataset.instances[major_changed])
        # dataset.rows -= 1

        dataset.instances[major_changed].set_nearest((-1, -1, INF + 1))
    return base_dist_matrix, major_min_dist


if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(calc_dist(VanillaDataset(data, 3, 2, []), ManhattanDistance()))
