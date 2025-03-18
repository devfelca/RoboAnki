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
        time.sleep(4)  # aguarda a página carregar (ajuste conforme necessário)

        # Localiza o campo de email usando o XPath
        email_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[1]/input")
        # Localiza o campo de senha
        senha_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[2]/input")
        # Localiza o botão de login
        login_button = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[3]/button")
        
        # Preenche os campos e clica no botão de login
        email_input.send_keys(self.usuario)
        senha_input.send_keys(self.senha)
        login_button.click()

    def add_card(self):
    
       self.browser.find_element(By.XPATH, "/html/body/div/nav/div/div[2]/ul[1]/li[2]/a").click()
       time.sleep(3)
    
    def reed_cards_sheets(self):
        # Usa o data_locator já atribuído no __init__
        if self.data_locator.endswith('.xlsx'):
            df = pd.read_excel(self.data_locator)
        elif self.data_locator.endswith('.csv'):
            df = pd.read_csv(self.data_locator)
        else:
            raise ValueError("Formato de arquivo não suportado. Use .xlsx ou .csv.")

        # Itera sobre as linhas da planilha e adiciona os cards
        for index, row in df.iterrows():
            front = row['Front']
            back = row['Back']
            tag = row['Tag']  # Certifique-se de que a coluna na planilha se chama 'Tag'
            self.add_card()
            time.sleep(2)
            self.send_cards(front, back, tag)
            print(f"Card adicionado: Front = {front}, Back = {back}, Tag = {tag}")
            time.sleep(2)
        
        # Aqui é os 3 campos mais importantes do card, frente, verso e tags nessa ordem
    def send_cards(self, front, back, tag):
        
        front_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[1]/div/div")
        back_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[2]/div/div")
        tag_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[3]/div/div")

        front_input.send_keys(front)
        back_input.send_keys(back)
        tag_input.send_keys(tag)
        
        add_button = self.browser.find_element(By.CSS_SELECTOR, "btn btn-primary btn-large mt-2")
        add_button.click
       
