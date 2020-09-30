import numpy as np

from domain import InstanceDataset
from domain.dist_calc import calc_dist_with_nearest


class SingleLink:
    def __init__(self, dataset: InstanceDataset):
        self.dataset = dataset
        self.distances = np.zeros(shape=(dataset.rows, dataset.rows))
        self.groups = []

    def calc(self):
        self.distances, next_to_group = calc_dist_with_nearest(self.dataset, self.distances, [], False)
        self.groups = [[next_to_group[0], next_to_group[1]]]
        while self.dataset.rows > 1:
            self.distances, next_to_group = calc_dist_with_nearest(self.dataset, self.distances,
                                                                   [next_to_group[0], next_to_group[1]], True)
            print("Shape: ", self.distances.shape)
            print("Instances:", len(self.dataset.instances))
            print('Next to group:', next_to_group)

            added = False
            for group in self.groups:
                if any([a in group for a in next_to_group]):
                    group.extend(list(next_to_group)[0:2])
                    added = True
            if not added:
                self.groups.append(list(next_to_group)[0:2])
            for a in self.groups:
                print(set(a))
        print(self.groups, next_to_group)
