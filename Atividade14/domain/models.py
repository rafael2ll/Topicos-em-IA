from enum import Enum

from domain.distance import Distance, EuclideanDistance


class Instance:
    def __init__(self, row, index=0):
        self.row = row
        self.index = index
        self.group = -1

    # Update row group and returns if group has been changed
    def update_group(self, centroids: [], distance_fun: Distance) -> bool:
        current_group = self.group
        means = [distance_fun.calc_dist(self.row, centroid) for centroid in centroids]
        # means to enumerate: (position, mean)
        new_group = min([a for a in enumerate(means)], key=lambda instance: instance[1])[0]
        self.group = new_group
        return new_group == current_group

    def __repr__(self) -> str:
        return '\nGroup: ' + str(self.group) + '\t Row: ' + str(self.row)


class VanillaDataset:
    def __init__(self, data, columns, rows, missing_data):
        self.data = data
        self.missing_values = len(missing_data)
        self.missing_data = missing_data
        self.columns = columns
        self.rows = rows


class InstanceDataset:
    def __init__(self, instances: [Instance]):
        self.instances = instances
        self.columns = len(instances[0].row)
        self.rows = len(instances)

    def get(self, pos: int = 0):
        return self.instances[pos]


class FillMode(Enum):
    MEAN = 0
    MODE = 1


if __name__ == '__main__':
    i = Instance([1, 2, 4])
    for t in range(10):
        g = i.update_group([[5, 6, 7], [12, -1, 15], [1, 2, 5]], EuclideanDistance())
        print(g)
