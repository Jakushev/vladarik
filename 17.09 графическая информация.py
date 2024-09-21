import math
def task1(h, m,):
    k = 1
    V = h * m * k #находим объем памяти изображения
    return int (V)

def task2(before, after,):
    result = after / before #находим во сколько раз увеличился объем памяти
    return int (result)

def task3(hh, mm, vv):
    vv = vv * 1024 * 8 #переводим Кбайты в биты
    k = vv / (hh * mm) #определяем колличество цветов
    return int (k)

def task4 (c, vvv):
    vvv = vvv * 8 #переводим байты в бит
    c = math.log2 (c) #узнаём сколько бит в одной точке
    mn = vvv / k #количество точек на экране
    return int (mn)
    




if __name__ == "__main__" :
    #h = int (input("ширина: "))
    #m = int (input("высота: "))
    #print (task1(n, m))
    #before = int (input("количество цветов до: "))
    #after = int (input("количество цветов после: "))
    #print (task2(before, after))
    #hh = int (input("ширина: "))
    #mm = int (input("высота: "))
    #vv = int (input("объем памяти: "))
    #print (task3(nn, mm, vv))
    c = int (input("количество цветов: "))
    vvv = int (input("объем памяти: "))
    print (task4(c, vvv))