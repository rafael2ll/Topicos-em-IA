from enum import Enum


class Dataset:
    def __init__(self, data, columns, rows, missing_data):
        self.data = data
        self.missing_values = len(missing_data)
        self.missing_data = missing_data
        self.columns = columns
        self.rows = rows


class FillMode(Enum):
    MEAN = 0
    MODE = 1
