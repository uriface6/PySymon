import msvcrt
from inputClass import InputOutputClass
from myException import MyException
import constant


class CmdClass(InputOutputClass):

    def initGame(self):
        print("Welcome to Shumzy&Leib Symon!!!!")
        print("To start new game anter any key, to exit enter x (any time): ")
        is_unusual_char, usr_input = self.myGetch()
        # print("user input is: " + usr_input)

        if usr_input == constant.EXIT_CHAR:
            raise MyException("Bye Bye")

    def getUserInput(self) -> int:
        is_unusual_char, usr_input = self.myGetch()
        # print("user input is: " + usr_input)

        if is_unusual_char:
            print(usr_input)
            if usr_input == constant.UP_CHAR:
                return constant.UP_INT
            elif usr_input == constant.RIGHT_CHAR:
                return constant.RIGHT_INT
            elif usr_input == constant.DOWN_CHAR:
                return constant.DOWN_INT
            elif usr_input == constant.LEFT_CHAR:
                return constant.LEFT_INT
        elif usr_input == constant.EXIT_CHAR:
            raise MyException("Bye Bye")
        else:
            # raise MyException("ERROR: Incorrect char!!!")
            print("please enter correct input")
            return self.getUserInput()

    def symonOutput(self, output_option: int):
        pass

    def myGetch(self):
        is_unusual_char = False
        usr_input = msvcrt.getwche()
        if usr_input == '\000' or usr_input == '\xe0':
            # print("unusual char")
            usr_input = msvcrt.getwche()
            is_unusual_char = True
        return is_unusual_char, usr_input

    def lose(self):
        print("You Lose")
