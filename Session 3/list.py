# food1 = "salad nga"
# food2 = "Chocolate"
# food3 = "so"

# List (array)
#Create
menu = ["salad nga" , "chocolate", "so"]

# # Read
# print(*menu, sep=', ')  # seperator
# print(len(menu)) #Kiem tra so luong phan tu list
# menu.append("thit ga") #them phan tu
# print(menu)

# first_item = menu[-1] # index phan tu
# print(first_item)

# for i in range(len(menu)):
#     # print(1+i,".", menu[i], sep="")#cach 1
#     print("{0}.{1}".format(i+1, menu[i]))
# print("*" * 20)
# for index, item in enumerate(menu):
#     print("{0}.{1}".format(index + 1, item)) #index theo so tt va phan tu
# print("*" * 20)
# for item in menu: # chi duyet theo phan tu
#     print(item)

## Update
menu[2] = "hen"
print(*menu, sep=", ")