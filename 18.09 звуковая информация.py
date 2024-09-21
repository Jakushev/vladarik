import math
#def task1(rate, time, resolution):
    #time = time * 60 #перевод минут в секунды
    #rate = rate * 1000 #перевод кгц в гц (писать с точкой)
    #v = (rate * time * resolution) / 8 #находим объем памяти в байтах
    #return int(v)

#def task2(time1, resolution1, v ):
    #time1 = time1 * 60 #переводим минуты в секунды
    #v = v * (1024 ** 2) #переводим мбайты в байты
    #rate1 = v / (time1 * resolution1 * (8)) #находим частоту в гц
    #return float(rate1)

#def task3(vv, resolution2, rate2):
    #vv = vv * (1024 ** 3) #переводим гбайты в байты
    #time2 = vv / (rate2 * resolution2 * (8)) #находим время звучания в секундах
    #return float(time2)


#def task4(vvv, resolution3, rate3):
    #vvv = vvv * 1024 #переводим кбайты в байты
    #rate3 = rate3 * 1000 #переводим кгц в гц
    #time3 = vvv / (rate3 * resolution3 * (8)) #находим время звучания в секундах
    #return float(time3)

def task5(rate4, time4, resolution4):
    time4 = time4 * 60 #перевод минут в секунды
    rate4 = rate4 * 1000 #перевод кгц в гц (писать с точкой)
    vvv = (rate4 * time4 * resolution4) / 8 #находим объем памяти в байтах
    return int(vvv)


if __name__ == "__main__" :
    #rate = float(input("частота: "))
    #time =  int(input("время в минутах: "))
    #resolution = int(input("разрешение: "))   
    #print (task1(rate, time, resolution))
    #v = float(input("объем в мбайты (писать с точкой): "))
    #time1 =  int(input("время в минутах: "))
    #resolution1 = int(input("разрешение: "))   
    #print (task2(v, time1, resolution1))
    #vv = float(input("объем в гбайты (писать через точку): "))
    #rate2 =  int(input("частота: "))
    #resolution2 = int(input("разрешение: "))   
    #print (task3(vv, rate2, resolution2))
    #vvv = float(input("объем в кбайты: "))
    #rate3 =  int(input("частота: "))
    #resolution3 = int(input("разрешение: "))   
    #print (task4(vvv, rate3, resolution3))
    rate4 = int(input("частота: "))
    time4 =  int(input("время в минутах: "))
    resolution4 = int(input("разрешение: "))   
    print (task5(rate4, time4, resolution4))




