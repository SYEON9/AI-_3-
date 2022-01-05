
#class생성

class Student(object):
    
    #클래스 속성
    #클래스 전체가 공유하는 속성값.
    #"Class.attr" 형태로 접근 가능.
    SCHOOL = "SCH"

    #생성자.
    #magic method의 일종으로 객체를 생성할 때 자동으로 호출된다.
    #일반적으로 객체의 속성을 초기화 하는데 사용한다. 
    #클래스를 생성할 때 생성자에서 요구하는 args를 충족해줘야 한다. 
    #정해진 argument format이 없는 magic method.
    def __init__(self, name:str, sid: int):
        self.name = name                     #self는 객체를 말한다. 
        self.sid = sid                       #그러므로 self.변수는 객체의 변수를 의미한다. 
        self.classes = set()


    #클래스 함수(method)
    #각 객체에 적용이 가능한 함수로 "객체.method(args)"행태로 접근가능.
    def take_class(self, class_name: str) -> None:
        self.classes.add(class_name)

    def drop_class(self, class_name: str) -> None:
        self.classes.discard(class_name)



#객체 생성
suyeon = Student("Suyeon Kim", 20181466)

#속성 출력
print(suyeon.name, "in", Student.SCHOOL)
#메소드 실행
suyeon.take_class("CS101")
suyeon.take_class("CS102")
suyeon.drop_class("CS101")
