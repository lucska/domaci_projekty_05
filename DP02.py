from turtle import shape, forward, left, right, exitonclick
from math import sqrt


def kresleni_domku (strana):
        forward (strana)
        left (135)
        forward (sqrt (2)*strana)
        right (135)
        forward (strana)
        right(135)
        forward (sqrt(2)*strana)
        right (135)
        forward (strana)
        right (45)
        forward ((sqrt(2)*strana)/2)
        right (90)
        forward ((sqrt(2)*strana)/2)
        right (45)
        forward (strana)

        left (90)
        forward (2*strana)
        return
shape ("turtle")
kresleni_domku (10)
kresleni_domku (50)
kresleni_domku (100)
exitonclick()
