from domain.separators.abs import Separator


class TabSeparator(Separator):

    def get_separator(self) -> str:
        return '\t'
