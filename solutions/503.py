def median(series):
    length = len(series)
    if length % 2 == 0:
        pos1, pos2 = int(series.count() / 2), int(series.count() / 2 + 1)
        mev = sorted(series.tolist())
        print(mev[pos1:pos2 + 1])
        return sum(mev[pos1:pos2 + 1]) / 2


print(pd.DataFrame(sales_data['turnover']).agg(median))
pd.DataFrame(sales_data['turnover']).median()