import rpa as r
import pyautogui as p

r.init()
r.url('http://rpachallenge.com')

p.sleep(10)

r.download('https://rpachallenge.com/assets/downloadFiles/challenge.xlsx','challenge.xlsx')



