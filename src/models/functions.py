from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
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
        """
        Cria um novo deck.
        Observação: Se o elemento de input estiver em iframe/shadow DOM,
        pode ser necessário alternar de contexto.
        Após clicar no botão, o campo de input fica ativo automaticamente.
        """
        # Clica no botão que abre a criação de deck
        self.browser.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-secondary").click()
        time.sleep(3)
        # Usa o elemento ativo para enviar o nome do deck
        prompt = self.browser.switch_to.alert
        # Envia o nome do deck para o prompt
        prompt.send_keys(deck_name)
        time.sleep(2)
        # Clica em "OK" para confirmar
        prompt.accept()

    def click_deck(self, deck_name):
        """Localiza a div correspondente ao deck pelo texto e clica no botão associado."""
        # Aguarda até que a div com o nome do deck apareça no DOM
        row = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'row light-bottom-border') and contains(., '{deck_name}')]")))
        # Dentro dessa div, localiza o botão com as classes que você mencionou
        button = row.find_element(By.XPATH, ".//button[contains(@class, 'btn btn-link pl-0')]")
        # Se o botão estiver fora da tela, rola até ele
        self.browser.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(1)
        # Opcional: aguarda até que o botão esteja clicável
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(button))
        # Tenta clicar "normalmente"
        try:
            button.click()
        except:
            # Se der ElementNotInteractableException, força o clique via JS
            self.browser.execute_script("arguments[0].click();", button)
        
    def add_card(self):
        # Clica no link "Add Card"
        self.browser.find_element(By.XPATH, "/html/body/div/nav/div/div[2]/ul[1]/li[2]/a").click()

    def add_button(self):
        #botão css dentro da página de adionar cards, usado após preencher os dados sobre os cards.
        self.browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-large.mt-2").click()

    def select_deck(self, deck_name):
        #na aba de adionar card, a função serve para digitar o nome do deck
        deck_input = self.browser.find_element(By.XPATH, "/html/body/div/main/div[2]/div/div/div[2]/input")
        deck_input.click()
        deck_input.send_keys(deck_name)
        deck_input.send_keys(Keys.TAB)
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.click()

    def send_cards(self, front, back, tag):
        """Localiza os campos de entrada para o card apenas usar caso o robô opere através do add_card pois essa
        função não considera os campos Type e Deck
        """
        front_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[1]/div/div")
        back_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[2]/div/div")
        tag_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[3]/div/input")

        # Preenche os campos com os dados fornecidos
        front_input.clear()
        front_input.send_keys(front)
        back_input.clear()
        back_input.send_keys(back)
        tag_input.clear()
        tag_input.send_keys(tag)
        
        # Chama o botão na na aba de adionar cards
        self.add_button()

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
        Pega os dados armazenados pela read_cards_sheet e chama a send_cards para a
        """
        if not self.cards_data:
            raise ValueError("Nenhum dado encontrado. Execute read_cards_sheet() primeiro.")

        for row in self.cards_data:
            front = row['Front']
            back = row['Back']
            tag = row['Tag']  # Certifique-se de que o cabeçalho da coluna é 'Tag'

            time.sleep(2)
            self.send_cards(front, back, tag)
            print(f"Card adicionado: Front = {front}, Back = {back}, Tag = {tag}")