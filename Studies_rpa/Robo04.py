import pyautogui as p

#p.sleep(2)
#print(p.position())

p.doubleClick(x=713, y=1065)
p.sleep(2)
p.click(x=748, y=586)
p.write('www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(3)


#me retorna as coordenadas da imagem
#o confidenci é a quantidade de precisão de busca
localpesq = p.locateOnScreen('Pesquisa.PNG',confidence=0.9)
    #print(localpesq)
localpesquisa = p.center(localpesq)
    #print(localpesquisa)
xPesquisa, yPesquisa = localpesquisa

#dessa forma conseguimos encontrar a imagem na tela e também encontrar o centro da imagem  para clickar
p.moveTo(xPesquisa, yPesquisa, duration=1)
p.click(xPesquisa, yPesquisa)
p.sleep(1)
p.write('Charles Lima')
p.press('enter')
p.sleep(3)
p.screenshot('cursos.PNG')



localClo = p.locateOnScreen('Close.PNG',confidence=0.7)
localClose = p.center(localClo)
xClose, yClose = localClose
p.moveTo(xClose, yClose, duration=1)
p.click(xClose, yClose)
