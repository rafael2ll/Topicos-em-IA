from domain.models import FillMode
from domain.models import VanillaDataset
from domain.separators.abs import Separator
from utils import do_type, load_file, mean_col, mode_col


def parse_dataset(path: str, separator: Separator, has_header=False, hasGroup=False):
    data_raw = load_file(path)
    rows_count = 0
    columns_count = -1
    data = []
    groups = []
    missing_values = []
    for row_raw in data_raw:
        if has_header:
            has_header = not has_header
            continue
        row = row_raw.split(separator.get_separator())
        row[-1] = str(row[-1]).replace("\n", "")
        if hasGroup:
            groups.append(do_type(row.pop()))
        row, mv = handle_row(rows_count, row)
        missing_values.extend(mv)
        data.append(row)
        rows_count += 1
        if columns_count < 0:
            columns_count = len(data[0])

    return VanillaDataset(data, columns_count, rows_count, missing_values), groups


def fill_missing_values(dataset: VanillaDataset, fill_mode: FillMode):
    mean_cols = dict()
    mode_cols = dict()
    for missing_pos in dataset.missing_data:
        column = missing_pos[1]
        if fill_mode == FillMode.MEAN:
            try:
                filler = mean_cols.get(column, mean_col(dataset.data, column))
            except TypeError:
                filler = mean_cols.get(column, mode_col(dataset.data, column))

            if column not in mean_cols.keys():
                mean_cols[column] = filler
        else:
            filler = mode_cols.get(column, mode_col(dataset.data, column))
            if column not in mode_cols.keys():
                mode_cols[column] = filler

        dataset.data[missing_pos[0]][column] = filler


def handle_row(pos, row):
    missing_values = []
    for i in range(len(row)):
        row[i] = do_type(row[i])
        if row[i] == '?':
            missing_values.append([pos, i])
    return row, missing_values
