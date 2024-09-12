def int_fract():
    try:
        dec_num = str(input("Введите  число: "))
        base = int(input("Введите основание: "))
    except:
        return("Введите корректное число в десятичной системе!")
    alf = {
        "0" : "0", 
        "1" : "1", 
        "2" : "2", 
        "3" : "3", 
        "4" : "4", 
        "5" : "5", 
        "6" : "6", 
        "7" : "7", 
        "8" : "8", 
        "9" : "9", 
        "10" : "A", 
        "11" : "B", 
        "12" : "C",
        "13" : "D",
        "14" : "E",
        "15" : "F",
        }
    int_part = ""
    fract_part = ""
    flag =False
    for i in dec_num:
        if i ==",":
            flag = True
            continue
        if flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    return  str(int_conv(int_part, base)) + "," + str(fract_conv(fract_part, base))

def int_conv(int_part, base):
    decimal = 0
    power = 0
    for digit in reversed(int_part):
            decimal +=(int(digit) * (base ** power))
            power += 1
    return decimal

def fract_conv(fract_part, base):
    fract_decimal = 0
    power = -1
    for digit in reversed (fract_part):

            fract_decimal +=(int(digit) * (base ** power))
            power -= 1
    return   fract_decimal

if __name__ == "__main__":
    print(int_fract())
