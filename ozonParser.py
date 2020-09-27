from bs4 import BeautifulSoup


def parse(content):
    soup = BeautifulSoup(content, "html.parser")

    product_name_handler = soup.find("h1", {"class": "b3a8"})
    product_price_handler = soup.find("span", {"class": "b3d"})
    discounted_product_price_handler = soup.find("span", {"class": "b3d b3n5"})
    before_discount_product_price_handler = soup.find("span", {"class": "b3d5"})

    product_name = "Undefined"
    product_price = 0
    product_price_before_discount = 0
    is_discounted_product = False

    if product_name_handler is not None and len(product_name_handler.contents) > 0:
        product_name = str(product_name_handler.contents[0])

    if discounted_product_price_handler is not None and len(discounted_product_price_handler) > 0:
        product_price = int(discounted_product_price_handler.contents[0].replace("₽", "").replace("\xa0", ""))
        if before_discount_product_price_handler is not None and len(before_discount_product_price_handler.contents) > 0:
            product_price_before_discount = int(
                before_discount_product_price_handler.contents[0].replace("₽", "").replace("\xa0", ""))
            is_discounted_product = True
    else:
        if product_price_handler is not None and len(product_price_handler.contents) > 0:
            product_price = int(product_price_handler.contents[0].replace("₽", "").replace("\xa0", ""))

    return {
        "name": product_name,
        "price": product_price,
        "isDiscountedProduct": is_discounted_product,
        "priceBeforeDiscount": product_price_before_discount
    }
