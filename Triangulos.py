import math

def altura(a, b, c):
    s = (a + b + c) / 2
    h = (2 / c) * (math.sqrt(s*(s - a) * (s - b) * (s - c)) )
    return h

def area(h, base):
    return (base * h) / 2

def distancia_puntos(x1, x2, y1, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2) )

def calcular_area(a1, a2, b1, b2, c1, c2): 
    distancia_a_b = distancia_puntos(a1, b1, a2, b2)
    distancia_b_c = distancia_puntos(b1, c1, b2, c2)
    distancia_c_a = distancia_puntos(c1, a1, c2, a2)

    alt = altura(distancia_a_b, distancia_b_c, distancia_c_a)

    return area(alt, distancia_a_b)

if __name__ == '__main__':
    a1 = int(input() )
    a2 = int(input() )
    b1 = int(input() )
    b2 = int(input() )
    c1 = int(input() )
    c2 = int(input() )
    
    d1 = int(input() )
    d2 = int(input() )

    area_1 = calcular_area(a1, a2, b1, b2, c1, c2)
    print(area_1)
    area_2 = calcular_area(a1, a2, b1, b2, d1, d2)
    print(area_2)
    area_3 = calcular_area(a1, a2, d1, d2, c1, c2)
    print(area_3)
    area_4 = calcular_area(d1, d2, b1, b2, c1, c2)
    print(area_4)

    if area_1 >= (area_2 + area_3 + area_4):
        print("Esta adentro")
    else:
        print("Esta afuera")

