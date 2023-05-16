
import pyautogui
import time
import pandas as pd
import pyperclip

#piperclip serve para copiar um texto dentro do codico com caracteres especias, o pyautogui não aceita caracteres especiais
# pyautogui.click
# pyautogui.write
# pyautogui.press
# pyautogui.hotkey

#1 acessar o sistema da empresa
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

#2 fazer log in no sistema (print (pyautogui.position()) para saber a posição do mouse e dar o click no campo certo)
pyautogui.click(x=983, y=441)
pyautogui.write("Tonex2507")
#tentar trocar segundo click por um tab
pyautogui.click(x=983, y=241)
pyautogui.write("dridrinepai")
#click no botão"acessar"
pyautogui.click(x=983, y=141)

time.sleep(5)

#3 baixar a base de dados
#button="right" = clicar com botão direito / segundo click é clicar no download
pyautogui.click(x=983, y=441, button="right")
pyautogui.click(x=983, y=441)

time.sleep(5)
#4 calcular os indicadores

#   importar a base de dados
database = pd.read_csv("C:\Users\Milton\Downloads\Compras.csv")
#   calcular os indicadores(total gasto/quantidade/preco medio)
total_gasto = database["ValorFinal"].sum()
quantidade = database["Quantidade"].sum()
preco_medio = total_gasto / quantidade

#5 enviar o e-mail
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=983, y=441)

pyautogui.write("nabor1210@gmail.com")
pyautogui.press("tab")

#mudar campo de remetente para assunto
pyautogui.press("tab")
assunto = "Relatório de compras"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v") #assunto copiado do pyperclip
pyautogui.press("tab") #passar do assunto para o corpo

corpo_email = f"""
Bom dia Milton,

Segue o relatorio de compras do dia de ontem.:

Total gasto: {total_gasto:,.2f}
Quantidade: {quantidade:,.2f}
Preço médio: {preco_medio:,.2f}

Qualquer duvida deixe-me saber.

Atenciosamente,
Milton
"""
#piperclip serve para copiar um texto dentro do codico com caracteres especias, o pyautogui não aceita caracteres especiais
pyperclip.copy(corpo_email)
pyautogui.hotkey("ctrl", "v")

#enviar e-mail
pyautogui.hotkey("ctrl", "enter")