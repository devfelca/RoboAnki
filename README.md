<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <title>RoboAnki - README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      line-height: 1.6;
      background-color: #fafafa;
    }
    pre {
      background: #f4f4f4;
      padding: 10px;
      border-radius: 5px;
      overflow-x: auto;
    }
    code {
      background: #f4f4f4;
      padding: 2px 4px;
      border-radius: 3px;
    }
    h1, h2, h3 {
      color: #333;
    }
    ul, ol {
      margin-left: 20px;
    }
    a {
      color: #0066cc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <h1>RoboAnki</h1>
  <p>
    Fala pessoal! O RoboAnki é um projeto de automação que utiliza o Selenium para interagir com o AnkiWeb. O objetivo do projeto é automatizar tarefas como o login, criação de decks e adição de cards, lendo os dados de uma planilha (Excel ou CSV) para facilitar a vida da galera que gosta de editar seus cards.
  </p>
  
  <h2>Estrutura do Projeto</h2>
  <pre>
ROBOANKI/
├── .venv/
├── .vscode/
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── Data/
│   └── cards.xlsx
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── functions.py
├── README.html
├── setup.bat
└── tests.py
  </pre>

  <h2>Dependências</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Selenium</li>
    <li>Pandas</li>
  </ul>

  <h2>Instalação</h2>
  <p>Instale as dependências com:</p>
  <pre>
pip install selenium pandas
  </pre>

  <h2>Como Funciona</h2>
  <ol>
    <li><strong>Login:</strong> O robô acessa o AnkiWeb e realiza o login com as credenciais fornecidas.</li>
    <li><strong>Criação do Deck:</strong> Um novo deck é criado através de um prompt JavaScript, e o deck é selecionado automaticamente.</li>
    <li><strong>Adição de Cards:</strong> Após abrir o formulário de “Add Card”, o robô lê os dados da planilha e envia os cards um a um.</li>
  </ol>

  <h2>Principais Funções</h2>
  <ul>
    <li><code>login()</code>: Realiza o login no AnkiWeb.</li>
    <li><code>creat_deck(deck_name)</code>: Cria um novo deck via prompt e seleciona-o.</li>
    <li><code>click_deck(deck_name)</code>: Localiza e clica no deck com base no nome.</li>
    <li><code>add_card()</code>: Abre o formulário de adição de card.</li>
    <li><code>send_cards(front, back, tag)</code>: Preenche os campos de um card e envia o mesmo.</li>
    <li><code>read_cards_sheet()</code>: Lê uma planilha e armazena os dados.</li>
    <li><code>send_all_cards()</code>: Itera sobre os dados lidos e envia os cards.</li>
  </ul>

  <h2>Exemplo de Uso</h2>
  <p>Para executar o teste principal, use o seguinte comando:</p>
  <pre>
python tests.py
  </pre>
  <p>O fluxo básico é:</p>
  <ol>
    <li>Login no AnkiWeb;</li>
    <li>Criação e seleção do deck;</li>
    <li>Abertura do formulário de adicionar card;</li>
    <li>Leitura dos dados da planilha;</li>
    <li>Envio dos cards.</li>
  </ol>

  <h2>Observações</h2>
  <p>
    Durante o desenvolvimento, foram usados <code>time.sleep()</code> para aguardar o carregamento das páginas. Para uma automação mais robusta, considere utilizar esperas explícitas com <code>WebDriverWait</code>.
  </p>

  <h2>Contribuições</h2>
  <p>
    Contribuições são bem-vindas! Se quiser melhorar o projeto, por favor, abra uma issue ou envie um pull request.
  </p>

  <h2>Licença</h2>
  <p>
    Este projeto está licenciado sob a <a href="https://opensource.org/licenses/MIT" target="_blank">MIT License</a>.
  </p>

  <h2>Contato</h2>
  <p>
    Email: <a href="felipe.coliver@outlook.com">in/felipe-cabral-554b9183</a>
  </p>
</body>
</html>
