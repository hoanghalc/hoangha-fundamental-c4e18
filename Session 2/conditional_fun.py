yob = int(input("Nhap nam sinh cua may vao:"))
age = 2018 - yob
print(age)

if age < 10:
    print("con nit")   ; #nếu đã thoả mãn nhánh 1 sẽ bỏ qua các nhánh tiếp thep
elif age <= 20:
    print("thieu nien")
elif age == 22:
    print("may bang tuoi tao")
else:
    print("may gia roi")
print("bye")


