from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Allows the execution of keys
import pandas as pd

# to run chrome in the background
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True # also works
# nav = webdriver.Chrome(options=chrome_options)

# Open browser
navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")

# Step 1: Dollar Quotation
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# Step 2: Euro Quotation
navegador.get("https://www.google.com/")
navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Step 3: Gold Quotation
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

navegador.quit() # Close the browser

# Step 4: Import the product list
tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

# Step 5: Recalculate the price of each product
# Update the quote
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
# Update the 'Preço Base Reais' (Preço Base Original * Cotação)
tabela["Preço Base Reais"] = tabela["Cotação"] * tabela["Preço Base Original"]

# Update the 'Preço Final' (Preço Base Reais * Margem)
tabela["Preço Final"] = tabela["Preço Base Reais"] * tabela["Margem"]

display(tabela)

# Step 6: Save new product prices
tabela.to_excel("Produtos Novo1.xlsx", index=False)
