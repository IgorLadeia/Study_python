import rpa as r
import pyautogui as p

#quando eu utilizar a biblioteca RPA sempre terei que iniciar o programa com o comando INIT
# o comando initi vem setado como (visual_automation = false,chrome_browser = true )
# sendo assim sempre que voce chamar o init ele vai chamar o browser, caso voce não queira usar o browser basta mudar
#r.init(visual_automation = true,chrome_browser = false )

r.init()
r.url('http://www.google.com')
janela =  p.getActiveWindow()
janela.maximize()
r.wait(2.0)

#voce pode buscar o campo pela clasificação do CSS do componente do site ... lembrando que tem uma hierarquia
#r.type('//*[@]name=q','rpa[enter]')
r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input','anna[enter]')

# a biblioteca RPA foi construida em cima do pyautogui por esse motivo tem algumas melhorias
# no comando type eu coloco o local onde quero escrever, o testo que quero escrever e ainda se eu quiser
# clicar em uma tecla eu posso colocala entre [] após o texto

r.wait(1.0)
r.snap('page','rpa_page.png')
# se voce não colocar o endereço da pasta de arquivo que queira salvar a imagem .... vai ser salva no
#repositório do seu projeto.

r.wait(2.0)
r.close()


