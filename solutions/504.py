import datetime

def dfunc(series):
    year = series.apply(lambda x: x.year).sum()/series.count()
    dayofyear = series.apply(lambda x: x.dayofyear).sum()/series.count()
    date = datetime.datetime(
        year=int(year), month=1, day=1) + datetime.timedelta(
        days=int(dayofyear))
    return date

mbirth = sales_data['birthday'].agg(dfunc)
print(mbirth)

# ca. Gegenprobe nur mit Jahr
sales_data['birthday'].apply(lambda x: x.year).sum()/sales_data['birthday'].count()