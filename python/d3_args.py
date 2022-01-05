#1
def test_1(x, y, z):
    print(x, y, z, end = '\n', sep = ',')

test_1(1,2,3)
test_1(x=1,y=2,z=3)
test_1(1, y=2, z=3)
test_1(1,2,z=3)
test_1(z=3, x=1, y=2)


#3
def test_3(*args):
    print(args)
    print(args, type(args))

test_3(1)
test_3(1,2)
test_3(1,2,'hello')


#4-tuple이 아니라 개별 요소를 받아 출력
def test_4(*args):
    print(*args)
    #print(*args, type(*args))    #type(*args)의 경우 하나의 type만 있을 때 가능

test_4(1)
test_4(1,2,"hello")


#5
def test_5(*args):
    for i in args:
        print(i, end=',')
    print()

test_5(1)
test_5(1,2)
test_5(1,2,'hello')

#6
def test_6(*args):
    a = list(args)    #리스트에 args 요소를 넣어 a라는 이름을 붙여준다. 
    a.append(type(args))   #*args는 요소 개별적으로 판단하므로 안됨
    print(*a)         # *를 붙여서 요소 개별적으로 전달

test_6(1)
test_6(1,2)


#7
def test_7(x,y,*args):
    print(x, y, args)
    print(x,y,*args)

test_7(1,2)
test_7(1,2,3)
test_7(1,2,3,'hello')


#8
def test_8(**kwargs):  # *kwargs는 dictionary로 받아들임
    print(kwargs)

def test_9(**kwargs):
    test_8(**kwargs)

test_8(color='red', value=1)
test_9(color='red', value=1)
