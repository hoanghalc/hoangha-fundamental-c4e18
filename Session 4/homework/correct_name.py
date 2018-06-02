name = input('Nhập tên của bạn: ')
name = name.lower()
name = name.title()
name = name.strip()
for i in range(len(name)):
    name = name.replace('  ', ' ')
print('Tên sau khi được chuẩn hoá:', name)
