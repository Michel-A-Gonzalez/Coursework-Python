from vpython import *

import math

def main():
    # define a ball
    ball = sphere(pos=vector(-5,0,0), radius=0.5, color=color.cyan)
    ball2 = sphere(pos=vector(0,0,0), radius=0.5, color=color.blue)
    #build the container
    wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
    wallL = box(pos=vector(-6,0,0), size=vector(0.2,12,12), color=color.green)
    wallT = box(pos=vector(0,6,0), size=vector(12,0.2,12), color=color.yellow)
    wallB = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color=color.yellow)
    wallF = box(pos=vector(0,0,6), size=vector(12,12,0.2), color=color.red, opacity=0)
    wallBA = box(pos=vector(0,0,-6), size=vector(12,12,0.2), color=color.red)
    # define velocity of the ball
    ball.velocity = vector(25,25,25)
    ball2.velocity = vector(25,25,25)
    #motion motion of the ball
    deltat = 0.005
    t = 0
    ball.pos = ball.pos + ball.velocity * deltat
    ball2.pos = ball2.pos + ball2.velocity * deltat

    while (t < 10):
        rate(50)

        if (ball.pos.x > wallR.pos.x):
            ball.velocity.x = (-1) * ball.velocity.x
        if (ball.pos.x < wallL.pos.x):
            ball.velocity.x = (-1) * ball.velocity.x
        if (ball.pos.y > wallT.pos.y):
            ball.velocity.y = (-1) * ball.velocity.y
        if (ball.pos.y < wallB.pos.y):
            ball.velocity.y = (-1) * ball.velocity.y 
        if (ball.pos.z > wallF.pos.z):
            ball.velocity.z = (-1) * ball.velocity.z
        if (ball.pos.z < wallBA.pos.z):
            ball.velocity.z = (-1) * ball.velocity.z

        if (ball2.pos.x > wallR.pos.x):
            ball2.velocity.x = (-1) * ball2.velocity.x
        if (ball2.pos.x < wallL.pos.x):
            ball2.velocity.x = (-1) * ball2.velocity.x
        if (ball2.pos.y > wallT.pos.y):
            ball2.velocity.y = (-1) * ball2.velocity.y
        if (ball2.pos.y < wallB.pos.y):
            ball2.velocity.y = (-1) * ball2.velocity.y 
        if (ball2.pos.z > wallF.pos.z):
            ball2.velocity.z = (-1) * ball2.velocity.z
        if (ball2.pos.z < wallBA.pos.z):
            ball2.velocity.z = (-1) * ball2.velocity.z

        distance = math.sqrt((ball.pos.x - ball2.pos.x) ** 2 + \
                             (ball.pos.y - ball2.pos.y) ** 2 + \
                             (ball.pos.z - ball2.pos.z) ** 2)

        if(distance < ball2.radius + ball.radius):

           v_1 = ball.velocity

           v_2 = ball2.velocity

           ball.velocity = v_2

           ball2.velocity = v_1
           
        ball.pos = ball.pos + ball.velocity * deltat
        ball2.pos = ball2.pos + ball2.velocity * deltat
        t = t + deltat

main()

