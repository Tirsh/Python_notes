from controller.arg_parser import ArgParser
from repository.data_collector import DataCollector
from settings.settings import DATA_FILE


class Controller:
    def __init__(self, args):
        self.args = args
        self.arg_parser = ArgParser(self.args)
        self.collector = DataCollector(DATA_FILE)

    def run(self):
        self.arg_parser.action()
