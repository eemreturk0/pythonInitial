def deneme(x=3):
    print(x)


def mydeneme(y):
    y(5)
    print("fff")


mydeneme(lambda : deneme(5))
