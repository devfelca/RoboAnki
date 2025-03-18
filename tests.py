
from selenium import webdriver
from src.models.functions import ANKI
import time


# Instancia o driver (variável global)
driver = webdriver.Chrome()

def main():
    usuario = "dirt156@gmail.com"
    senha = "Mari745/*"
    data_locator = r"Data/cards.xlsx"
    deck_name = "Língua Potuguesa - SUSEP"
    
    # Instancia a classe ANKI com o caminho da planilha
    anki = ANKI(driver, usuario, senha, data_locator, deck_name)
    
    # Realiza o login
    anki.login()
    time.sleep(5)
    
    # Primeiro, lê a planilha e armazena os dados
    anki.read_cards_sheet()
    time.sleep(2)

    anki.creat_deck()
    time.sleep(100)
    # Em seguida, envia os cards utilizando os dados armazenados
    anki.send_all_cards()
    
    # Opcional: fecha o navegador ao final
    # driver.quit()

if __name__ == '__main__':
    main()
