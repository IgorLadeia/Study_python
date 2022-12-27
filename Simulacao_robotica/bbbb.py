import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# Construimos la matriz de transformacion desde la base hasta J1, Tb1

def Matrix_junta01(Angle,Eixo):

    "primeiro vamos defir as caracteristicas do primeiro link"
    eixo = Eixo
    angle = np.radians(Angle)

    "agora iremos definir a matriz de rotação de 2D"
    M_rotation = np.array([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]])

    "agora a matriz de translação do nosso objeto"
    M_translação = np.array([[eixo * np.cos(angle)],[eixo * np.sin(angle)]])

    "agora iremos criar a nova matriz, para isso primeiro iremos colocar concatenar a matriz de rotação com a de "
    "de tranlação, para essa função iremos colocar o indexisador (axis=1) pois as matrizes não são de mesma dimenssão"
    M_concate = np.concatenate((M_rotation, M_translação), axis=1)

    "finalmente iremos agora colocar a linha de seleção de movimentação, lembrando que nosso robo é planar,"
    "de modo que todas as movimentações teram como eixo de rotação referencial o Z"
    matrix_final = np.concatenate((M_concate, [[0, 0, 1]]), axis=0)

    return matrix_final


def Matrix_junta02(angle):
    q = np.radians(angle)
    R = np.array([[np.cos(q), -np.sin(q)],
                  [np.sin(q), np.cos(q)]])
    t = np.array([[100], [0]])

    Rt = np.concatenate((R, t), axis=1)
    Matrix01 = np.concatenate((Rt, [[0, 0, 1]]), axis=0)

    return Matrix01


def Matrix_junta03(angle):
    q = np.radians(angle)
    R = np.array([[np.cos(q), -np.sin(q)],
                  [np.sin(q), np.cos(q)]])
    t = np.array([[100],
                  [0]])
    # construimos la matriz de transformación homogenea
    Rt = np.concatenate((R, t), axis=1)
    Matrix02 = np.concatenate((Rt, [[0, 0, 1]]), axis=0)

    return Matrix02


# Con los valores obtenidos calculamos Tbee = Tb1 * T12 * T2ee


def plot(matrix_um_eixo,i):

    axes.clear()
    x_J1 = matrix_um_eixo[0, 2]
    y_J1 = matrix_um_eixo[1, 2]

    plt.plot(0, 0, 'o')
    plt.plot(x_J1, y_J1, 'o')
    plt.plot([0, x_J1], [0, y_J1])
    axes.set_xlim(-250, 250)
    axes.set_ylim(-0, 250)


fig, axes = plt.subplots()

ani = animation.FuncAnimation(fig,plot(matriz))

a = 30
b = 0
c = -45
Produto_matriz01 = Matrix_junta01(a).dot(Matrix_junta02(b))  # El producto matricial de Tb1 y Tb2

Produto_matriz_ponto = Produto_matriz01.dot(Matrix_junta03(c))  # El producto matricial de Tb2 y T2ee

# Calculamos la posición del obketo respecto de la base
pObjeto_ee = [20, 0, 1]  # la posición en coordenadas homogeneas
pObjeto_b = Produto_matriz_ponto.dot(pObjeto_ee)

plt.show()
# Plot the new wireframe and pause briefly before continuing.

plt.pause(.001)

ani = animation.FuncAnimation
