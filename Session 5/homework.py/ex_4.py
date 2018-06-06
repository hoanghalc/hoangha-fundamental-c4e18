rabbit = [1]

after_month = int(input('number of month:'))

for i in range(1, after_month + 1):
    rabbit.append(rabbit[i-1] + rabbit[i-2])

for month, pair in enumerate(rabbit):
    print('after {0} month, total pair of rabbit is:{1}'.format(month,pair))