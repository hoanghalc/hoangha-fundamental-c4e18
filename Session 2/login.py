import getpass #hide pass
username = "duykhon"
password = "duyochco"
user = input("nhap username vao")
if user != username:
    print("sai ten dang nhap roi")
passw = getpass.getpass("nhap pass vao")
if user == username and passw != password:
    print("sai mat khau roi")
elif user == username and passw == password:
    print("may vao duoc roi")

  

