from selenium import webdriver
from src.models.functions import ANKI
import time

# Cria o driver e define-o como variável global para que o modelo (que usa "driver")
# possa encontrá-lo sem problemas
driver = webdriver.Chrome()

def main():
    # Defina as credenciais do usuário
    usuario = "dirt156@gmail.com"
    senha = "Mari745/*"
    data_locator = r"Data/cards.xlsx"
    
    # Instancia a classe ANKI conforme definida em src/models/functions.py
    anki = ANKI(driver, usuario, senha, data_locator)
    # Como o construtor da classe não recebe "senha", atribuimos manualmente
    anki.senha = senha

    # Realiza o login
    anki.login()
    time.sleep(5)  # Aguarda a conclusão do login
    anki.reed_cards_sheets()
    # clique no botão de card
    anki.add_card()
    time.sleep(3)

    # import data from excel
    anki.reed_cards_sheets()
    time.sleep(5)

    anki.send_cards()
    time.sleep(6)



if __name__ == '__main__':
    main()
