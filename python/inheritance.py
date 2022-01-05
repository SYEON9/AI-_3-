class Student:
    def __init__(self, name:str, sid:int):
        self.name = name
        self.sid = sid
        self.classes = []

    def __str__(self):
        return self.name + "_" + str(self.sid)

    def take_class(self, class_name:str)->None:
        self.classes.append(class_name)


class Master(Student):                          #Student 상속
    def __init__(self, name:str, sid:int, professor:str):
        super().__init__(name, sid)             #Student 클래스 생성자에 접근. 
        self.professor = professor

    def __str__(self):
        return super().__str__() + "_" + str(self.professor)

master = Master("Suyeon Kim", 20181466, "Jaegul Choo")
print(master)
print(super(Master, master).__str__())           #super로 원하는 상위 클래스로 변환
