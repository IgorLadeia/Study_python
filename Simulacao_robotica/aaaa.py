

# importamos las librerías necesarias
import sympy.sim
import sympy as sp
###  Conectamos con Sim y obtenemos los manejadores

def connect(port):
# Establece la conexión a CoppeliaSim
# port debe coincidir con el puerto de conexión en VREP
# retorna el número de cliente o -1 si no puede establecer conexión
    sim.simxFinish(-1) # just in case, close all opened connections
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) # Conectarse
    if clientID == 0: print("conectado a", port)
    else: print("no se pudo conectar")
    return clientID

# Conectarse al servidor y obtener manejadores
def getHandlers():
    retCode,effector=sim.simxGetObjectHandle(clientID,'effector',sim.simx_opmode_blocking)
    retCode,target=sim.simxGetObjectHandle(clientID,'Cuboid',sim.simx_opmode_blocking)
    retCode,joint1=sim.simxGetObjectHandle(clientID,'MTB_joint1',sim.simx_opmode_blocking)
    retCode,joint2=sim.simxGetObjectHandle(clientID,'MTB_joint2',sim.simx_opmode_blocking)
    retCode,joint3=sim.simxGetObjectHandle(clientID,'MTB_joint3',sim.simx_opmode_blocking)
    retCode,joint4=sim.simxGetObjectHandle(clientID,'MTB_joint4',sim.simx_opmode_blocking)
    joint = [joint1, joint2, joint3, joint4]
    return joint, effector, target
# Definimos funciones para obtener matrices de transformación simbólicas

def symTfromDH(theta, d, a, alpha):
    # theta y alpha en radianes
    # d y a en metros
    Rz = sp.Matrix([[sp.cos(theta), -sp.sin(theta), 0, 0],
                   [sp.sin(theta), sp.cos(theta), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    tz = sp.Matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, d],
                   [0, 0, 0, 1]])
    ta = sp.Matrix([[1, 0, 0, a],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    Rx = sp.Matrix([[1, 0, 0, 0],
                   [0, sp.cos(alpha), -sp.sin(alpha), 0],
                   [0, sp.sin(alpha), sp.cos(alpha), 0],
                   [0, 0, 0, 1]])
    T = Rz*tz*ta*Rx
    return T

def matrixFromPose(pose):
    # pose = [x, y, z, alpha, beta, gamma]
    # x, y, z en metros
    # alpha, beta, gamma en radianes
    x, y, z = pose[0], pose[1], pose[2]
    alpha, beta, gamma = pose[3], pose[4], pose[5]
    Ra = sp.Matrix([[1, 0, 0, 0],
                   [0, sp.cos(alpha), -sp.sin(alpha), 0],
                   [0, sp.sin(alpha), sp.cos(alpha), 0],
                   [0, 0, 0, 1]])
    Rb = sp.Matrix([[sp.cos(beta), 0, sp.sin(beta), 0],
                   [0, 1, 0, 0],
                   [-sp.sin(beta), 0, sp.cos(beta), 0],
                   [0, 0, 0, 1]])
    Rc = sp.Matrix([[sp.cos(gamma), -sp.sin(gamma), 0, 0],
                   [sp.sin(gamma), sp.cos(gamma), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    T = Ra*Rb*Rc
    T[0,3] = x
    T[1,3] = y
    T[2,3] = z
    return T

# Comenzaremos el trabajo desde la descripción de Denavit-Hartenberg para el robot
#      theta     |      d      |      a      |    alpha
# ---------------------------------------------------------
#      q1        |    0.302    |    0.467    |     0
#      q2        |    -0.01    |    0.4005   |    180
#      0         |      q3     |     0       |    180
#      q4        |      0      |     0       |     0
# ---------------------------------------------------------
#      0         |    -0.058   |     0       |     0
# La matriz de transformación desde la base al efector final es
sq = sp.symbols(['q1', 'q2', 'q3', 'q4'])

T = sp.simplify(symTfromDH(sq[0], 0.302, 0.467, 0) *
                symTfromDH(sq[1], -0.01, 0.4005, sp.pi) *
                symTfromDH(0, sq[2], 0, sp.pi) *
                symTfromDH(sq[3], 0, 0, 0) *
                symTfromDH(0, -0.058, 0, 0))

clientID = connect(19999)
joint, effector, target = getHandlers()
# definimos las coordenadas de destino
res, pos = sim.simxGetObjectPosition(clientID, target, -1, sim.simx_opmode_blocking)
res, eul = sim.simxGetObjectOrientation(clientID, target, -1, sim.simx_opmode_blocking)
a = pos[0] + 0.025
b = pos[1] - 0.025
c = pos[2] + 0.03
pos = [a, b, c]
pose_destino = pos + eul
pose_destino
#la matriz de transformación será
D = matrixFromPose(pose_destino)
D
# ahora resolvemos la ecuación utilizando nsolve()
q = sp.nsolve(T-D, sq, [0.1, 0.1, 0.1, 0.1], prec=6)
q
# enviamos los ángulos al robot
retCode = sim.simxSetJointTargetPosition(clientID, joint[0], q[0], sim.simx_opmode_oneshot)
retCode = sim.simxSetJointTargetPosition(clientID, joint[1], q[1], sim.simx_opmode_oneshot)
retCode = sim.simxSetJointTargetPosition(clientID, joint[2], q[2], sim.simx_opmode_oneshot)
retCode = sim.simxSetJointTargetPosition(clientID, joint[3], q[3], sim.simx_opmode_oneshot)
