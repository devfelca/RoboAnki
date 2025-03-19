from selenium import webdriver
from src.models.functions import ANKI
import time

def main():
    # Definições iniciais
    usuario = "dirt156@gmail.com"
    senha = "Mari745/*"
    data_locator = r"Data/cards.xlsx"
    deck_name = "Língua Potuguesa - SUSEP"  # Nome do deck a ser criado

    # Instancia o driver e a classe ANKI
    driver = webdriver.Chrome()
    anki = ANKI(driver, usuario, senha, data_locator)
    
    # Realiza o login
    print("Realizando login...")
    anki.login()
    time.sleep(5)
    
    # Lê a planilha e armazena os dados
    print("Lendo a planilha...")
    anki.read_cards_sheet()
    time.sleep(2)
    
    # Se um deck_name foi definido, cria o deck
    if deck_name:
        print(f"Criando deck: {deck_name}")
        anki.creat_deck(deck_name)
        time.sleep(6)
    
    # Verifica se a planilha possui dados e, se sim, envia os cards
    if anki.cards_data and len(anki.cards_data) > 0:
        print("Enviando os cards...")
        anki.send_all_cards()
    else:
        print("Nenhum card encontrado na planilha.")
    
    # Tempo para visualização antes de encerrar (opcional)
    time.sleep(5)


if __name__ == '__main__':
    main()
