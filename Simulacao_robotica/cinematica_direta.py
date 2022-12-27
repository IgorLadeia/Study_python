import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


# Construimos la matriz de transformacion desde la base hasta J1, Tb1


#
# # Construimos la matriz de transformacion desde J1 hasta J2, T12
# q = 0*np.pi/180
# R = np.array([[np.cos(q), -np.sin(q)],
#          [np.sin(q), np.cos(q)]])
# t = np.array([[100],
#          [0]])
# # construimos la matriz de transformación homogenea
# Rt = np.concatenate((R,t), axis=1)
# T12 = np.concatenate((Rt, [[0,0,1]]), axis=0)
#
#
# # Construimos la matriz de transformacion desde J2 hasta ee, T2ee
# q = -45*np.pi/180
# R = np.array([[np.cos(q), -np.sin(q)],
#          [np.sin(q), np.cos(q)]])
# t = np.array([[50*np.cos(q)],
#           [50*np.sin(q)]])
# # construimos la matriz de transformación homogenea
# Rt = np.concatenate((R,t), axis=1)
# T2ee = np.concatenate((Rt, [[0,0,1]]), axis=0)
#
#
# # Con los valores obtenidos calculamos Tbee = Tb1 * T12 * T2ee
# Tb2 = Tb1.dot(T12) # El producto matricial de Tb1 y Tb2
#
# Tbee = Tb2.dot(T2ee) # El producto matricial de Tb2 y T2ee
#
#
# #Calculamos la posición del obketo respecto de la base
# pObjeto_ee = [20, 0, 1] # la posición en coordenadas homogeneas
# pObjeto_b = Tbee.dot(pObjeto_ee)
#
#
# # Para graficar tomamos las coordenadas de los puntos de interés, respecto de la base
# x_J1 = Tb1[0,2]
# y_J1 = Tb1[1,2]
# x_J2 = Tb2[0,2]
# y_J2 = Tb2[1,2]
# x_ee = Tbee[0,2]
# y_ee = Tbee[1,2]
# x_objeto = pObjeto_b[0]
# y_objeto = pObjeto_b[1]
#
#
# print(x_J1)
# print(y_J1)
#
# # ya podemos graficar
# fig, axes = plt.subplots()
# # primero los puntosj
# plt.plot(0,0, 'o')
# plt.plot(x_J1,y_J1, 'o')
# plt.plot(x_J2,y_J2, 'o')
# plt.plot(x_ee,y_ee, 'x')
# plt.plot(x_objeto, y_objeto, 'bo')
# # grafiquemos luego las lineas
# plt.plot([0,x_J1,x_J2,x_ee],[0,y_J1,y_J2,y_ee])
# # ajustamos los ejes
# axes.set_xlim(-150,150)
# axes.set_ylim(0,200)
#
#
# plt.show()
# # Plot the new wireframe and pause briefly before continuing.
#
# plt.pause(.001)
#
# ani = animation.FuncAnimation

fig, axes = plt.subplots()
plt.subplots_adjust(bottom=0.25)

def matriz(angle):
    q = np.radians(angle)
    l = 100
    R = np.array([[np.cos(q), -np.sin(q)], [np.sin(q), np.cos(q)]])
    t = np.array([[l * np.cos(q)], [l * np.sin(q)]])
    # construimos la matriz de transformación homogenea
    Rt = np.concatenate((R, t), axis=1)
    Tb1 = np.concatenate((Rt, [[0, 0, 1]]), axis=0)

    return Tb1

def matriz2(angle):
    q = np.radians(angle)
    l = 100
    R = np.array([[np.cos(q), -np.sin(q)], [np.sin(q), np.cos(q)]])
    t = np.array([[l ], [0]])
    # construimos la matriz de transformación homogenea
    Rt = np.concatenate((R, t), axis=1)
    Tb2 = np.concatenate((Rt, [[0, 0, 1]]), axis=0)

    return Tb2

Tb1 = matriz(0)
x_J1 = Tb1[0, 2]
y_J1 = Tb1[1, 2]
Tb2 = matriz2(60)
print(Tb2)
Tb2 = Tb1.dot(Tb2)
print(Tb2)
x_J2 = Tb2[0,2]
y_J2 = Tb2[1,2]
axes.plot(0, 0, 'o')
axes.plot(x_J2,y_J2, 'o')
axes.plot(x_J1, y_J1, 'o')
axes.plot([0, x_J1,x_J2], [0, y_J1,y_J2])
axes.set_xlim(-250, 250)
axes.set_ylim(-250, 250)







ax_slide = plt.axes([0.25,0.1,0.65,0.03])

def update(val):
    axes.clear()
    current = s_factor.val
    Tb1 = matriz(current)
    Tb2 = matriz2(60)
    print(Tb2)
    Tb2 = Tb1.dot(Tb2)
    print(Tb2)
    print("---------")
    x_J1 = Tb1[0, 2]
    y_J1 = Tb1[1, 2]
    axes.plot(0, 0, 'o')
    axes.plot(x_J1, y_J1, 'o')
    axes.plot(x_J2, y_J2, 'o')
    axes.plot([0, x_J1,x_J2], [0, y_J1,y_J2])
    axes.set_xlim(-250, 250)
    axes.set_ylim(-250, 250)

s_factor = Slider(ax_slide,"Angulo01",valmin=0.0,valmax=360,valinit=360,valstep=0.1)
s_factor.on_changed(update)
plt.show()