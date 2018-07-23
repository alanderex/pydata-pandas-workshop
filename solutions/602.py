df = sales_data[sales_data.index.weekday.isin({5,6})]
df.groupby(df.index.week).sum()['turnover'].plot.bar(figsize=(10, 4));