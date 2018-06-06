prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

for k in prices and stock:
    print(k)
    print('price:', prices.get(k))
    print('stock:', stock.get(k))


total = 0
for k in prices and stock:
    sell = prices[k] * stock[k]
    total += sell
    print(' money you can get from',k,sell,'$' )

print('total money:', total,'$')
