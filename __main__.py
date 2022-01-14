from client import get_mandelbrot_numbers
from plot import draw_mandelbrot_figure


delta_between_points = 0.014
count = 100*2
xmin, xmax = -count, count
ymin, ymax = -count, count



complex_numbers = get_mandelbrot_numbers(xmin, xmax, ymin, ymax, delta_between_points)


draw_mandelbrot_figure(list(map(lambda x : x.real_part, complex_numbers)),
                        list(map(lambda x : x.img_part, complex_numbers)))
