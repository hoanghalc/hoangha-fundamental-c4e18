sheep = [5,10,15,20,35,40]
print('hello my name is Ha and these is my ship size:', sheep, sep=', ')
biggest = max(sheep)
print('my biggest ship is:', biggest, 'let shear it')
sheep.remove(biggest)
print('after shearing, here is my flock:', sheep)
month = int(input("how many month?"))
for i in range(1,month+1):
    print('month',i, ':')
    print('one month has passed, now here is my flock:')
    for j in range(len(sheep)):
        sheep[j] += 50
    print(sheep) 
    biggest = max(sheep)
    print("Now my biggest sheep has size", biggest, "lets shear it")
print("My flock has size in total:", sum(sheep))
print("I would get", sum(sheep), "* 2$ =", sum(sheep)*2)


