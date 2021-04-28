class MyException(Exception):

    def __init__(self, msg):
        self._msg = msg

    def ptintMsg(self):
        print(self._msg)