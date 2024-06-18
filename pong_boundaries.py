import stdio
import stddraw
import random      
x_coord = .5
y_coord = .5
velocity_x = round(random.random() / 10, 2)
velocity_y = round(random.random() / 10, 2)


while True:
    stddraw.clear()
    stddraw.point(x_coord, y_coord)
    stddraw.show(100)

    if (y_coord + velocity_y) >= 1:
        velocity_y = round(random.random() / 10, 2)
        print(velocity_y)
        print(velocity_x)
        velocity_y = -velocity_y

    if (y_coord + velocity_y) <= 0:
        velocity_y =  round(random.random() / 10, 2)
        velocity_y = velocity_y
        print(velocity_y)
        print(velocity_x)
    elif (x_coord + velocity_x) >= 1:
        stddraw.text(0.5, 0.5, "Player 1 has won the game.")
        stddraw.show(1100)
        exit()
    elif (x_coord + velocity_x) <= 0:
        stddraw.text(0.5, 0.5, "Player 2 has won the game.")
        stddraw.show(1100)
        exit()

    y_coord = y_coord + velocity_y
    x_coord = x_coord + velocity_x