import pyautogui
import time

pyautogui.PAUSE = 0.5

# PASSO A PASSO DO PROJETO

# 1. Abrir sitema da empresa
     #https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir navegador

pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

time.sleep(1)
# entrar no sistema    
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
     
pyautogui.write(link)
pyautogui.press("enter")

# segundos para carregar site
time.sleep(3)

# selecionar campo de email e senha
# 2. Fazer Login
pyautogui.click(x=828, y=467)
pyautogui.write("gabeestacio@gmail.com")

pyautogui.press("tab")
pyautogui.write("12345")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)
# 3. Abrir/importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl.

import pandas as pd 

tabela = pd.read_csv("produtos.csv")


# 4. Cadastrar um produto

for linha in tabela.index:
     codigo = str(tabela.loc[linha,"codigo"])

     # clicar no campo do codigo do produto
     pyautogui.click(x=735, y=314)

     # preencher código
     pyautogui.write(codigo)

     # passar para proximo campo
     pyautogui.press("tab")

     # marca
     pyautogui.write(str(tabela.loc[linha,"marca"]))

     # passar para proximo campo
     pyautogui.press("tab")

     # tipo
     pyautogui.write(str(tabela.loc[linha,"tipo"]))

     # passar para proximo campo
     pyautogui.press("tab")

     # categoria
     pyautogui.write(str(tabela.loc[linha,"categoria"]))

     # passar para proximo campo
     pyautogui.press("tab")

     # preço
     pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

     # passar para proximo campo
     pyautogui.press("tab")

     # custo
     pyautogui.write(str(tabela.loc[linha,"custo"]))

     # passar para proximo campo
     pyautogui.press("tab")

     # obs
     obs = str(tabela.loc[linha,"obs"])
     if obs != "nan":
          pyautogui.write(obs)

     # passar para proximo campo     
     
     pyautogui.press("tab")

     # apertar botão
     pyautogui.press("enter")
     pyautogui.scroll(5000)
     pyautogui.click(x=894, y=299)
# 5. repetir para todos produtos até acabar 