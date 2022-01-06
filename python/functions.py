CONSTANT = 10

def add(num1: int, num2: int):
    return num1 + num2


#import문은 import된.py 파일을 처음부터 끝까지 실행시키므로 특정 모듈만 실행시키
#고 싶다면 __name__()을 사용하면 된다.
if __name__ == "__main__":
    print("Import 문은 global 코드 전체를 실행한다.")

