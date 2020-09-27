from typing import List

import jsonable

from productHistory import ProductHistory


class Product(jsonable.Type):
    __slots__ = ("id", "url", "name", "last_process_time", "product_history",)

    def initialize(self, id, url, name, last_process_time, product_history: List[ProductHistory]):
        self.id = id
        self.url = url
        self.name = name
        self.last_process_time = last_process_time
        self.product_history = [ProductHistory(x) for x in product_history]

    def insert_product_history(self, history):
        self.product_history.append(history)

    def __str__(self):
        return str(self.id) + " " + str(self.url) + " " + str(self.name)
