import jsonable


class ProductHistory(jsonable.Type):
    __slots__ = ("is_discounted", "price", "price_before_discount", "process_time")

    def initialize(self, is_discounted, price, price_before_discount, process_time):
        self.price = price
        self.is_discounted = is_discounted
        self.price_before_discount = price_before_discount
        self.process_time = process_time
