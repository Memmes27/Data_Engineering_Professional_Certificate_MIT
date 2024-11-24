def add(x,y):
    result = x + y
    print(result)

add(y=5, x=3)

def add_1(*args):
    result = 0
    for x in args:
        result += x
    print(result)

add_1(20,30,40,50,60)

def add_2(*args, **kwargs):
    result = 0
    for x in args:
        result += x
    for k, v in kwargs.items():
        result += v
    print(result)

args = [10,20,30,40,50]
kwargs = {'Mo': 26, 'jasmine': 25, 'ahmed': 27}

add_2(*args, **kwargs)

