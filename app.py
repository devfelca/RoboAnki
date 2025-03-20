import requests
from selenium import webdriver
from src.models.functions import ANKI
import time

def main():
    print("Bem-vindo(a) ao RoboAnki!")
    
    # Menu de opções
    try:
        selector = int(input(
            "Digite a opção que gostaria de Executar:\n"
            " (1) Criar um novo Deck \n"
            " (2) Adicionar Cards \n"
            " (3) Criar um Novo Deck e Adicionar Cards \n"
            "Opção: "
        ))
    except ValueError:
        print("Digite um número inteiro válido!")
        exit()
    
    if selector not in [1, 2, 3]:
        print("Digite um número inteiro dentro das opções (1, 2 ou 3).")
        exit()
    
    # Solicita credenciais e outros dados
    usuario = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    data_locator = r"Data/cards.xlsx"
    
    # Instancia o driver e a classe ANKI
    driver = webdriver.Chrome()
    anki = ANKI(driver, usuario, senha, data_locator)
    
    # Realiza login
    print("\nRealizando login...")
    anki.login()
    time.sleep(5)
    
    # Opção 1: Criar um novo Deck
    if selector == 1:
        deck_name = input("Digite o nome do deck a ser criado: ")
        anki.creat_deck(deck_name)
        time.sleep(3)
        print("Deck Criado")
    
    # Opção 2: Adicionar Cards em um deck já criado
    elif selector == 2:
        deck_name = input("Digite o nome do seu deck: ")
        anki.add_card()
        time.sleep(3)
        anki.select_deck(deck_name)
        print("Lendo os Cards da planilha...")
        anki.read_cards_sheet()
        time.sleep(3)
        anki.send_all_cards()
        time.sleep(3)
        anki.add_button()
        print("Cards sendo adicionados")
        time.sleep(6)
    
    # Opção 3: Criar um novo Deck e adicionar Cards
    elif selector == 3:
        deck_name = input("Digite o nome do seu deck: ")
        anki.creat_deck(deck_name)
        time.sleep(3)
        anki.click_deck(deck_name)
        time.sleep(3)
        anki.add_card()
        time.sleep(3)
        anki.select_deck(deck_name)
        print("Lendo os Cards da planilha...")
        anki.read_cards_sheet()
        time.sleep(3)
        anki.send_all_cards()
        time.sleep(3)
        anki.add_button()
        print("Cards sendo adicionados")
        time.sleep(6)
    
    print("\nProcesso concluído. Fechando o navegador.")
    driver.quit()

if __name__ == '__main__':
    main()
