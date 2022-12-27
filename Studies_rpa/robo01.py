import pyautogui as p

# para coordenar o mause voce precisa entender que o mause não passa de uma coordenada cartesianada então seus
# valores são coordenadas de x e y

# minha coordenada zero fica no canto esquerdo superior da tela

#para descobrir a posição que irá ser usado voce pode utilizar comandos, o comando que informa a posição atual do mause 7
# é o comando position(), no nosso caso nomeamos a biblioteca do pyautogui como p e estamos usando uma de suas classes
# para utilizar então peço que a maquina espere alguns segundos até que eu coloque o mause sobre a posição que eu desejo
# e então ele me mostra a posição do mause como no camando a seguir

                                #p.sleep(2)
                                #print(p.position())

# agora podemos usar as coordenadas para realizar algumas tarefas por exemplo mover o mause para algum lugar da tela
#nesse comando ainda podemos dizer quanto tempo o mause precisa esperar para realizar essa função como pode ser visto

                                #p.moveTo(x=519, y=1077,duration=1)

#além disso podemos pedir para que o computadort realize um click vejamos

                                #p.click(x=519, y=1077)

p.hotkey('win','r')  #eu consigo passar teclas de atalho do meu teclado, ou seja para execultar mais de uma tecla do teclado
p.sleep(1)
p.typewrite('notepad') #serve para escrever um texto
p.sleep(2)
p.press('enter') #presione uma tecla do teclado
p.sleep(2)
p.typewrite('eu sou lindo')
p.sleep(5)
valor = p.getActiveWindow() #vai identificar qual é a janela aberta no momento
valor.close()
p.sleep(2)
p.press('right')
p.sleep(2)
p.press('enter')



