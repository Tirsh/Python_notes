from controller.arg_parser import ArgParser


class Controller:
    def __init__(self, args):
        self.args = args
        self.arg_parser = ArgParser(self.args)

    def run(self):
        self.arg_parser.action()
