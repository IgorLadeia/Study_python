import pyautogui as p

p.hotkey('win', 'r')
p.sleep(1)
p.write("C:\\Users\\ifrtef\\Desktop\\RPA.pbix")
p.sleep(1)
p.press('enter')
p.sleep(20)
p.click(x=759, y=93)
p.sleep(10)
p.click(x=1893, y=18)
p.sleep(3)
p.click(x=980, y=557)

#p.sleep(5)
#print(p.position())


