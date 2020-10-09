import argparse

from domain import calc_sswc
from domain import parse_dataset, fill_missing_values, KMeans
from domain.models import FillMode, Instance, InstanceDataset
from domain.separators.comma_separator import CommaSeparator

parser = argparse.ArgumentParser(description='Input Args')
parser.add_argument('path', type=str,
                    help='Raw dataset path')

parser.add_argument('--has-header', type=bool, default=False,
                    help='first line contains column name')

args = parser.parse_args()


def main():
    separator = CommaSeparator()

    dataset = parse_dataset(args.path, separator, args.has_header)
    fill_missing_values(dataset, FillMode.MEAN)
    sswcs = []
    for i in range(2, 5, 1):
        print("{} K={} {}".format(":" * 25, i, ":" * 25))
        instanceDataset = InstanceDataset([Instance(a) for a in dataset.data])
        kmeans = KMeans(instanceDataset, i)
        kmeans.rotate_all()

        print('\n'.join(['Centroid {}: {}'.format(a[0], a[1]) for a in enumerate(kmeans.centroids)]))

        filename = args.path.split("\\")[-1].split("/")[-1].split(".")[0] + "k" + str(i) + "_clustered.csv"

        sswc = calc_sswc(instanceDataset, kmeans)
        sswcs.append(sswc)

        with open(filename, 'w') as f:
            f.write(','.join(['p{}'.format(i) for i in range(instanceDataset.columns)]))
            f.write(',group\n')
            f.write('\n'.join([','.join(str(a) for a in instance.row) + ',' + str(instance.group) for instance in
                               instanceDataset.instances]))

    for i in range(2, 5, 1):
        print("SSWC(K={})= {:.3f}".format(i, sswcs[i - 2]))


if __name__ == '__main__':
    main()
