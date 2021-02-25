from display import *
from draw import *
import random

s = new_screen()
c = [0, 255, 0]

"""
def the_drawing():

    for i in range(15):
        c = [181, 208, 255]

        if (i < 5):
            a = random.randint(216, 500)
            b = random.randint(0, 167)

        elif (i >= 10):
            a = random.randint(216, 500)
            b = random.randint(167, 327)

        else:
            a = random.randint(216, 500)
            b = random.randint(327, 500)

        draw_line(a, b, a + 40, b + 40, s, c)
        draw_line(a, b, a - 40, b - 40, s, c)

        draw_line(a + 20, b + 20, a + 20, b + 60, s, c)
        draw_line(a + 20, b + 20, a + 60, b + 20, s, c)

        draw_line(a - 20, b + 20, a - 20, b + 60, s, c)
        draw_line(a - 20, b + 20, a - 60, b + 20, s, c)

        draw_line(a - 20, b - 20, a - 21, b - 60, s, c)
        draw_line(a - 20, b - 20, a - 60, b - 20, s, c)

        draw_line(a + 20, b - 20, a + 21, b - 60, s, c)
        draw_line(a + 20, b - 20, a + 60, b - 20, s, c)

        draw_line(a, b, a - 40, b + 40, s, c)
        draw_line(a, b, a + 40, b - 40, s, c)

    for i in range(15):
        c = [0, 0, 255]

        if (i < 5):
            a = random.randint(72, 216)
            b = random.randint(0, 167)

        elif (i >= 10):
            a = random.randint(72, 216)
            b = random.randint(167, 327)

        else:
            a = random.randint(72, 216)
            b = random.randint(327, 500)

        draw_line(a, b, a + 20, b + 20, s, c)
        draw_line(a, b, a - 20, b - 20, s, c)

        draw_line(a + 10, b + 10, a + 10, b + 30, s, c)
        draw_line(a + 10, b + 10, a + 30, b + 10, s, c)

        draw_line(a - 10, b + 10, a - 10, b + 30, s, c)
        draw_line(a - 10, b + 10, a - 30, b + 10, s, c)

        draw_line(a - 10, b - 10, a - 11, b - 30, s, c)
        draw_line(a - 10, b - 10, a - 30, b - 10, s, c)

        draw_line(a + 10, b - 10, a + 11, b - 30, s, c)
        draw_line(a + 10, b - 10, a + 30, b - 10, s, c)

        draw_line(a, b, a - 20, b + 20, s, c)
        draw_line(a, b, a + 20, b - 20, s, c)

    for i in range(15):
        c = [202, 228, 241]

        if (i < 5):
            a = random.randint(0, 72)
            b = random.randint(0, 167)

        elif (i >= 10):
            a = random.randint(0, 72)
            b = random.randint(167, 327)

        else:
            a = random.randint(0, 72)
            b = random.randint(327, 500)

        draw_line(a, b, a + 10, b + 10, s, c)
        draw_line(a, b, a - 10, b - 10, s, c)

        draw_line(a + 5, b + 5, a + 5, b + 15, s, c)
        draw_line(a + 5, b + 5, a + 15, b + 5, s, c)

        draw_line(a - 5, b + 5, a - 5, b + 15, s, c)
        draw_line(a - 5, b + 5, a - 15, b + 5, s, c)

        draw_line(a - 5, b - 5, a - 6, b - 15, s, c)
        draw_line(a - 5, b - 5, a - 15, b - 5, s, c)

        draw_line(a + 5, b - 5, a + 6, b - 15, s, c)
        draw_line(a + 5, b - 5, a + 15, b - 5, s, c)

        draw_line(a, b, a - 10, b + 10, s, c)
        draw_line(a, b, a + 10, b - 10, s, c)

the_drawing()
"""
#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES / 2, s, c)
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

#octants 8 and 4
c[BLUE] = 255;
draw_line(0, YRES-1, XRES-1, 0, s, c);
draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
draw_line(XRES-1, 0, 0, YRES/2, s, c);

#octants 2 and 6
c[RED] = 255;
c[GREEN] = 0;
c[BLUE] = 0;
draw_line(0, 0, XRES/2, YRES-1, s, c);
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

#octants 7 and 3
c[BLUE] = 255;
draw_line(0, YRES-1, XRES/2, 0, s, c);
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

#horizontal and vertical
c[BLUE] = 0;
c[GREEN] = 255;
draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')