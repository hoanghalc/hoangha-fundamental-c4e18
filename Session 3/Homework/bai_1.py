items = ['t-shirt','sweater']
shop = ['ç','r','u','d']
n = input('what do you want')
for item in shop:
    if n == 'r':
        print(items, sep=', ')
        break
    elif n == 'c':
        new_item = input('enter new item:')
        items.append(new_item)
        print(items)
        break
    elif n == 'u':
        pos = int(input('update position:'))
        new_item = input('new item:')
        items.insert(pos-1,new_item)
        print(items)
        break
    else:
        delete = int(input('delete position:'))
        items.pop(delete-1)
        print(items)
        break




        
