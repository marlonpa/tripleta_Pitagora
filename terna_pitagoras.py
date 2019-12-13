"""
En este ejemplo recorremos el rango de cada uno de las variables q intervienen en la terna
de pitagoras cuya formula es a**2 + b**2 = c**2 (las sumas de a y de b al cuadrado tiene que 
ser igual a C al cuadrado y ademas las suma de las 3 variable debe ser igual a 1000
"""

class Terna:

    def terna():
          
        lista = []
        for a in range(1, 500):
            for b in range(a + 1, 500):
                for c in range(b + 1, 500):
                    if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                        lista.append((a, b, c))
        
        return lista


t = Terna.terna()
print(t)
