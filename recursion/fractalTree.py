import turtle

def tree(branch_len):
    if branch_len > 25:
        t.forward(branch_len)
        t.right(45)
        tree(branch_len - 50)
        t.left(90)
        tree(branch_len - 50)
        t.right(67.5)
        tree(branch_len - 50)
        t.left(45)
        tree(branch_len - 50)
        t.right(22.5)
        tree(branch_len - 50)
        t.backward(branch_len)


t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor('green')
t.left(90)
t.penup()
t.backward(120)
t.pendown()  # 到达预定位置
tree(180)
turtle.done()