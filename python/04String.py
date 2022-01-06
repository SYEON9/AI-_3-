#"\"를 사용하여 특수문자를 활용해보자
text = '\
        이렇게 적으면\
        엔터없이\
        여러 줄을 적어요\
        '
text
print(text)

text = 'print할 때랑 \n평가할 때랑 달라요.'
text
print(text)


#String Functions
text = "this is the Python course"

print(len(text))              #문자열의 길이를 잴 수 있음.
print(text.upper())           #전부 대문자로 변환.
print(text.lower())           #전부 소문자로 변환
print(text.capitalize())      #문자열 시작 문자를 대문자로 변환        
print(text.title())           #단어 시작을 대문자로 변환
print()

test = "    i have \t block\t\n"
print(test)
print(test.strip())           #좌우 공백 제거
print(test.lstrip())          #왼쪽 공백 제거
print(test.rstrip())          #오른쪽 공백 제거

print('1234'.isdigit())         #숫자 형태인지 확인
print('1.24e-3'.isdigit())      #아라비아 숫자만 인식
print("Capitalize".isupper())   #대문자로만 이루어져 있는지 확인
print("lower_case".islower())   #소문자로만 이루어져 있는지 확인


#pattern 
test = 'abc_text_abc_ee'
pattern = 'abc'

test.count(pattern)   #문자열 내 패턴 등장 위치
test.find(pattern)    #문자열 내 패턴 첫 등장 위치
test.rfind(pattern)   #문자열 내 패턴 첫 등장 위치 뒤에서부터
test.startswith(pattern)  #문자열이 패턴으로 시작하는지 확인
test.endswith(pattern)    #문자열이 패턴으로 끝나는지 확인


#split and join
text = "korean abc test \n abc \t ok"
text.split()    #공백으로 나누기
text.split('abc')
' '.join(text.split())
','.join(str(i) for i in range(10))



#formating

#%-formating
print("Art: %5d, Price per Unit: %8.2f" % (453, 59.058))

#String.format
print("Art: {0:5d}, Price per Unit: {1:8.2f}".format(453,59.058))

#naming
print("%(first)5.2f - %(second)5.2f" % {"first":10.2, "second":5.62})
print("{first:5.2f} - {second:5.2f}".format(**{"first":10.2, "second":5.62}))

#f-string
a,b,c = 10,1.745,'sample'
print(f"{a}: {b} - {c}")
print(f"{a}: {c} - {b}")
value = 12.34
print(f"{value}+{value*10}+{value/10}")
print(f"{value*10:.3f}+{value/10:.3f}")


