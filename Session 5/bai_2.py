teencode = {
    "vl": "vãi lúa",
    "vk": "vợ",
    "Duy": "óc chó",
    "Hà": "Đẹp trai",
    "Nguyệt Anh": "Gấu cũ của Duy",
    "HG": "Gấu cũ của Hà"
}

while True:
    for k in teencode:
        print(k, end= "\t")

    code = input("nhập từ bạn muốn tra:")

    if code in teencode:
        print("Nghĩa của từ đó là:", teencode[code])
    else:
        print("làm gì có từ đấy")
        print("*" * 20)
        add = input("bạn có muốn thêm từ mới? Y/N").upper()
        print("*" * 20)
        if add == "Y":
            new_word = input("Nhập nghĩa của từ mới:")
            print("*" * 20)
            teencode[code] = new_word
            print(code, "nghĩa là", new_word)  
        else:
            print("không thèm nhập thì thôi")
            break





# input("nhập từ muốn tra cứu:")
