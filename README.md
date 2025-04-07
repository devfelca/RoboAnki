# RoboAnki

RoboAnki é um projeto de automação que utiliza o [Selenium](https://www.selenium.dev/) para interagir com o [AnkiWeb](https://ankiweb.net/). O objetivo do projeto é automatizar tarefas como login, criação de decks e adição de cards, lendo dados de uma planilha (Excel ou CSV) para quem deseja editar seus flashcards de forma mais rápida.


- **Data/**: Contém arquivos de dados (por exemplo, `cards.xlsx` com as colunas `Front`, `Back` e `Tag`).  
- **src/models/**: Onde reside a lógica principal, como o arquivo `functions.py` com as classes e métodos para automação.  
- **tests.py**: Script que orquestra as funções, chamando login, criação de deck, leitura da planilha e envio dos cards.

---

## Pré-requisitos

- **Python 3.x**  
- **Selenium**  
- **Pandas**  
- Um **WebDriver** compatível (por exemplo, [ChromeDriver](https://chromedriver.chromium.org/) se usar o Google Chrome)

Instale as dependências:
```bash
pip install selenium pandas
