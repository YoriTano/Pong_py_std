import stdio
import stddraw

p1_pdl_y = 0
p2_pdl_y = 0

while True:
    stddraw.show(0)
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        stdio.write(key)
        if key == 'w':
            p1_pdl_y = .5 + p1_pdl_y  
        if key == 's':
            p1_pdl_y =  p1_pdl_y - .5
        if key == 'u':
            p2_pdl_y = .5 +  p2_pdl_y
        if key == 'j':
            p2_pdl_y =  p2_pdl_y - .5
        stdio.writeln(p1_pdl_y)
        stdio.writeln(p2_pdl_y)