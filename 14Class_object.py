class Car:
    #속성
    engineCc=0
    door=0
    carType=None
    
    #생성자
    def __init__(self,engineCc,door,carType):
        #멤버변수 초기화
        self.engineCc=engineCc
        self.door=door
        self.carType=carType
    
    #Method
    def display(self):
        print("자동차는 %d cc이고, 문은 %d개, 타입은 %s"
              %(self.engineCc,self.door,self.carType))


car1 = Car(3000,4,'suv')
car2 = Car(5000,2,'truck')
car1.door=10
car1.display()
car2.display()
del car2

import datetime
from datetime import date, time

today = date(2023,5,5)
print(today, today.year, today.month, today.day)
w = today.weekday()
print(w)

currTime = time(21,4,30)
print(currTime, currTime.hour, currTime.minute, currTime.second)
print(currTime.isoformat)