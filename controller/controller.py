from model.note import Note
from repository.data_collector import DataCollector
from settings.settings import DATA_FILE


class Controller:
    def __init__(self, args):
        self.collector = DataCollector(DATA_FILE)

    def run(self):
        pass
