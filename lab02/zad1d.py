from math import exp

def machine_epsilon():
    epsilon = 1
    epsilon_last = epsilon

    while epsilon + 1 > 1:
        epsilon_last = epsilon
        epsilon = epsilon/2
    return epsilon_last

def better_exponent(x):
    val = 1
    to_add = 1
    index = 1
    new_x = abs(x)
    epsilon = machine_epsilon()

    while abs(to_add)>epsilon:
        to_add *= new_x/index
        val += to_add
        index += 1
    
    if x >= 0:
        return val
    else:
        return 1/val

if __name__ == "__main__":
    arr = [1,-1,5,-5,10,-10]

    for element in arr:
        print("Dla x = ",element)
        print("Wartosc zwrocona z exponent: ",better_exponent(element))
        print("Wartosc zwrocna z exp: ",exp(element))
        print("-----------------------------------------------------")