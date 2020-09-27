from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import pandas as pd

from datetime import datetime


def create_report(products):
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template("ozonreport.html")

    rows = []
    for product in products:
        for history in product.product_history:
            data_row = {"id": product.id,
                        "url": product.url,
                        "name": product.name,
                        "process_time": history.process_time,
                        "price": history.price,
                        "is_discounted": history.is_discounted}
            rows.append(data_row)

    df = pd.DataFrame(rows)

    report = df.pivot_table(index=["id","url","name","process_time"], values=["price","is_discounted"])

    report.head()

    template_vars = {"title": "Ozon reports" + str(datetime.now()),
                     "products": report.to_html()}

    html_out = template.render(template_vars)

    HTML(string=html_out).write_pdf("report.pdf")