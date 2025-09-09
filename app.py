import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

system_message = SystemMessage(
    content=(
        "Instruções"
        "Você é um assistente de uma padaria que deve responder somente a perguntas relacionadas à padaria, e nada mais"
        "Os itens presentes nessa padaria são divididos em categorias e seus respectivos valores (valores estão por unidade) são:"
        "Pães: Pão francês = R$0.50, Pão de leite = R$0.70, Pão de cará = R$0.90, Brioche = R$1.10; Salgados: Joelho/Misto = R$2.40, Pedaço de torta salgada (Frango, Atum) = R$4.00, Coxinha = R$2.00, Hamburgão = R$3.00, Bauru = R$3.50, Empadinha = R$1.50, Pão de queijo: R$1.00; Doces: Bolos (Chocolate, Fubá, Cenoura) = R$7.00, Broa de milho = R$1.70, Pedaço de torta doce (Morango, Limão)= R$4.50, Carolina = R$0.30, Bomba de chocolate = R$1.40"
        "Caso o cliente pergunte sobre um item, não pergunte se ele deseja adquirir, apenas informe o preço junto do item"
        "Caso o cliente queira saber quanto custa uma certa quantidade de um item, realize a soma do preço da unidade e informe, se ele perguntar por outra medida indique que vendemos por unidade"
        "Você deve responder às perguntas de maneira objetiva"
        "Caso a pergunta não tenha a ver com a padaria, recuse-a explicando que não pode responder pois não está em seu escopo e peça para o usuário refazer a pergunta"
    )
)

def envia_mensagem(mensagem_usuario, mensagens_anteriores):
    mensagens = [system_message] + mensagens_anteriores + [HumanMessage(content=mensagem_usuario)]
    resposta = llm.invoke(mensagens)
    return resposta.content

def faz_resumo(mensagens):
    resumo_instrucao = SystemMessage(
        content=(
            "O resumo deve ser formatado por enumeração, comentando brevemente cada pergunta e sua respectiva resposta. Agradeça ao final da mensagem pela preferência"
            "Dentro desse resumo, não inclua contas, apenas o resultado delas"
        )
    )
    mensagens_resumo = [system_message] + mensagens + [resumo_instrucao]
    resposta_resumo = llm.invoke(mensagens_resumo)
    return resposta_resumo.content

def conta_pergunta(contador): 

    match contador: 

        case 0: 

            return print("3 perguntas restantes:\n") 

        case 1: 

            return print("2 perguntas restantes:\n")

        case 2: 

            return print("Última pergunta:\n") 

def chat():
    mensagens_anteriores = []
    contador = 0
    max = 3

    print("\nBem vindo à Padaria Prataria, sou o assistente Pãopei, em que posso ajudar? (Digite 'fim' caso queira interromper o atendimento)\n")
    while True:
        conta_pergunta(contador)
        entrada = input("Digite: ")
        mensagens_anteriores.append(HumanMessage(content=entrada))
        contador += 1

        if entrada == "fim":
            break

        resposta = envia_mensagem(entrada, mensagens_anteriores)
        print(f"\nPãopei:\n{resposta}\n\n")
        
        if contador == max:
            resumo = faz_resumo(mensagens_anteriores)
            print(resumo)
            break

if __name__ == "__main__":
    chat()