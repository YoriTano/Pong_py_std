import math
import random 
import stddraw
import stdio

def pong_input(p1_pdl_y, p2_pdl_y):
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        stdio.write(key)
#w and s control up and down for p1 paddle
        if key == 'w':
            p1_pdl_y = .1 + p1_pdl_y  
        if key == 's':
            p1_pdl_y =  p1_pdl_y - .1
#u and j control up and down for p2 paddle
        if key == 'u':
            p2_pdl_y = .1 +  p2_pdl_y
        if key == 'j':
            p2_pdl_y =  p2_pdl_y - .1
    return p1_pdl_y, p2_pdl_y 


def boundries(x_coord, y_coord, velocity_x, velocity_y, p1_pdl_y, p2_pdl_y):

    if (y_coord + velocity_y) >= 1:
        velocity_y += .001
        return  velocity_x, -1 * velocity_y
    if (y_coord + velocity_y) <= 0:
        velocity_y -= .001
        return velocity_x, -1 * velocity_y
    if (x_coord + velocity_x) < .1 and (y_coord >= p1_pdl_y and y_coord <= p1_pdl_y + .5):
        velocity_x += .001
        return -1 * velocity_x, velocity_y
    if (x_coord + velocity_x) > .9 and (y_coord >= p2_pdl_y and y_coord <= p2_pdl_y + .5):
        velocity_x += .001
        return -1 * velocity_x, velocity_y
    elif (x_coord + velocity_x) >= 1:
        stddraw.text(0.5, 0.5, "Player 1 has won the game.")
        stddraw.show(5000)
        exit()
    elif (x_coord + velocity_x) <= 0:
        stddraw.text(0.5, 0.5, "Player 2 has won the game.")
        stddraw.show(5000)
        exit()
    else:
        return velocity_x, velocity_y
def main():
   stddraw.setCanvasSize(1000, 600)
   stddraw.filledRectangle(1.5, 1.2, .5, 5)
   p1_pdl_x = .05
   p1_pdl_y = .2 
   p1_pdl_w = .05
   p1_pdl_h = .5
   p2_pdl_x = 0.90
   p2_pdl_y = .2 
   p2_pdl_w = .05
   p2_pdl_h = .5
   ball_x = 0.4
   ball_y = 0.5
   velocity_x = round(random.randint(-3, 3) / 100, 3)
   velocity_y = round(random.randint(-3, 3) / 100, 3)
   stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, p1_pdl_w, p1_pdl_h)
   stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, p2_pdl_w, p2_pdl_h)
   stddraw.point(ball_x, ball_y)

   while True:
        p1_pdl_y, p2_pdl_y = pong_input(p1_pdl_y, p2_pdl_y)
        velocity_x, velocity_y = boundries(ball_x, ball_y, velocity_x, velocity_y, p1_pdl_y, p2_pdl_y)
        ball_y = ball_y + velocity_y
        ball_x = ball_x + velocity_x
        stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, p1_pdl_w, p1_pdl_h)
        stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, p2_pdl_w, p2_pdl_h)
        stddraw.point(ball_x, ball_y)
        stddraw.show(50)
        stddraw.clear()

if __name__ == '__main__':
    main()