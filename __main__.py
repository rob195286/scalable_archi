from mandelbrot import Mandelbrot
from complex_operations import ComplexNumber
from plot import Draw_points
from time import time
import numpy as np
#from canvas import Draw_point, Run

delta_between_points = 0.004
points_size = 1
count = 100*8
xmin, xmax = -count, count
ymin, ymax = -count, count


t1 = time()

complex_numbers = [ComplexNumber(real_part * delta_between_points, img_part * delta_between_points)
                   for real_part in range(xmin, xmax)
                   for img_part in range(ymin, ymax)
                   if (Mandelbrot(ComplexNumber(real_part * delta_between_points, img_part * delta_between_points)))]

#print(complex_numbers)
t2 = time()
print("time :",t2-t1,"s")

Draw_points(list(map(lambda x : x.real_part, complex_numbers)),
            list(map(lambda x : x.img_part, complex_numbers)),
            points_size)
