import abc


class Separator(abc.ABC):

    @abc.abstractmethod
    def get_separator(self) -> str:
        return NotImplemented
