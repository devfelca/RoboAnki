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
        """
        Cria um novo deck.
        Observação: Se o elemento de input estiver em iframe/shadow DOM,
        pode ser necessário alternar de contexto.
        Após clicar no botão, o campo de input fica ativo automaticamente.
        """
        # Clica no botão que abre a criação de deck
        create_deck_button = self.browser.find_element(By.XPATH, "/html/body/div/main/div[5]/div/button")
        create_deck_button.click()
        time.sleep(1)
        # Usa o elemento ativo para enviar o nome do deck
        active_input = self.browser.switch_to.active_element
        active_input.send_keys(deck_name)
        active_input.send_keys(Keys.RETURN)
        time.sleep(3)
        
    def add_card(self):
        # Clica no link "Add Card"
        self.browser.find_element(By.XPATH, "/html/body/div/nav/div/div[2]/ul[1]/li[2]/a").click()
        time.sleep(3)

    def add_button(self):
        #botão css dentro da página de afionar cards, usado após preencher os dados sobre os cards.
        self.browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-large.mt-2").click()
        time.sleep(3)

    def send_cards(self, front, back, tag):
        """Localiza os campos de entrada para o card apenas usar caso o robô opere através do add_card pois essa
        função não considera os campos Type e Deck
        """
        front_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[1]/div/div")
        back_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[2]/div/div")
        tag_input = self.browser.find_element(By.XPATH, "/html/body/div/main/form/div[3]/div/input")

        # Preenche os campos com os dados fornecidos
        front_input.send_keys(front)
        back_input.send_keys(back)
        tag_input.send_keys(tag)
        
        # Chama o botão na na aba de adionar cards
        self.add_button()
        time.sleep(3)

    def select_deck(self, name_deck):
        """
        Digita o nome do deck caso já criado, exemplo: anteriormente adionei através do send_cards
        e quero adicionar outros cards referentes, então ele tem que pegar o nome do card armazenado
        por uma variavél
        """
        name_deck = input("Digite o nome do seu deck")
        #identifica o campo "Deck" que corresponde aos decks já criados
        self.browser.find_element(By.XPATH, "/html/body/div/nav/div/div[2]/ul[1]/li[2]/a").click()
        deck_input.send_keys(name_deck)

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
            time.sleep(2)