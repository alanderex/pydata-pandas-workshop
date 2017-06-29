from barnum import gen_data
import random
import pandas as pd


"""
creates a fake set of popular products 
being sold by the Blooth store 
to company customers.
"""


data = []
for i in range(100):
    data.append(
        [
            gen_data.create_name(full_name=False),
            gen_data.create_birthday(min_age=18, max_age=65),
            gen_data.create_date(past=True, max_years_future=0, max_years_past=2),
            gen_data.create_company_name(biz_type='Generic'),
         ]

    )
    data.append(
        [
            gen_data.create_name(full_name=False),
            gen_data.create_birthday(min_age=30, max_age=50),
            gen_data.create_date(past=True, max_years_future=0, max_years_past=1),
            gen_data.create_company_name(biz_type='Generic'),
        ]

    )
    data.append(
        [
            gen_data.create_name(full_name=False),
            gen_data.create_birthday(min_age=30, max_age=39),
            gen_data.create_date(past=True, max_years_future=0, max_years_past=1),
            gen_data.create_company_name(biz_type='Generic'),
        ]

    )

products = {
    # http://www.insidermonkey.com/blog/the-10-top-best-selling-products-of-all-time-330581/?singlepage=1
    # product: price range (from, to)
    'PlayStation': (200, 300),
    'Lipitor': (10, 12),
    'Corolla': (20000, 25000),
    'Star Wars': (8, 12),
    'iPad': (300, 1100),
    'Thriller record': (8, 20),
    'Harry Potter book': (5, 35),
    'iPhone': (400, 900),
    'Rubik’s Cube': (15, 19),
    'banana': (10, 10),  # how much is a banana, 10 dollars?
}

salesdata = []
for i in range(1000):
    sel = random.sample(data, 1)[0]
    units = random.randint(1, 50)
    product = random.sample(products.keys(), 1)[0]
    unitprice = round(random.uniform(products[product][0], products[product][1]), 2)
    salesdata.append(sel+[
        product,
        units,
        unitprice,
    ])

df = pd.DataFrame(salesdata)
columns = ['name', 'birthday', 'orderdate', 'customer', 'product', 'units', 'unitprice']
df.columns = columns
df.to_csv('blooth_sales_data.csv', index=False)
