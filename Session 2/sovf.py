
# for i in range(1, mystery_int+1):
#     row = [str(i)]
#     for j in range(2, mystery_int+1):
#         row = row + [str(i*j)]
#     print('\t'.join(row))

# num = int(input('enter a number:'))


# for row in range (num):
#     for column in range(num):
#         if (row + column) % 2 == 0:
#             print(1,end='  ')
#         else:
#             print(0,end='  ')

#     print('\n')

from turtle import *
color("red")
for i in range(4):
        left(30)
        forward(50)
        right(60)
        forward(50)
        right(120)
        forward(50)
        right(60)
        forward(50)
        right(60)
mainloop()