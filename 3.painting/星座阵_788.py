import turtle as t
import time,random  

#六芒星
def LMX(x,y,d):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(60)
    for i in range(3):
        t.fd(d)   
        t.left(120)
    t.penup()
    t.goto(x, -y)
    t.pendown()
    t.seth(-60)    
    for i in range(3):
        t.fd(d)   
        t.right(120)
    t.hideturtle()

#圆
def yuan(r):
    t.penup()
    t.goto(-r*pow(3,0.5)/2, -r/2)
    t.pendown()
    t.circle(r)
    t.hideturtle()

#六个小圆环
def sixy(x,y,r):
    def txyuan(x,y,r):
        t.seth(0)
        y = y - r
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(2)
        t.circle(r)
        t.penup()
        t.goto(x, y+3)
        t.pendown()
        r=r-3
        y = y - r
        t.circle(r)
    t.color("#5daed9") 
    txyuan(x,y,r)
    txyuan(-x,y,r)
    txyuan(-x,-y,r)
    txyuan(x,-y,r)
    txyuan(175,0,r)
    txyuan(-175,0,r)
    t.hideturtle()

#六边形

def lbx(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(6):
        t.fd(180)
        t.left(60)
    t.hideturtle()

#月亮
def yueliang(x,y,r):

    y = y - r
    t.penup()
    t.goto(x, y)
    t.pendown() 
    t.circle(r)
    t.circle(r-10)
    t.hideturtle()
#星座
def xingzuo(r,c,h):
    t.penup()
    t.pencolor("#fdcfad")
    t.goto(-10,-10)
    t.seth(-45)
    t.fd(r)
    t.pendown()
    xz=['♒','♓','♈','♉','♌','♍','♎','♏','♊','♋','♐','♑']
    for i in range(12):
        t.write(xz[(i+h)%12],font=("", c, ""))
        t.penup()
        t.right(90)
        t.circle(-r, 30)
        t.left(90)
        t.pendown()
    t.hideturtle()
    
#星堆
def xingdui(r):
    #大三角形
    for i in range(1,5):
        temp = 3
        t.penup()
        t.goto(0, 0)
        t.seth(i * 90)
        t.pendown()
        t.right(22.5)
        t.fd(r)
        if i==1:
            t.goto(0,3*r-temp)
            t.goto(0,0)
            t.seth(i * 90 + 22.5)
            t.fd(r)
            t.goto(0,3*r-temp)
        elif i==2:
            t.goto(- 3 * r+temp,0)
            t.goto(0, 0)
            t.seth(i * 90 + 22.5)
            t.fd(r)
            t.goto(-3 * r+temp,0)
        elif i==3:
            t.goto(0, -3 * r+temp)
            t.goto(0, 0)
            t.seth(i * 90 + 22.5)
            t.fd(r)
            t.goto(0, -3 * r+temp)
        else:
            t.goto(3 * r+temp,0)
            t.goto(0, 0)
            t.seth(i * 90 + 22.5)
            t.fd(r)
            t.goto(3 * r+temp,0)
        t.hideturtle()

    # 小三角形
    x = pow(((2 * r) ** 2) / 2, 0.5)-8
    for i in range(1,5):
        t.penup()
        t.goto(0, 0)
        t.seth(i * 90)
        t.pendown()

        t.right(22.5)
        t.fd(r)
        if i==1:
            t.goto(x,x)
            t.goto(0,0)
            t.right(45)
            t.fd(r)
            t.goto(x,x)
        elif i==2:
            t.goto(- x, x)
            t.goto(0, 0)
            t.right(45)
            t.fd(r)
            t.goto( - x, x)
        elif i==3:
            t.goto( - x, -x)
            t.goto(0, 0)
            t.right(45)
            t.fd(r)
            t.goto(- x, -x)
        else:
            t.goto(x, -x)
            t.goto(0,0)
            t.right(45)
            t.fd(r)
            t.goto(x, -x)
        t.hideturtle()

#菱形
def lx(rd,l,q,j):
    def Skip(step):
        t.penup()
        t.fd(step)
        t.pendown()
    CLA=['pink','#7ecff1','black']
    for a in range(l):
        t.pu()
        t.goto(0,0)
        t.pendown()
        degree=-360/l*a+q
        t.seth(degree)
        Skip(rd)
        t.begin_fill()
        t.fillcolor(CLA[j])
        t.pencolor(CLA[j])
        t.right(30)
        t.fd(25)        
        LZ=[60,120,60]
        for i in range(3):
            t.left(LZ[i])
            t.fd(25)
        t.end_fill()
    t.hideturtle()
        
#星星
def stars(m):
    CLQ=['pink','#7ecff1']
    for i in range(m):
        a=random.uniform(-m*2,m*2)
        b=random.uniform(-m*2,m*2)
        t.begin_fill()
        t.penup()
        t.goto(a,b)
        t.pendown()
        t.speed(900)
        t.fillcolor(CLQ[m%2])
        t.pencolor(CLQ[m%2])
        t.circle(m/200)
        t.end_fill()
        t.hideturtle()

    #初始化
t.setup(1.0, 1.0, 0, 0)
t.bgcolor("black")
t.pencolor("#7ecff1")
t.hideturtle()

#六芒星和叠加
mt=["#0489D4","#d9f1f1"]
mv=["#6cd1ef","#d9f1f1"]
for i in range (2):
    t.speed(3)
    t.delay(0)
    t.pensize(2-i*1.2)
    t.color(mt[i]) 
    LMX(0,-70,122.5)
    LMX(0,-100,175)
    t.pensize(3-i*1.6)
    t.color(mv[i]) 
    LMX(0,-200,350)
    LMX(0,-220,385)

#圆叠加
nc=["#94d5f0","#acdefa"]
for i in range(2):
    t.speed(13)
    t.pensize(3-i*1.5)
    t.pencolor(nc[i])
    yuan(220+i)
    yuan(250+i)
    yuan(258+i)
    t.pensize(1)
    t.pencolor("#389bc8")
    t.speed(6)
    yuan(100+i)
    yuan(110+i)
    yuan(35+i)
    yuan(30+i)

#六个小圆环
time.sleep(0.5)
t.speed(5)
sixy(86,155,40)

#六边形和叠加效果
BT=["#54B6D8","#f0efeb"]
t.speed(10)
for i in range(2):
    t.speed(5)
    t.delay(0)
    t.color(BT[i])
    t.pensize(3-i*1.6)
    t.seth(-12)
    lbx(-123,-135.88)
    t.seth(0)
    lbx(-90,-155.88)
    t.seth(12)
    lbx(-57,-175.88)

#月亮
t.speed(10)
t.pencolor("#5daed9")
t.pensize(1.3)
ZR=[-150,30,300,120]
for i in range(4):
    t.seth(ZR[i])
    yueliang(0,53,50)

#星座
t.delay(0)
t.penup()
t.goto(-400, 20)
t.pendown()
xingzuo(235,15,0)

#涂抹一层
for i in range(2):
    t.pensize(10-7.7*i)
    t.speed(12)
    t.penup()
    t.goto(0, -254+i*34)
    t.pendown() 
    t.pencolor("black")
    t.seth(0)
    t.circle(254-i*34)


time.sleep(2)
#星座
t.speed(35)
for i in range(15):
    t.pu()
    t.goto(0,-240-i*4.5)
    t.down()
    t.pencolor("black")
    t.pensize(35)
    t.seth(0)
    t.circle(240+i*4.5)
    xingzuo(240+i*4.5,17,i)

time.sleep(1.5)

#星堆
t.speed(15)
t.pencolor("pink")
t.pensize(0.7)
xingdui(30)
time.sleep(2)
t.reset()

#星堆放大
CL=['#7ecff1','pink','#7ecff1','pink']
j=0
for i in range(30,91,20):
    t.delay(0)
    t.pensize(0.1*(i-20)/10+0.7)
    t.pencolor(CL[j])
    t.speed(30)
    xingdui(i)
    time.sleep(1)
    j=j+1
    t.reset()

t.pencolor("pink")
t.pensize(1.4)
t.speed(30)
xingdui(90)

#菱形
t.speed(50)
t.delay(0)
lx(280,8,0,0)
time.sleep(1)
lx(340,24,0,1)
time.sleep(1)
lx(400,8,0,0)
time.sleep(1.5)
lx(280,8,0,2)
lx(340,24,0,2)
lx(400,8,0,2)

time.sleep(0.75)
for i in range(3):
    t.speed(150+i*100)
    t.delay(0)
    lx(380+i*150,12,0,1)
    lx(380+i*150,6,0,0)


#星星
t.speed(20)
stars(51)
stars(100)
stars(301)
stars(590)
 
t.done()
