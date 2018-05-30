from random import choice
list_of_word = ["champion", "meticulous", "hexagon"]
word = choice(list_of_word)
chars = list(word)
new_word=[]
for i in range(len(chars)):
    rand = choice(chars)
    chars.remove(rand)
    new_word.append(rand)
print(*new_word)
while True:
    answer = input("cau tra loi cua ban la:")
    if answer == word:
        print("dung roi")
        break
    else:
        print("sai roi")
        break
