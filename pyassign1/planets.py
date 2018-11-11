import turtle
import math


def oval_tg(L):
    """make the first item in list L draw oral together with others
    """
    t=L[0]
    a=L[1]
    E=L[2]
    T=L[3]
    R=L[4]
    d_t=d%T
    arc=d_t*2*math.pi/T
    c=a*E
    b=a*(1-E**2)**0.5
    t.goto(c+a*math.cos(arc),b*math.sin(arc))


def start(L):
    """start to draw an oval from the east pole
    """
    t=L[0]
    a=L[1]
    E=L[2]
    R=L[4]
    C=L[5]
    t.ht()
    t.pu()
    t.shape("circle")
    t.shapesize(R)
    t.color(C)
    t.fd(a*(E+1))
    t.st()
    t.pd()
    

def main():
    """a module of six planets' moving mode
    """ 
    Sun=turtle.Turtle()
    Sun.shape("circle")
    Sun.shapesize(2)
    Sun.color("black")

    mercury=turtle.Turtle()
    venus=turtle.Turtle()
    earth=turtle.Turtle()
    mars=turtle.Turtle()
    jupiter=turtle.Turtle()
    saturn=turtle.Turtle()

    Mercury=[mercury,45,0.206,88,0.3,"gray"]#name;a;e;T;size;color
    Venus=[venus,70,0.007,224.7,0.5,"yellow"]
    Earth=[earth,90,0.0167,365,0.6,"blue"]
    Mars=[mars,120,0.093,687,0.4,"red"]
    Jupiter=[jupiter,200,0.048,1000,1,"green"]
    Saturn=[saturn,280,0.055,1500,0.8,"brown"]

    stars=[Mercury,Venus,Earth,Mars,Jupiter,Saturn]

    for x in range(6):
        start(stars[x])
    global d    
    for d in range(3000):
        for x in range(6):
            oval_tg(stars[x])
        

if __name__=='__main__':
    main()
