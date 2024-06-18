import stdio
import stddraw

def main():
    while True:
        stddraw.filledRectangle(1.5, 1.2, .5, 5)

        p1_pdl_x = .05
        p1_pdl_y = .2 
        p1_pdl_w = .05
        p1_pdl_h = .5
        p2_pdl_x = 0.90
        p2_pdl_y = .2 
        p2_pdl_w = .05
        p2_pdl_h = .5
        ball_x = 0.5
        ball_y = 0.5
        stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, p1_pdl_w, p1_pdl_h)
        stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, p2_pdl_w, p2_pdl_h)
        stddraw.point(ball_x, ball_y)

        stddraw.show(100)
        stddraw.clear()

if __name__ == '__main__':
    main()