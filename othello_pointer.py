#Kan Dang 54515091 Lab 4 Safir

class Mouse:
    def __init__(self, fractal_x: float, fractal_y: float):
        self._fractal_x = fractal_x
        self._fractal_y = fractal_y

    def fractal(self) -> (float, float):
        'Returns fractal attribute'
        return (self._fractal_x, self._fractal_y)

    def pixel(self, w: float, h: float) -> (float, float):
        'Returns pixels attribute'
        return( int(self._fractal_x * w), int(self._fractal_y * h))

def from_fractal(x: float, y: float) -> Mouse:
    'Returns fractals from mouse'
    return Mouse(x, y)

def from_pixel(x: float, y: float, w: float, h: float) -> Mouse:
    'Returns pixels from mouse'
    return Mouse(x/w, y/h)
