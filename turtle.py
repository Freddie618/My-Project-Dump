import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 75
h = 0
for i in range(10000):
  c = colorsys.hsv_to_rgb(h,1,0.8)
  h += 1 / n
  t.color(c)
  t.left(0.5)
  t.fd(1)
  for j in range (4):
    t.left(0.5)
    t.circle(215)
