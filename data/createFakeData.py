from barnum import gen_data
import random
import pandas as pd
import datetime

"""
creates a fake set of popular products 
being sold by the Blooth store 
to company customers.
"""

humans = []
for i in range(100):
    humans.append(
        [
            gen_data.create_name(full_name=False),
            str(gen_data.create_birthday(min_age=18, max_age=65)),
            gen_data.create_company_name(biz_type='Generic'),
        ]

    )
    humans.append(
        [
            gen_data.create_name(full_name=False),
            str(gen_data.create_birthday(min_age=30, max_age=50)),
            gen_data.create_company_name(biz_type='Generic'),
        ]

    )
    humans.append(
        [
            gen_data.create_name(full_name=False),
            str(gen_data.create_birthday(min_age=30, max_age=39)),
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
for i in range(2345):
    sel = random.sample(humans, 1)[0]
    units = random.randint(1, 50)
    product = random.sample(products.keys(), 1)[0]
    unitprice = round(random.uniform(products[product][0], products[product][1]), 2)
    salesdata.append(sel + [
        str(gen_data.create_date(past=True, max_years_future=0, max_years_past=1)),
        product,
        units,
        unitprice,
    ])

df = pd.DataFrame(salesdata)
columns = ['name', 'birthday', 'customer', 'orderdate', 'product', 'units', 'unitprice']
df.columns = columns

# df.to_json('blooth_sales_data_".json', orient='records')
df.to_json('blooth_sales_data_2.json', orient='records', date_format="%m/%Y/%dT%I:%M:%S%p+0900")
# df.to_html('blooth_sales_data.html')

df['birthday'] = df['birthday'].map(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))
df['orderdate'] = df['orderdate'].map(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f"))
# df.to_csv('blooth_sales_data.csv', index=False)
df.to_csv('blooth_sales_data_2.csv', index=False, decimal=',', sep=";")
df.to_csv('blooth_sales_data_3.csv', index=False, decimal=',', sep=";", date_format="%m/%Y/%dT%I:%M:%S%p+0900")
# xlsxwriter = pd.ExcelWriter('blooth_sales_data.xlsx',
#                             engine='xlsxwriter',
#                             datetime_format='dd.mm.yyyy hh:mm:ss',
#                             date_format='dd.mm.yyyy'
#                             )
# df.to_excel(xlsxwriter, index=False)
