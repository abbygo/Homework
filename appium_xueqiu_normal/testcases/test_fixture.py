#abby
def handle_back(func):
    def wrapper(*args,**kwargs):
        print('异常处理开启了')
        res=func(*args,**kwargs)
        print(func.__name__)

        print('异常处理停止了')
    return wrapper


@handle_back
def do_cacke(size,weidao,caomei):
    return ('尺寸大小{0},口味{1},{2}'.format(size,weidao,caomei))

# handle_back(do_cacke)(1.6,'偏甜',caomei=10)
res=do_cacke(1.6,'偏甜',caomei=10)
print(res)

