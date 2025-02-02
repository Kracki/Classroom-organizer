from random import choice
from utils.table import *


class Openspace:
    def __init__(self, seats: int = 4, number_of_table: int = 6):
        self.tables = [Table(seats) for _ in range(number_of_table)]
        self.number_of_table = number_of_table

    def organize(self, names):
        choice(names)
        for name in names:
            seated = False
            for table in self.tables:
                if table.has_free_spot():
                    if table.assign_seat():
                        seated = True
                        break
            if not seated:
                print(f"No available seats for {name}")

    def display(self):
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i} : {table}")

    def store(self, filename):
        pass
