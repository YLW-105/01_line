from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 >= x0):
        x = int(x0)
        y = int(y0)
        x1 = int(x1)
        y1 = int(y1)
    else:
        x = int(x1)
        y = int(y1)
        x1 = int(x0)
        y1 = int(y0)

    #change
    dx = x1 - x
    dy = y1 - y

    A = dy
    B = dx

    if (dx != 0):
        m = dy / dx

    #vertical
    if (dx==0):
        while (y <= y1):
            plot(screen, color, x, y)
            y = y + 1

    #horizontal
    elif (dy==0):
        while (x <= x1):
            plot(screen, color, x, y)
            x = x + 1

    #Octant 1 and 5
    elif (m > 0 and m <=1):
        B = B * -1
        d = 2*A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d = d + 2*B
            else:
                x = x + 1
                d = d + 2*A

    #Octant 2 and 6
    elif (m > 1):
        A = A * -1
        d = 2 * B + A
        while (y <= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d = d + 2 * A
            else:
                y = y + 1
                d = d + 2 * B

    # Octant 3 and 7
    elif (m < -1):
        A = A * -1
        d = 2 * B - A
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d = d - 2 * A
            else:
                y = y - 1
                d = d + 2 * B

    # Octant 4 and 8
    elif (m < 0 and m >= -1):
        B = B * -1
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d = d + 2 * A
            else:
                y = y - 1
                d = d - 2 * B




