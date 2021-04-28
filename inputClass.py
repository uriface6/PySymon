from abc import ABC, abstractmethod


class InputOutputClass(ABC):

    @abstractmethod
    def initGame(self):
        pass

    @abstractmethod
    def getUserInput(self) -> int:
        pass

    @abstractmethod
    def sequenceOutput(self, output_option: int):
        pass

    @abstractmethod
    def lose(self):
        pass
