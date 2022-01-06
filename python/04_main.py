import functions
print(functions.add(1,2))

'''만약 상위 디렉토리에 functinos.py가 있다면 어떻게 될까?
#폴더 내.py파일
import directory.functions 
print(directory.functions.add(1,2))

#as로 별칭만들기
import directory.functions as func
print(func.add(1,2))

#from으로 특정 부분 import
import directory import functions
print(functions.add(1,2))

#특정 함수 import
from directory.functions import add
print(add(1,2))

#*로 모두 import. 권장하지 않는다.
from directory.functions import *
print(add(1,(CONSTANT)))
'''
