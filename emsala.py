
# --------------------------------------------------
# ESTUDAMAIS - PROTOTIPO DE ASSISTENTE EDUCACIONAL
# Objetivo: demonstrar a logica de um assistente
# de estudos usando recursos basicos de Python.
# --------------------------------------------------

def responder_duvida():
    """Apresenta uma explicacao simples sobre Python."""
    print("\n--- TIRA-DUVIDAS ---")
    print("Python e uma linguagem de programacao.")
    print("Ela pode ser usada para criar sites,")
    print("automatizar tarefas e desenvolver sistemas.")


def recomendar_material():
    """Recomenda um material conforme o assunto."""
    print("\n--- BUSCA DE MATERIAIS ---")
    assunto = input("Qual assunto deseja estudar? ").lower()

    # Verifica se o assunto informado e conhecido.
    if "python" in assunto:
        print("Recomendacao: estude variaveis e condicionais.")
    elif "banco de dados" in assunto or "sql" in assunto:
        print("Recomendacao: estude SELECT e INNER JOIN.")
    elif "redes" in assunto:
        print("Recomendacao: estude enderecamento IP.")
    else:
        print("Ainda nao temos uma recomendacao para esse assunto.")


def sugerir_estudo():
    """Sugere um proximo passo para o estudante."""
    print("\n--- PROXIMO PASSO ---")
    print("1. Revise a teoria do assunto.")
    print("2. Estude um exemplo resolvido.")
    print("3. Resolva exercicios praticos.")
    print("4. Revise os erros cometidos.")


def apresentar_exercicio():
    """Apresenta uma questao simples de pratica."""
    print("\n--- EXERCICIO DE PYTHON ---")
    print("Qual comando mostra uma mensagem na tela?")
    print("A) input()")
    print("B) print()")
    print("C) int()")

    resposta = input("Digite A, B ou C: ").strip().upper()

    # Compara a resposta com o gabarito.
    if resposta == "B":
        print("Correto! print() exibe uma mensagem.")
    else:
        print("Resposta incorreta. O gabarito e B: print().")


# Funcao principal: controla o menu do assistente.
def main():
    while True:
        print("\n===== ESTUDAMAIS =====")
        print("1 - Tirar uma duvida")
        print("2 - Buscar material")
        print("3 - Orientar meus estudos")
        print("4 - Praticar exercicio")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        # Executa a funcao correspondente a opcao.
        if opcao == "1":
            responder_duvida()
        elif opcao == "2":
            recomendar_material()
        elif opcao == "3":
            sugerir_estudo()
        elif opcao == "4":
            apresentar_exercicio()
        elif opcao == "0":
            print("Obrigado por estudar com a EstudaMais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


# Inicia o programa quando este arquivo e executado.
if __name__ == "__main__":
    main()
