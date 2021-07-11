import pyautogui # allow automations (screen, mouse and keyboard)
import time # delay
import pyperclip # allow automations
import pandas as pd # the "pandas" is for data analysis!

pyautogui.PAUSE = 1 # Os códigos serão executados em um intervalo de 1seg)

# Step 1
# Open Google on Desktop
time.sleep(4)
pyautogui.click(435,210, clicks=2)
# Enter system link
pyautogui.click(485, 52)
pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press('enter')

# Step 2
time.sleep(4)
pyautogui.click(396, 301, clicks=2)
time.sleep(1)

# Step 3
pyautogui.click(407,371) # click on file
time.sleep(0.5)
pyautogui.click(1156,190) # click on the "3 dots"
time.sleep(2)
pyautogui.click(968,570) # click "download"
time.sleep(8)
pyautogui.click(496,414) # click "save"

# Passo 4
tabela = pd.read_excel(r"C:\Users\LUCAS\Downloads\Vendas - Dez.xlsx") # this "r" is important for python to understand the file path
faturamento = tabela["Valor Final"].sum() # the sum of the "Valor Final" column
quantidade = tabela["Quantidade"].sum() # the sum of the "Quantidade" column
display(tabela)

# Step 5
# Open a new tab
time.sleep(4)
pyautogui.click(435,210, clicks=2)

# Sign in to gmail
pyautogui.click(485, 52)
pyautogui.write('https://mail.google.com/')
pyautogui.press('enter')
time.sleep(8)

# Click on the 'Write' button
pyautogui.click(98,208)
time.sleep(0.5)

# Enter who we are sending to
pyautogui.write('lucascabralmendes.correa@gmail.com')
pyautogui.press('tab') # select email
pyautogui.press('tab') # move to email subject field

# Enter the subject
assunto = "Relatório de Vendas de Ontem"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", 'v')
pyautogui.press('tab') # move to email body field

# Enter the body of the email
texto_email = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Lucas Cabral
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')

# click send
pyautogui.hotkey('ctrl', 'enter')
