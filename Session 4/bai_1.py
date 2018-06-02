from getpass import getpass
username = 'techkids'
password = 'khongdung'
count = 0
while True:
    user = input('tên đăng nhập:')

    if user == username:
        passw = getpass('mật khẩu là:')
        if passw == password:
            print('chuc mung')
            break   #phá vỡ vòng lặp gần nhất
        else:
            print('sai mat khau')  
    else:
        print('sai username')
        user = input('tên đăng nhập:')
    count += 1   
    if count == 3:
        print("nhap sai mat khau qua nhieu")
        break   