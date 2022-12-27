import pyautogui as p


p.hotkey('win', 'r')
p.sleep(1)
p.write("C:\\Users\\ifrtef\\Downloads")
p.press('enter')
p.sleep(1)
p.click(x=632, y=510)
p.sleep(1)
p.hotkey('ctrl','x')
p.sleep(1)
p.click(x=765, y=438)
p.sleep(1)
p.write('C:\\RPA')
p.sleep(1)
p.press('enter')
p.sleep(1)
p.hotkey('ctrl','v')
p.sleep(1)
p.click(x=1515, y=279)

#p.sleep(5)
#print(p.position())

p.press('esc')
p.sleep(1)

janela = p.getActiveWindow()
janela.maximize()