# ChatbotIA
Este é um chatbot feito em python que utiliza o provedor de IA Groq e seu modelo de IA 'llama-3.3-70b-versatile', além de Langchain. Ele foi criado como tarefa para faculdade e utiliza parâmetros fictícios. Abaixo alguns detalhes de uso.

**Contexto**
Neste chatbot foi aplicado o contexto de uma padaria onde o bot é responsável pelo atendimento de clientes, por isso ele responderá apenas a perguntas que tenham relevância a seu propósito.

_Exemplos_

"Quanto está o preço do pão francês?" é uma pergunta válida que o bot responderá.
"Qual novela da Globo de passava na Turquia" é uma pergunta inválida que não será respondida pelo bot.

**Tecnologias**
Groq API
LangChain
Python 3.10+
python-dotenv

**Instalação**

_Clone este repositório:_

git clone [https://github.com/VictorRaSaFa/ChatbotIA.git](https://github.com/VictorRaSaFa/ChatbotIA.git)
cd ChatbotIA

_Instale as dependências:_

pip install -r requirements.txt

_Adicione sua chave api Groq onde está indicado no arquivo ".env":_

GROQ_API_KEY="Insira sua chave"

**Uso**

_Execute o chatbot com um dos seguintes comandos:_

python app.py
ou
py app.py

_Faça perguntas a ele:_

"Bem vindo à Padaria Prataria, sou o assistente Pãopei, em que posso ajudar?"
"Digite: Quais doces vocês têm?"

_Feitas 3 perguntas, um resumo das perguntas e respostas é apresentado:_

Aqui está um resumo das suas perguntas:
1. Perguntou sobre o preço de uma dúzia de pães de brioche, e a resposta foi R$13.20.
2. Perguntou sobre os doces disponíveis na padaria, e foram listados os itens com seus respectivos preços.
3. Perguntou se uma torta salgada custa o mesmo que uma torta doce, e a resposta foi que não, pois elas têm preços diferentes.

