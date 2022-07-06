from turtle import *
from datetime import datetime #현재 시각을 확인하는 모듈
speed(0)

def h(): #home을 더 편하게
    penup()
    home()
    pendown()

def border(): #시계 테두리                                                                                                                                                                                                                                                                                                                                                                                                                      
    penup()
    pensize(5)
    sety(-300) #(0,0)을 중심으로 r=300인 원을 그리기 위해서
    pendown()
    circle(300)
    penup()
    sety(-317)
    pendown()
    pensize(23)
    circle(317)
    pensize(1)
    h()

def square(): # 70x70틀, 숫자 만들때 활용
    penup()
    setpos(xcor()-35,ycor()-35) #현재위치를 반환하여 x,y 둘다 -35씩 이동
    pendown()
    for i in range(4):
            forward(70)
            left(90)
    h()

def clock_second(): #초침 생성
    global now_secend
    global second_hand
    second_hand = Turtle() #초침 터틀 생성
    s = Shape("compound") #초침 터틀 모양 설정
    s1 = ((0,0),(0,100))
    s.addcomponent(s1,"dimgrey")
    register_shape("second hand",s)
    second_hand.shape("second hand")
    second_hand.shapesize(1,2.5,1) # 길이,두께조절
    now = datetime.now()
    now_secend = now.second #현재 xx초 반환
    second_hand.right(now_secend * 6 - 90) #시침의 각도 조절

def clock_minute(): #분침 생성
    global now_minute
    global minute_hand
    minute_hand = Turtle() #분침 터틀 생성
    m = Shape("compound") #분침 터틀 모양 설정
    m1 = ((0,0),(0,100))
    m.addcomponent(m1,"dimgrey")
    register_shape("minute hand",m)
    minute_hand.shape("minute hand")
    minute_hand.shapesize(1,2.3,3) # 길이,두께조절
    now = datetime.now()
    now_minute = now.minute #현재 xx분 반환
    minute_hand.right(now_minute * 6 - 90) #분침의 각도 조절

def clock_hour(): #시침 생성
    global now_hour
    global hour_hand
    hour_hand = Turtle() #시침 터틀 생성
    h = Shape("compound") #시침 터틀 모양 설정
    h1 = ((0,0),(0,100))
    h.addcomponent(h1,"dimgrey")
    register_shape("hour hand",h)
    hour_hand.shape("hour hand")
    hour_hand.shapesize(1,1.5,6) # 길이,두께조절
    now = datetime.now()
    now_hour = now.hour #현재 xx시 반환
    now_minute = now.minute #현재 xx분 반환
    if now_minute < 10:  # 가중치 설정, 시침의 각도 조정
        addition_value = 0
    elif now_minute < 20:
        addition_value = 5
    elif now_minute < 30:
        addition_value = 10
    elif now_minute < 40:
        addition_value = 15
    elif now_minute < 50:
        addition_value = 20
    elif now_minute < 60:
        addition_value = 25
    hour_hand.right(now_hour * 30 + addition_value - 90) #가중치를 적용하여 시침의 각도 조정

def frame(): #시각 애니메이션
    global now_minute
    global now_secend
    now_minute = now_minute % 10
    second_hand.right(6) #초침을 이동
    now_secend += 1
    if now_secend == 60: #분침을 이동
        now_secend = 0
        minute_hand.right(6)
        now_minute += 1
        if now_minute == 10: #시침을 이동, 분침에 따라 각도 조절
            now_minute = 0
            hour_hand.right(5)
    ontimer(frame,1000) #초당 한번씩 frame함수 실행 (재귀함수와 유사)

def check_minute():#분침을 조금 더 정확하게 확인할 수 있도록
    penup()
    sety(-300)
    pendown()
    for i in range(1,61):
        circle(300,6) #총 60개의 선을 그리기 360/60 = 6
        re = heading() #현재 각도 저장
        setheading(towards(0,0)) #(0,0)을 보도록 설정
        penup()
        forward(15)
        pendown()
        if i % 5 == 0: #정시는 더 진하게 표시
            pensize(3)
            forward(10)
            penup()
            back(25)
            pendown()
            pensize(1)
        else:
            forward(10)
            penup()
            back(25)
            pendown()
        setheading(re) #다시 원래 각도로 복귀
    h()
    pencolor("grey")
    dot(10)
    pencolor("black")

def decoration(): #장식
    penup()
    goto(0,-140)
    pendown()
    write("good day",align="center",font=("Arial",10,"bold")) #여백의 장식
    hideturtle() #거북이 지우기

