from typing import List

from domain.models import VanillaDataset, InstanceDataset


def load_file(path):
    data_raw = open(path, "r")
    return data_raw


def do_type(value: str):
    try:
        v = float(value)
    except ValueError:
        v = value
    return v


def mean_col(data: List, col_number: int):
    rows = []
    value_distinct_count = 0
    for row in data:
        # print(row , col_number)
        if row[col_number] != "?":
            rows.append(row[col_number])
            if row[col_number] not in rows:
                value_distinct_count += 1
    return (sum(rows) / len(rows)) if value_distinct_count > 2 else mode_col(data, col_number)


def mode_col(data: List, col_number: int):
    values = dict()
    max = -1
    mode = None
    for row in data:
        if row[col_number] == '?':
            continue
        count = values.get(row[col_number], 0)
        values[row[col_number]] = count + 1
        if count > max:
            max = count
            mode = row[col_number]
    return mode


def dataset_to_csv(dataset: VanillaDataset, path: str):
    print("Missing values: ", dataset.missing_values)
    output_file = open(path + ".csv", "w")
    for row in dataset.data:
        output_file.write(",".join([str(a) for a in row]))
        output_file.write("\n")


def export_dataset(instanceDataset: InstanceDataset, name):
    filename = name + ".csv"
    with open(filename, 'w') as f:
        f.write(','.join(['p{}'.format(i) for i in range(instanceDataset.columns)]))
        f.write(',group\n')
        f.write('\n'.join([','.join(str(a) for a in instance.row) + ',' + str(instance.group) for instance in
                           instanceDataset.instances]))


if __name__ == '__main__':
    c = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, '?', 12], [4, 8, 6], [4, 9, 6]]
    print(mean_col(c, 1))
    print(mode_col(c, 1))
