
#generator
#요소를 하나씩 생성하여 반환하는 객체
def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1


for i in my_range(5):
    print(i)

#괄호로 Generaotr Comprehension 형태로 선언할 수 있다. 
even_generator = (i*2 for i in range(100))
print(list(even_generator))