def clock(): #시계 그리기
    clock_second() #초침 그리기
    clock_minute() #분침 그리기
    clock_hour() #시침 그리기
    frame() #시계 애니메이션
    border() #시계태두리 그리기
    for i in range(30,361,30): # 각 숫자를 배치할 위치로 이동 후 숫자배치
        left(90)
        right(i)
        penup()
        forward(230)
        setheading(0)
        pendown()
        num_list[i//30 - 1]() #숫자 함수 리스트에서 숫자를 가져와서 숫자 배치
    check_minute() #분침 확인용
    decoration() #장식 그리기

def One(): #70x70, 숫자 1을 표현
    pensize(5)
    sety(ycor()+23)
    sety(ycor()-46)
    pensize(1)
    h()

def Two(): #70x70, 숫자 2를 표현
    pensize(5)
    penup()
    setpos(xcor()-20,ycor()+20)
    pendown()
    forward(30)
    penup()
    sety(ycor()-20)
    pendown()
    circle(10,180)
    penup()
    sety(ycor()-20)
    pendown()
    forward(20)
    circle(10,90)
    forward(10)
    left(90)
    forward(40)
    pensize(1)
    h()

def Three(): #70x70, 숫자 3을 표현
    pensize(5)
    penup()
    setpos(xcor()-20,ycor()+20)
    pendown()
    forward(30)
    penup()
    sety(ycor()-20)
    pendown()
    circle(10,180)
    penup()
    sety(ycor()-20)
    pendown()
    forward(25)
    back(25)
    penup()
    sety(ycor()-20)
    pendown()
    right(180)
    circle(10,180)
    penup()
    sety(ycor()-20)
    pendown()
    forward(30)
    pensize(1)
    h()

def Four(): #70x70, 숫자 4를 표현
    pensize(5)
    penup()
    setx(xcor()+5)
    pendown()
    sety(ycor()-23)
    sety(ycor()+46)
    right(125)
    forward(38)
    left(125)
    forward(36)
    pensize(1)
    h()

def Five(): #70x70, 숫자 5를 표현
    pensize(5)
    penup()
    setpos(xcor()+20,ycor()+20)
    pendown()
    back(35)
    right(90)
    forward(20)
    left(90)
    forward(25)
    penup()
    sety(ycor()-20)
    pendown()
    circle(10,180)
    penup()
    sety(ycor()-20)
    pendown()
    forward(25)
    pensize(1)
    h()

def Six(): #70x70, 숫자 6을 표현
    pensize(5)
    penup()
    setpos(xcor()+18,ycor()+20)
    pendown()
    back(27)
    left(180)
    circle(10,90)
    forward(20)
    circle(10,90)
    forward(20)
    circle(10,180)
    forward(30)
    pensize(1)
    h()

def Seven(): #70x70, 숫자 7을 표현
    pensize(5)
    penup()
    setpos(xcor()-15,ycor()+21)
    pendown()
    forward(30)
    right(115)
    forward(50)
    pensize(1)
    h()

def Eighth(): #70x70, 숫자 8을 표현
    pensize(5)
    left(180)
    forward(9)
    circle(10,180)
    forward(20)
    circle(10,180)
    forward(9)
    back(9)
    right(180)
    circle(10,180)
    forward(20)
    circle(10,180)
    pensize(1)
    h()

def Nine(): #70x70, 숫자 9을 표현
    left(180) #6을 거꾸로 하여 실행
    penup()
    setpos(xcor()-35,ycor()-40)
    pendown()
    Six()
    pensize(1)
    h()

def Ten(): #70x70, 숫자 10을 표현
    pensize(5)
    penup()
    setpos(xcor()-18,ycor()+23)
    pendown()
    sety(ycor()-46)
    penup()
    setpos(xcor()+15,ycor()+23)
    pendown()
    right(90)
    forward(14)
    circle(10,90)
    forward(3)
    circle(10,90)
    forward(28)
    circle(10,90)
    forward(3)
    circle(10,90)
    forward(12)
    pensize(1)
    h()

def Eleventh(): #70x70, 숫자 11을 표현
    pensize(5)
    penup()
    setpos(xcor()-12,ycor()+23)
    pendown()
    sety(ycor()-46)
    penup()
    setpos(xcor()+25,ycor()+46)
    pendown()
    sety(ycor()-46)
    pensize(1)
    h()

def twelve(): #70x70, 숫자 12을 표현
    pensize(5)
    penup()
    setpos(xcor()-23,ycor()+23)
    pendown()
    sety(ycor()-46)
    penup()
    setpos(xcor()+15,ycor()+46)
    pendown()
    forward(24)
    penup()
    sety(ycor()-22)
    pendown()
    circle(11,180)
    penup()
    sety(ycor()-22)
    pendown()
    forward(14)
    circle(11,90)
    forward(11)
    left(90)
    forward(33)
    pensize(1)
    h()

num_list = [One,Two,Three,Four,Five,Six,Seven,Eighth,Nine,Ten,Eleventh,twelve] #숫자를 그리는 함수를 모아놓은 리스트

clock()

exitonclick()
