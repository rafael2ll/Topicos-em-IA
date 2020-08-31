import argparse

from domain import parse_dataset, fill_missing_values, KMeans
from domain.distance import EuclideanDistance
from domain.models import FillMode, Instance, InstanceDataset
from domain.separators.comma_separator import CommaSeparator

parser = argparse.ArgumentParser(description='Input Args')
parser.add_argument('path', type=str,
                    help='Raw dataset path')
parser.add_argument('--nro-clusters', type=int, default=3,
                    help='Nro of clusters')
parser.add_argument('--has-header', type=bool, default=False,
                    help='first line contains column name')

args = parser.parse_args()

if __name__ == '__main__':
    separator = CommaSeparator()
    distance = EuclideanDistance()

    dataset = parse_dataset(args.path, separator, args.has_header)
    fill_missing_values(dataset, FillMode.MEAN)

    instanceDataset = InstanceDataset([Instance(a) for a in dataset.data])
    kmeans = KMeans(instanceDataset, args.nro_clusters)
    kmeans.rotate_all()

    print('\n'.join(['Centroid {}: {}'.format(a[0], a[1]) for a in enumerate(kmeans.centroids)]))

    filename = args.path.split("\\")[-1].split("/")[-1].split(".")[0] + "_clustered.csv"

    with open(filename, 'w') as f:
        f.write(','.join(['p{}'.format(i) for i in range(instanceDataset.columns)]))
        f.write(',group\n')
        f.write('\n'.join([','.join(str(a) for a in instance.row) + ',' + str(instance.group) for instance in
                           instanceDataset.instances]))
