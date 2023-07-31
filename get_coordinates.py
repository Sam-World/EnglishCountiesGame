import turtle

screen = turtle.Screen()
screen.screensize()
screen.title("English Counties")
image = "BEC_500.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_cor(x, y):
    print(x, y)


# event listener - listens for click, then calls function
turtle.onscreenclick(get_mouse_click_cor)


# keeps screen open even when code is finished running (alternative to exitonclick)
turtle.mainloop()
