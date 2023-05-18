#pip install selenium
#firefox > geckodriver
#google chrome > chromedriver

#1 Entrar na internet e abrir o navegador
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

#2 Importar a base de dados
import pandas

database = pandas.read_excel("commodities.xlsx")

#3 Para todo produto da nossa base
# Xpath > ir no navegador, inspecionar e copiar o campo como xpath com botão direito
    # Funções: .send_keys("Meu nome é") -> escrever no campo
    # .click() -> clicar no campo ou botão
    # .get_attribute() -> pegar informação no campo/objeto

for linha in database.index:

    produto = database.loc[linha, "Produto"]

    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ç","c").replace("ã","a")
    navegador.get(link) #abrir navegador
    #precisa tratar os caracteres especiais áãéç etc...unicodedata

    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute("value") #encontrar elemento(campo valor milho).pegar valor
    cotacao = cotacao.replace(".", "").replace(",", ".") #tratar o numero ex: 1.257,22 para 1257,22
    cotacao = float(cotacao)

    database.loc[linha,"Preço Atual"] = cotacao


#4 Pegar o preço atual do produto
#5 Atualizar preços na base de dados
#6 Decidir quais produtos comprar
database["Comprar"] = database["Comprar"] < database["Preço Ideal"]
#7 Exportar a base atualizada
navegador.quit()

database.to_excel("commodities_atualizado.xlsx", index = False)