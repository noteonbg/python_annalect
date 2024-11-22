def adder(*num):
    print("\n 2 Data type of argument:",type(num))
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

def intro(**data):
    print("\n 1 Data type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="x", Lastname="y", Age=22, Phone=1234567890)
intro(Firstname="q", Lastname="z", Email="a@b.com", Country="sd")