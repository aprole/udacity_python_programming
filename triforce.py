import turtle

def draw_triforce(t, order, size):
    if order == 0:
        t.setheading(240)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(2 * size)
        t.left(120)
        t.forward(2 * size)
        t.setheading(240)
    else:
        draw_triforce(t, order-1, size/2)
        t.forward(size)
        draw_triforce(t, order-1, size/2)
        t.left(120)
        t.forward(size)
        t.right(120)
        draw_triforce(t, order-1, size/2)
        t.right(120)
        t.forward(size)
        t.left(120)

window = turtle.Screen()
window.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(0)

draw_triforce(t, 5, 200)
window.exitonclick()

