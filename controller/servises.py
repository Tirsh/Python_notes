from model.note import Note
from repository.data_collector import DataCollector
from settings.settings import DATA_FILE
from ui.console_interface import show_info, show_all, show_one


class Service:
    def __init__(self):
        self.collector = DataCollector(DATA_FILE)

    def help_info(self, *args):
        show_info()

    def get_all(self, *args):
        show_all(self.collector.get_all())

    def get_by_id(self, *args):
        if type(args[0].isdigit()):
            result = self.collector.get_by_id(int(args[0]))
            if result:
                show_one(result)
        else:
            self.help_info()

    def add_item(self, *args):
        self.collector.add(Note(args[0], args[1]))

    def update_item(self, *args):
        if type(args[0].isdigit()):
            result = self.collector.edit(int(args[0]), Note(args[1], args[2]))
            if result:
                show_one(result)
        else:
            self.help_info()

    def delete_item(self, *args):
        if type(args[0].isdigit()):
            self.collector.delete(int(args[0]))
        else:
            self.help_info()

    SERVICES = {
        "help": [help_info, 1],
        "show-all": [get_all, 2],
        "get": [get_by_id, 3],
        "add": [add_item, 4],
        "update": [update_item, 5],
        "del": [delete_item, 3]
    }
