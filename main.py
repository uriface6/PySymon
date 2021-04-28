import logging
import msvcrt
from gameManager import GameManager
from myException import MyException


def main():

    my_game_manager = GameManager()
    try:
        my_game_manager.gameManager()

    except MyException as m:
        m.ptintMsg()

    except Exception as e:
        logging.exception(e)

    print ("enter any key to exit...")
    msvcrt.getch()


if __name__ == "__main__":
    main()
