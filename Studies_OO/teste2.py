
def f(x):
    return ((200*pow(x,5)) + (947*pow(x,4)) + (1735*pow(x,3)) + (1470*pow(x,2)) + (470*pow(x,1)) - 65)


def g(x):
    return ((1000*pow(x,4)) + (3788*pow(x,3)) + (5205*pow(x,2)) + (2940*pow(x,1)) + 470)



def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')



x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

x0 = float(x0)
e = float(e)


N = int(N)


newtonRaphson(x0, e, N)