#alerta .... esse programa funciona apenas com o gmail e apenas com a liberação do chrome
#no caso não serve para o notebook de empresa onde o recurso de adm do chrome não funciona 


import rpa as r
import pyautogui as p
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(4)
janela =  p.getActiveWindow()
janela.maximize()
dolarCormercial = r.read('//*[@id="comercial"]') #capitura o valor de uma variavel seja imagem ou texto
r.close()


#texto do email
texto_email = dolarCormercial + ' esse é um teste de mensagem' + ' hoje:' + str(pd.Timestamp('today'))

# email remetente, senha, destinatário
de = 'igor.skate30@gmail.com'
senha = 'igorladeia12'
para = 'igor.skate30@gmail.com'
#para02 = ''

# Setup the MIME
message = MIMEMultipart()
message['From'] = de
message['To'] = para
#message['To'] = para02
message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(de, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()