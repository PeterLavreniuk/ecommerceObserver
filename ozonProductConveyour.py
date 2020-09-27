from datetime import datetime
from tinydb import TinyDB, Query
import ozonRequester
import ozonParser
import ozonReportCreator
from product import Product
from productHistory import ProductHistory


def process_products(products_ids):
    relevant_data = request_relevant_data(products_ids)
    products = []
    for relevant_product_data in relevant_data:
        product = process_product(relevant_product_data)
        products.append(product)

    report = ozonReportCreator.create_report(products)

    return report


def request_relevant_data(products_ids):
    result = []
    for id in products_ids:
        url = "https://www.ozon.ru/context/detail/id/" + str(id)
        content = ozonRequester.request(url)
        data = ozonParser.parse(content)

        process_time = str(datetime.now())

        history = [ProductHistory(
            data["isDiscountedProduct"],
            data["price"],
            data["priceBeforeDiscount"],
            process_time
        )]

        product = Product(id, url, data["name"], process_time, history)

        result.append(product)

    return result


def process_product(product):
    db = TinyDB("db.json")
    table = db.table("ozon")
    query = Query()

    temp = table.search(query.id == product.id)

    if temp is not None and len(temp) > 0:
        stored_product = Product.from_json(temp[0])
        stored_product.insert_product_history(product.product_history[0])
        stored_product.last_process_time = product.last_process_time

        table.update(stored_product.to_json(), query.id == product.id)

        return stored_product
    else:
        table.insert(product.to_json())
        return product
