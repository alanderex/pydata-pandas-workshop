data2 = pd.read_csv('../data/blooth_sales_data_2.csv', sep=';', decimal=',', parse_dates=['birthday', 'orderdate'])
data2.head()