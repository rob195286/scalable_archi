from complex_operations import ComplexNumber


def Mandelbrot(c, max_iter = 30):
    z = ComplexNumber(0,0)
    for i in range(max_iter):
        z = (z**2) + c
        if(z.module > 2):
            return False
    return True

