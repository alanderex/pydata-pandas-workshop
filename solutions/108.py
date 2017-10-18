sales_data['orderdate_parsed'] = pd.to_datetime(sales_data['orderdate'], format="%m/%Y/%dT%I%:H%M:%S%p+0900")
sales_data