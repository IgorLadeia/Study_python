
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

Tb1 = matriz(0)
x_J1 = Tb1[0, 2]
y_J1 = Tb1[1, 2]
axes.plot(0, 0, 'o')
axes.plot(x_J1, y_J1, 'o')
axes.plot([0, x_J1], [0, y_J1])
axes.set_xlim(-100, 100)
axes.set_ylim(-100, 100)





ax_slide = plt.axes([0.25,0.1,0.65,0.03])

def update(val):
    axes.clear()
    current = s_factor.val
    Tb1 = matriz(current)
    x_J1 = Tb1[0, 2]
    y_J1 = Tb1[1, 2]
    axes.plot(0, 0, 'o')
    axes.plot(x_J1, y_J1, 'o')
    axes.plot([0, x_J1], [0, y_J1])
    axes.set_xlim(-100, 100)
    axes.set_ylim(-100, 100)

s_factor = Slider(ax_slide,"Angulo01",valmin=0.0,valmax=360,valinit=360,valstep=0.1)
s_factor.on_changed(update)
plt.show()