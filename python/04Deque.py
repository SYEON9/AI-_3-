#queue

from collections import deque

queue = deque([10,4,12])

queue.appendleft(16)      #left insert
print(queue)
queue.pop()               #right delet
print(queue)

queue.append(20)          #right insert
print(queue)
queue.popleft()           #left delet
print(queue)



#defaultdict
#파이썬 dictionary value에 default값을 key가 없어도 추가할 수 있도록 한다. 
#등장횟수를 셀 때 사용하는 것이 대표적이다. 
from collections import defaultdict
characters = defaultdict(int)
text = "등장횟수를 셀 때 사용하는 것이 대표적이다."
for char in text:
    characters[char]+=1
print(characters)


#Counter
#dictionary처럼 생성 및 관리가 가능하다.
from collections import Counter
c = Counter({"Korean":2, "English":3})
print(c)

c.keys()            #key 반환
c.values()          #value 반환
c["Korean"]         #"Koeran"의 value 반환
list(c.elements())  #모든 요소 반환

c = Counter(korean=2, english=3)   #kwargs로 생성
print(c)

a = Counter([1,1,2,2,2,3])
b = Counter([2,3,3,4])

print(a)
print(a+b)
print(a&b)
print(a|b)
print(a-b)

'''
#NamedTuple
from collections import namedtuple
#새로운 타입을 만들자.
Coords3D = nametuple("Coords3D",['x','y','z'])

point = Coords3D(10,20,z=30)
print(point.x)
print(point[1])
print(*point)
'''

#dataclass
from dataclasses import dataclass
@dataclass
class Coords3D:
    x:float
    y:float
    z:float=0

    def norm(self) -> float:
        return (self.x**2 + self.y **2 + self.z**2)**.5

point = Coords3D(10,20,z=30)
print(point)
print(point.norm())
