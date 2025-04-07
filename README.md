# RoboAnki 🤖📚

RoboAnki é um projeto de automação que utiliza o [Selenium](https://www.selenium.dev/) para interagir com o [AnkiWeb](https://ankiweb.net/). O objetivo do projeto é automatizar tarefas como login, criação de decks e adição de cards, lendo dados de uma planilha (Excel ou CSV) para quem deseja editar seus flashcards de forma mais rápida.

## Funcionalidades Principais ✨
Login automático no AnkiWeb

Criação de decks de forma programática

Adição de cards em massa a partir de planilhas

Suporte a múltiplos formatos de dados (Excel, CSV)

Estrutura modular e fácil de estender


## Estrutura do Projeto 🗂 

- **Data/**: Contém arquivos de dados (por exemplo, `cards.xlsx` com as colunas `Front`, `Back` e `Tag`).  
- **src/models/**: Onde reside a lógica principal, como o arquivo `functions.py` com as classes e métodos para automação.  
- **tests.py**: Script que orquestra as funções, chamando login, criação de deck, leitura da planilha e envio dos cards.


## Pré-requisitos ⚙️

- **Python 3.x**  
- **Selenium**  
- **Pandas**  
- Um **WebDriver** compatível (por exemplo, [ChromeDriver](https://chromedriver.chromium.org/) se usar o Google Chrome)

## Começando 🚀 

git clone https://github.com/seu-usuario/RoboAnki.git
cd RoboAnki

## Personalização 📝

Edite o arquivo src/models/functions.py para:

Ajustar os seletores CSS/XPath conforme atualizações do AnkiWeb

Modificar o fluxo de automação

Adicionar novas funcionalidades

## Contribuição 🤝 

Contribuições são bem-vindas! Siga estes passos:

Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-funcionalidade)

Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')

Push para a branch (git push origin feature/nova-funcionalidade)

Abra um Pull Request
