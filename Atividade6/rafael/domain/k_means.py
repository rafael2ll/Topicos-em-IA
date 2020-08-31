import random

import numpy as np
from matplotlib import pyplot as plt

from domain.distance import EuclideanDistance
from domain.models import InstanceDataset, Instance


class KMeans:
    def __init__(self, dataset: InstanceDataset, k: int):
        self.dataset = dataset
        count = [x for x in range(dataset.rows)]
        random.shuffle(count)
        self.centroids = [dataset.get(rand).row for rand in count[0:k]]
        print('Random Centroids: ', self.centroids)

    # re-calculate instance groups and notify if the groups did not change at all
    def rotate(self) -> bool:
        changed = False
        for instance in self.dataset.instances:
            changed = instance.update_group(self.centroids, EuclideanDistance())
        return changed

    def update_centroid(self, idx):
        old_centroid_mean = self.centroids[idx]
        instances = [instance.row for instance in self.dataset.instances if instance.group == idx]
        self.centroids[idx] = np.mean(instances, axis=0).tolist()  # Column means
        return old_centroid_mean != self.centroids[idx]

    def update_all_centroid(self):
        return [self.update_centroid(centroid_idx) for centroid_idx in range(len(self.centroids))]

    def rotate_all(self, max_retries: int = 100):
        for i in range(max_retries):
            self.rotate()
            has_changed = self.update_all_centroid()
            print('New Centroids: {}', self.centroids)
            if not any(has_changed):
                break


if __name__ == '__main__':
    data = [Instance(a) for a in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]]
    dataset = InstanceDataset(data)
    kmeans = KMeans(dataset, 2)
    kmeans.rotate_all(100)
    print(dataset.instances)
    plt.scatter([i.row[0] for i in dataset.instances], [i.row[1] for i in dataset.instances])
    plt.show()
