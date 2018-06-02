# numb_list = [-1, 2, 6, 9, 3]
# sorted = []

# while numb_list != []:
#     n = min(numb_list)
#     sorted.append(n)
#     numb_list.remove(n)
# print(sorted)

n = input('enter a sequence of number:')
numb = n.strip().split(' ')  # chuyển một loạt string thành list
numb = list(map(int, numb)) # chuyển list string sang int
sorted = []
print(numb)
for i in range(len(numb)-1):
    if numb[i] > numb[i + 1]:
        print("chưa sắp xếp")
        while numb != []:
            n = min(numb)
            sorted.append(n)
            numb.remove(n)
        print('dãy sau khi sắp xếp là:', sorted)
        break
    else:
        print('sap xep roi')

    