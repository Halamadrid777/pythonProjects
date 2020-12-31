
print("This is a unit converter built with python")


# temperature
# length
# area
# volume
def C2F(value):
    F = (9*value +32*5)*1/5
    return F

def C2K(value):
    K = (value +273)
    return K

def F2C(value):
    C = (5*value - 32*5)*1/9
    return C
def F2K(value):
    K = (10*value-320+273*18)*1/18
    return K
# print(C2F(150))
def K2C(value):
    C  = (value -273)
    return C

def K2F(value):
    F = (9*value-273*9+32*5)*1/5
    return F

def main():
    conv  = int(input("Type \n (1) Temperature \n (2)Length \n (3)area \n (4) volume \n type(1-4):"))
    if conv == 1:
        pass
        TempBase = int(input("Type \n (1) if your known temperature is in celcius \n (2) if your known temperature is in Fareneheight  \n (3) if your known temperature is in Kelvin \n:"))
        if TempBase == 1:
            temperature = int(input("Type your known value in Celcius: "))
            print("in Farenheight:   "+str(C2F(temperature)))
            print("in kelvin: " +str(C2K(temperature)))
            
        elif TempBase == 2:
            temperature = int(input("Type your known value in Farenheight: "))
            print("in celcius:  "+str(F2C(temperature)))
            print("in kelvin: "+str(F2K(temperature)))
        
        elif  TempBase == 3:
            temperature = int(input("Type your known value in Kelvin: "))
            print("in celcius: "+str(K2C(temperature)))
            print("in farenheight: "+str(K2F(temperature)))

        else:
            main()
    elif conv ==2:
        print("hello")



main()

