# person = ["Quý",20,0,"Vĩnh Phúc",2,["manga","coding"],3,20]

# dictionary
#Create
person = {
    "name": "Quý", 
    "age": 20,
    "ex": 0,
    "fav": ["Manga", "Coding"]
}

# print(person)

# name = person["name"] 
# print(name)

#Add more 
# person["length"] = 20
# print(person)

#Update
# person["length"] = 10
# print(person)

#Delete
# del person["length"]
# key = "length"
# if key in person:             #Kiểm tra phần tử có trong dict hay ko
#     print(person[key])
# else:
#     print("làm gì có mà tìm")

#Duyệt các phần tử trong dict
for k in person:            #Duyệt theo key
    print(k)

for k in person:
    print(k, person[k])

for v in person.values():   #Duyệt theo value
    print(v)

for k, v in person.items(): #Duyệt theo cả key và value
    print(k, v)