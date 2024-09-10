def int_fract(dec_num):
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
    return  str(int_conv(int_part)) + "," + str(fract_conv(fract_part))

def int_conv(int_part):
    decimal = 0
    power = 0
    for digit in reversed(int_part):
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal

def fract_conv(fract_part,):
    fract_decimal = 0
    power = -1
    for digit in fract_part:
        if digit == '1':
            fract_decimal += 2 ** power
        power -= 1
    return   fract_decimal

if __name__ == "__main__":
    dec_num = str(input("Введите двоичное число:"))
    print(int_fract(dec_num))
