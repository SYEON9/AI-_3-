import random
print(random.randint(0,100))     #0~100까지 정수 중 하나를 반환
print(random.uniform(0,1))       #0~1까지 균등 분포에서 샘플링


import time 
start=time.time()                #현재 시각
time.sleep(1)                    #1초 기다리기
print(time.time()-start)         #지난 시간 구하기


#import threading
def print_function():
    print("사실, 파이썬은 GIL 때문에 사실상 싱글 쓰레드이다.")
    time.sleep(1)

thread = threading.Thread(target = print_function)  #쓰레드 만들기
Thread.start()                                      #쓰레드 시작
Thread.join()                                       #쓰래드 수거
