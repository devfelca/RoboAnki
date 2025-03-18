from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

class ANKI:
    def __init__(self, browser, usuario, senha, data_locator):
        self.browser = browser
        self.url = "https://ankiweb.net/account/login"
        self.usuario = usuario
        self.senha = senha
        self.data_locator = data_locator

    def login(self):
        # Abre a URL de login
        self.browser.get(self.url)
        time.sleep(4)  # aguarda a página carregar

        # Localiza o campo de email usando XPath
        email_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[1]/input")
        # Localiza o campo de senha
        senha_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[2]/input")
        # Localiza o botão de login
        login_button = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[3]/button")
        
        # Preenche os campos e clica no botão de login
        email_input.send_keys(self.usuario)
        senha_input.send_keys(self.senha)
        login_button.click()

    def creat_deck(self, deck_name):

        deck_name_input = self.browser.find_element(By.XPATH, "/html/body/div/main/div[5]/div/button").click
        deck_name_input.send_keys(deck_name)
        deck_name_input = send_keys(Keys.RETURN)
        time.slep(3)

        
    def add_card(self):
        # Clica no link "Add Card"
        self.browser.find_element(By.XPATH, "/html/body/div/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(3)
           
    def send_cards(self, front, back, tag, deck):
        # Localiza os campos de entrada para o card
        deck_input = self.browser.finder_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/div")
        front_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[1]/div/div")
        back_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[2]/div/div")
        tag_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[3]/div/input")

        # Preenche os campos com os dados fornecidos
        front_input.send_keys(front)
        back_input.send_keys(back)
        tag_input.send_keys(tag)
        deck_input.send_keys(deck)
        
        # Corrige o seletor CSS para localizar o botão de adicionar o card
        add_button = self.browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-large.mt-2")
        add_button.click()
        time.sleep(3)

    def read_cards_sheet(self):
        """
        Lê a planilha e armazena os dados em self.cards_data.
        """
        if self.data_locator.endswith('.xlsx'):
            df = pd.read_excel(self.data_locator)
        elif self.data_locator.endswith('.csv'):
            df = pd.read_csv(self.data_locator)
        else:
            raise ValueError("Formato de arquivo não suportado. Use .xlsx ou .csv.")

        # Armazena os dados da planilha como uma lista de dicionários
        self.cards_data = df.to_dict('records')
        print("Planilha lida com sucesso. Dados armazenados.")

    def send_all_cards(self):
        """
        Itera sobre os dados armazenados e envia cada card.
        """
        if not self.cards_data:
            raise ValueError("Nenhum dado encontrado. Execute read_cards_sheet() primeiro.")

        for row in self.cards_data:
            front = row['Front']
            back = row['Back']
            tag = row['Tag']  # Certifique-se de que o cabeçalho da coluna é 'Tag'
            self.add_card()
            time.sleep(2)
            self.send_cards(front, back, tag)
            print(f"Card adicionado: Front = {front}, Back = {back}, Tag = {tag}")
            time.sleep(2)