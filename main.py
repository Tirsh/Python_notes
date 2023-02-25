import sys
from controller.controller import Controller

if __name__ == '__main__':
    controller = Controller(sys.argv)
    controller.run()