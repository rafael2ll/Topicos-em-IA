from domain.separators.abs import Separator


class SemicolonSeparator(Separator):

    def get_separator(self) -> str:
        return ';'
