import csv

from model.note import Note
from repository.date_time_service import parse_date_time


class DataCollector:
    id_counter = 0

    def __init__(self, data_file):
        self.data_file = data_file
        self.data = None
        self.load_data()

    def __del__(self):
        self.save_data()

    def load_data(self):
        self.data = dict()
        with open(self.data_file, newline='') as csv_file:
            data_read = csv.reader(csv_file, delimiter=';')
            for row in data_read:
                self.data[int(row[0])] = Note(row[1], row[2], parse_date_time(row[3]))
            DataCollector.id_counter = list(self.data.keys())[-1] if len(self.data) > 0 else 0

    def save_data(self):
        with open(self.data_file, 'w', newline='') as csv_file:
            data_writer = csv.writer(csv_file, delimiter=';')
            for key in self.data:
                data_writer.writerow([key, self.data[key].title, self.data[key].message, self.data[key].date_time])

    def get_all(self):
        return self.data

    def get_by_id(self, item_id):
        if item_id in self.data:
            return self.data[item_id]
        else:
            return None

    def add(self, note):
        DataCollector.id_counter += 1
        self.data[DataCollector.id_counter] = note

    def edit(self, item_id, note):
        if item_id in note:
            self.data[item_id] = note
            return True
        else:
            return False

    def delete(self, item_id):
        if item_id in self.data:
            self.data.pop(item_id)
            return True
        else:
            return False
