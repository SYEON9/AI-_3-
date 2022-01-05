
#자주 사용하는 간단한 내장함수를 살펴보자. 
#순환 가능한 객체를 대상으로 하는 케이스를 보자.
#sum()
print(sum([1,2,3,4,5]))   #15
print(sum(i for i in range(1, 101) if i % 2 == 0))  #2550 #짝수만 합한다.


#any()
#하나도 참이면 참이다.
print(any([False, True, False]))  #True

#all()
#하나라도 거짓이면 거짓이다. 
print(all([False, True, False]))  #False

#min/max
print(max([7,5,-2,5,8]))   #8
print(min([7,5,-2,5,8]))   #-2


#zip
#2개 이상의 순환 가능한 객체를 앞에서부터 한번에 접근할 때 사용한다. 
seq1 = ['What','is','zip']
seq2 = [True, False, True]
seq3 = [1,2,3,4]             #길이가 안맞을 경우 남는건 버린다. 

for w1, w2, w3 in zip(seq1, seq2, seq3):  #앞에서부터 하나식 빼어 Tuple로 변환
    print(w1, w2, w3)

array = [[1,2,3],[4,5,6],[7,8,9]]

#행단위 접근
for row in array:
    print(row)

#열 단위 접근
for col in zip(*array):
    print(col)



#Lambda Function
#아래 두 함수가 동일한 동작을 한다. 
def add(x,y):
    return x+y

add = lambda x,y: x+y


#map
#순환하는 각 요소에 function을 적용하여 반환한다.
seq = [6,-2,8,4,-5]
list(map(lambda x: x*2, seq))

#filter
#각 요소에 funciton함수를 적용하여 참이 나오는 것만 반환한다.
list(filter(lambda x: x>0, seq))
