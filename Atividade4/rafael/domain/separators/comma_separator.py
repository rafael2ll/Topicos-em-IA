from domain.separators.abs import Separator


class CommaSeparator(Separator):

    def get_separator(self) -> str:
        return ','
