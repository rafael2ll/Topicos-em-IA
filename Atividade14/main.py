import argparse

from domain import parse_dataset, fill_missing_values, summarize
from domain.distance import EuclideanDistance
from domain.models import FillMode, Instance, InstanceDataset
from domain.separators.comma_separator import CommaSeparator

parser = argparse.ArgumentParser(description='Input Args')
parser.add_argument('path', type=str,
                    help='Raw dataset path')

parser.add_argument('--has-header', type=bool, default=False,
                    help='first line contains column name')

args = parser.parse_args()

if __name__ == '__main__':
    separator = CommaSeparator()
    distance = EuclideanDistance()

    dataset, ys = parse_dataset(args.path, separator, args.has_header, hasGroup=True)
    fill_missing_values(dataset, FillMode.MEAN)

    instanceDataset = InstanceDataset([Instance(row=a[1], index=a[0]) for a in enumerate(dataset.data)])

    summarize(instanceDataset, ys)

