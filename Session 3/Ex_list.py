sothich = ["choi", "an", "ngu"]
print(sothich)
n = input("nhap so thich moi vao")
sothich.append(n)
print(*sothich, sep=', ')
a = int(input("vi tri muon thay doi:"))
vitri = a - 1
sothich[vitri] = n
for index, item in  enumerate(sothich):
    print("{0}.{1}".format(index +1, item))
