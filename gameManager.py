import random
from cmdClass import InputOutputClass
from cmdClass import CmdClass
import constant


class GameManager:

    def __init__(self):
        self.sequence = []

    # @staticmethod
    def gameManager(self):
        in_out_class = CmdClass()
        in_out_class.initGame()

        user_input = in_out_class.getUserInput()

        while True:
            GameManager.newGame()

    # @staticmethod
    def newGame(self, in_out_class: InputOutputClass):
        end_game = False

        self.sequence.append(random.randint(0, 4))

        while not end_game:

            in_out_class.sequenceOutput()

            for move in self.sequence:
                usr_input = in_out_class.getUserInput()
                if move != usr_input:
                    in_out_class.lose()
                    self.sequence.clear()
                    end_game = True
                    break

            self.sequence.append(random.randint(0, 4))

    # @staticmethod
    def outputSequence(self):
        pass
