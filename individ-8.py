def print_info(func):
    def f(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Площадь круга равна = {result:1.2f}')
    return f
@print_info
def area(x):
    return 3.1415926 * x * x
 
r = float(input('Введите радиус'))
area(r)