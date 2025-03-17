from RoboAnki.scr.models.functions import ANKI, login



# Configuração inicial
driver = webdriver.Chrome()
usuario = "dirt156@gmail.com"
senha = "Mari745/*"
arquivo_planilha = r"D:\Automação ANKI\Data\cards.xlsx"

# Instancia a classe ANKI
anki = ANKI(driver, usuario, senha)

# Faz login
anki.login()

# Adiciona cards a partir da planilha
anki.reed_cards_sheets(arquivo_planilha)

# Fecha o navegador
driver.quit()