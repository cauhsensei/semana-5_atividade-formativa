estudantes = []

def gerenciar_estudantes():
    print("Opção selecionada: Gerenciar estudantes")
  

def gerenciar_professores():
    print("Opção selecionada: Gerenciar professores")
    

def gerenciar_disciplinas():
    print("Opção selecionada: Gerenciar disciplinas")
  

def gerenciar_turmas():
    print("Opção selecionada: Gerenciar turmas")


def gerenciar_matriculas():
    print("Opção selecionada: Gerenciar matrículas")


def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar estudantes")
        print("2. Gerenciar professores")
        print("3. Gerenciar disciplinas")
        print("4. Gerenciar turmas")
        print("5. Gerenciar matrículas")
        print("6. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            if menu_gerenciar_estudantes():
                print("Encerrando aplicação")
                break
        elif opcao == "2":
            if menu_gerenciar_professores():
                print("Encerrando aplicação")
                break
        elif opcao == "3":
            if menu_gerenciar_disciplinas():
                print("Encerrando aplicação")
                break
        elif opcao == "4":
            if menu_gerenciar_turmas():
                print("Encerrando aplicação")
                break
        elif opcao == "5":
            if menu_gerenciar_matriculas():
                print("Encerrando aplicação")
                break
        elif opcao == "6":
            print("Encerrando aplicação")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

def menu_gerenciar_professores():
    while True:
        print("\nMenu de Operações - Gerenciar Professores:")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            print("\n=== EM DESENVOLVIMENTO ===")
            return menu_principal() 
        elif opcao == "5":
            return False  
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
    
            
def menu_gerenciar_estudantes():
    while True:
        print("\nMenu de Operações - Gerenciar Estudantes:")
        print("1. Incluir")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            editar_estudante()
        elif opcao == "4":
            excluir_estudante()
        elif opcao == "5":
            return False
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

        return True


def incluir_estudante():
    while True:
        codigo = int(input("Digite o código do estudante ('0' para cancelar): "))
        if codigo == 0:
            return menu_gerenciar_estudantes()

        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")

        estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
        estudantes.append(estudante)

        print("\nEstudante adicionado com sucesso!")


def listar_estudantes():
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados.")
    else:
        print("\nEstudantes cadastrados:")
        for estudante in estudantes:
            print("- Código: {}".format(estudante["codigo"]))
            print("  Nome: {}".format(estudante["nome"]))
            print("  CPF: {}".format(estudante["cpf"]))
            print("")

        input("Aperte Enter para voltar")

    return menu_gerenciar_estudantes()


def excluir_estudante():
    codigo = int(input("Digite o código do estudante a ser excluído: "))
    for estudante in estudantes:
        if estudante["codigo"] == codigo:
            estudantes.remove(estudante)
            print("Estudante excluído com sucesso!")
            return menu_gerenciar_estudantes()
    print("Estudante não encontrado.")
            

def editar_estudante():
    codigo = int(input("Digite o código do estudante a ser editado: "))
    for estudante in estudantes:
        if estudante["codigo"] == codigo:
            nome = input("Digite o nome do estudante: ")
            cpf = input("Digite o CPF do estudante: ")

            estudante["nome"] = nome
            estudante["cpf"] = cpf

            print("Estudante editado com sucesso!")
            return menu_gerenciar_estudantes()

    print("Estudante não encontrado.")


def menu_gerenciar_disciplinas():
    while True:
        print("\nMenu de Operações - Gerenciar Disciplinas:")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            print("\n=== EM DESENVOLVIMENTO ===")
            return menu_principal() 
        elif opcao == "5":
            return False  
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
            
def menu_gerenciar_turmas():
    while True:
        print("\nMenu de Operações - Gerenciar Turmas:")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            print("\n=== EM DESENVOLVIMENTO ===")
            return menu_principal()  
        elif opcao == "5":
            return False  
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")
            
def menu_gerenciar_matriculas():
    while True:
        print("\nMenu de Operações - Gerenciar Matriculas:")
        print("1. Incluir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal")

        opcao = input("Selecione uma opção: ")

        if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            print("\n=== EM DESENVOLVIMENTO ===")
            return menu_principal()  
        elif opcao == "5":
            return False  
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")

menu_principal()
