def N(data):
    return [('color: red' if isinstance(x, str) and 'n' in x else '') for x in data]

sales_data.style.apply(N)