import argparse

from domain import parse_dataset, fill_missing_values
from domain.models import FillMode
from domain.separators import SemicolonSeparator, TabSeparator
from domain.separators.comma_separator import CommaSeparator
from utils import dataset_to_csv

parser = argparse.ArgumentParser(description='Input Args')
parser.add_argument('path', type=str,
                    help='Raw dataset path')
parser.add_argument('--separator', type=str, default="comma",
                    help='change the dataset separator style (default: comma) [comma, semicolon, tab]')
parser.add_argument('--has-header', type=bool, default=False,
                    help='first line contains column name')
args = parser.parse_args()

if __name__ == '__main__':
    separator = CommaSeparator()
    if args.separator == 'semicolon':
        separator = SemicolonSeparator()
    elif args.separator == 'tab':
        separator = TabSeparator()
    dataset = parse_dataset(args.path, separator, args.has_header)

    fill_missing_values(dataset, FillMode.MEAN)


    filename = args.path.split("\\")[-1].split("/")[-1].split(".")[0]
    dataset_to_csv(dataset, filename)
