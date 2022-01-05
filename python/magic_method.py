
#소멸자
class Student:
    #객체를 소멸할 때 호출한다. 
    #파이썬은 garbage collection으로 메모리를 관리하므로 잘 사용하지 않는다.
    #변수 자체가 포인터 역할을 하므로 del을 사용해도 참조를 명시적으로 삭제하는 것이지 객체를 명시적으로 삭제하는 것이 아니다. 
    def __del__(self):
        self.classes.clear()  #classes set을 비운다. 


#indexing method(__getitem__ / __setitem__)
class DoubleMapper(object):
    def __init__(self):
        self.mapping = {}

    def __getitem__(self, index):                #Indexing get
        return self.mapping.get(index, index*2)  #mapping안에 있으면 index반환. 없으면 index*2 반환.

    def __setitem__(self, index, item):          #Indexing get
        self.mapping[index] = item               #다음 형태로 주어졌을때, mapping이 item을 가진다. 

mapper = DoubleMapper()
print(mapper[10], mapper[1,2])                   #이때, [1,2]는 [(1,2)]이다.
mapper[10] = 15
print(mapper[10], mapper[1,2])
        


#Length method
class Dataset:
    def __init__(self, data, times = 3):
        self.data = data
        self.times = times

    #객체 내 data의 길이를 구하는 함수를 재정의
    #data길이에 times를 3번 곱한 값을 반환한다. 
    def __len__(self):
        return len(self.data) * self.times

    def __getitem__(self, index):
        if index>len(self):
            raise IndexError()

        return self.data[index % len(self.data)]

dataset = Dataset([10,2,5,2], times = 5)
print(len(dataset))    #20



#__str__
class Student:
    def __init__(self, name:str, sid:int):
        self.name = name
        self.sid = sid

    def __str__(self):
        return self.name + '_' + str(self.sid)

Suyeon_Kim = Student('Suyeon Kim', 20181466)
print(Suyeon_Kim)



#연산자 재정의
class Student:
    def __init__(self, name:str, sid:int):
        self.name = name
        self.sid = sid

    def __add__(self, other):
        return self.sid < other.sid

students = [
        Student("Cho", 1234),
        Student('Ho', 4566),
        Student('Jun', 2267)
        ]

#print(*[student.name for student in sorted(students)])


#함수화 메소드
class AdditionNumber(object):
    def __init__(self, number:int):
        self.numbmer = number

    def __call__(self, number:int):
        return number+self.number

addition_5 = AdditionNumber(5)
print(addition_5(10))
