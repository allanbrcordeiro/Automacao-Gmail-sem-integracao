
import pyautogui
import time
import pandas
#Nao esqueça de alterar os e-mails do cliente na planilha;
clientes = pandas.read_csv('clientes.csv')
#deixe o gmail aberto e deixe ele como a ultima tela acessada (entre no gmail e depois venha para o código, assim com o alt+tab vai voltar na tela anterior)
pyautogui.hotkey('alt','tab')

time.sleep(2)

for linha in clientes.index:
    pyautogui.PAUSE = 0.5
    pyautogui.press('c')
    pyautogui.write(clientes.loc[linha, "E-MAIL"])
    # pyautogui.hotkey('ctrl','shift','c') - esse é para e-mail em cópia
    # pyautogui.write('@gmail.com') - colouqe o e-mail que vai ficar em cópia
    pyautogui.press('tab', presses=2)
    pyautogui.write('FATURA EM ATRASO - '+ str(clientes.loc[linha, "ID"]) + ' - ' + clientes.loc[linha, "CLIENTE"])
    pyautogui.press('tab')
    pyautogui.write('Prezado(a) cliente, a fatura de R$ '  + str(clientes.loc[linha, "VALOR"]) + ' venceu no dia ' + str(clientes.loc[linha, "VENCIMENTO"])  + ', por gentileza verificar e realizar o pagamento;')
    pyautogui.press('enter',presses=2)
    pyautogui.write('Atenciosamente -  Equipe Cordeiros; ')
    pyautogui.press('tab')
    pyautogui.press('enter')
    