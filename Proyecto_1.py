# importamos los módulos necesarios

import pandas as pd
import matplotlib.pyplot as mplot
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

# declaramos una variable que nos permita continuar con el código si todo va bien
continuar = True

# declaramos la variable x
x = symbols("x")

# mostramos un menú para pedir al usuario la función y hacía que valor tiende x (controlamos posibles errores)

try:
    print("Ingresa la función que depende de x: ")
    fun = input(": ")

    print("hacía qué valor tiende x: ")
    lim = float(input(": "))

    # interpretamos la función

    y = parse_expr(fun)

    # mostramos el resultado

    print(f'El límite de la función {y} cuando x tiende a {lim} es:')    
    print(limit(y,x,lim))
    
except:
    
    print("Error al ingresar la información, fin del programa")
    continuar = False

#---------------------------------------------------------------------


    
# continuamos con la graficación

if continuar == True:
    # Preguntamos al usuario si desea ver un gráfico representativo

    print("Deseas ver un gráfico representativo del cálculo anterior")
    graf_1 = input("(si | no): ")

    # convertimos la cadena a minúsculas (lo anterior para trabajar aún en caso que el usuario haya
    #                                      ingresado si o no con alguna mayúscula)

    graf_2 = graf_1.lower()

    # Luego

    if graf_2 == "si":
        continuar =  True
    elif graf_2 == "no":
        print("Fin del programa")
        continuar = False
    else:
        print("¡Error! fin del programa")
        continuar = False
    
    # valores de aproximación
    valores = {"x": [lim + 1 / i for i in range(-10,11) if i != 0], "f(x)": [y.subs(x,i) for i in 
                                                                    [lim + 1 / i for i in range(-10,11) if i != 0]]}

    # creamos el dataframe
    df = pd.DataFrame(valores)
    
    # graficamos los puntos
    for i in range(-10,11):
        mplot.plot(df.iloc[i,0], df.iloc[i,1], marker = "o", color = "b")

    # graficamos el punto de interés en el límite (es x=x0)
    mplot.plot(lim, y.subs(x,lim), marker = "o", color = "r")
    
    if lim != 0 or y.subs(x,lim) != 0:
     
    # Construcción de las líneas auxiliares.

        # Caso en la ordenada y0 es positiva

        if y.subs(x,lim) > 0:
            v = 0
            while v <= y.subs(x,lim) and v >= 0:
                mplot.plot(lim,v, marker=",", color="k")
                v += 0.08

            # caso en que x=x0 es positivo

            if lim > 0:      
                u = 0
                while u <= lim and u >= 0:
                    mplot.plot(u,y.subs(x,lim), marker=",", color="k")
                    u += 0.05
            # caso en que x=x0 es negativo

            else:
                u = lim
                while u <= 0 and u >= lim:
                    mplot.plot(u,y.subs(x,lim), marker=",", color="k")
                    u += 0.05 

        # Caso en que la ordenada y0 es negativa          

        else:
            v = y.subs(x,lim)
            while v <= 0 and v >= y.subs(x,lim):
                mplot.plot(lim,v, marker=",", color="k")
                v += 0.08

            # caso en que x=x0 es positivo

            if lim > 0:      
                u = 0
                while u <= lim and u >= 0:
                    mplot.plot(u,y.subs(x,lim), marker=",", color="k")
                    u += 0.05

            # caso en que x=x0 es negativo

            else:
                u = lim
                while u <= 0 and u >= lim:
                    mplot.plot(u,y.subs(x,lim), marker=",", color="k")
                    u += 0.05  
    
 #----------------   
    # definimos el dominio de graficación 

    x = np.arange(-4,4, 0.01)

    # graficamos la funcion
    
    mplot.plot(x,eval(fun), color = "k")
    
    mplot.grid()
    mplot.show()
print("Fin del programa")
