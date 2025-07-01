STATUS_PERMITIDO = ['ATIVO', 'FINALIZADO', 'STAND-BY']
projetos = {}

def cadastrar_projeto():
    """
    Cadastra um novo projeto no dicionário 'projetos'.
    Solicita ID, nome, descrição e status do projeto.
    Verifica duplicidade e valida status permitido.
    """
    identificador_projeto = input("\nDigite o ID do novo projeto: ").upper().strip()

    if identificador_projeto not in projetos:
        nome_projeto = input("\nInforme o nome do novo projeto: ")
        descricao_projeto = input("Digite uma breve descrição para o projeto: ")
        status_projeto = input("\nATIVO\n" \
        "FINALIZADO\n" \
        "STAND-BY\n" \
        "\nQual status do projeto? ").upper().strip()

        if status_projeto not in STATUS_PERMITIDO:
            print("\nDefinição de status inválida!")
            return
        else:
            projetos[identificador_projeto] = {'Nome': nome_projeto, 'Descrição': descricao_projeto, 'Status': status_projeto}
            print("\nProjeto cadastrado com sucesso!\n")
    
    else:
        print("\nEste projeto já está cadastrado!\n")


def cadastrar_tarefa():
    if projetos:
        i = 1

        for code in projetos:
            print(f"{i} - {code}")
            i += 1

        j = 0
        cadastrar_novamente = 'SIM'
        while cadastrar_novamente == 'SIM':
            selecionar_codigo = input("\nDigite o código equivalente ao projeto que deseja cadastrar tarefa: ").upper().strip()

            if selecionar_codigo in projetos:
                titulo_tarefa = input("\nInforme o título da tarefa: ").upper()
                status_tarefa = input("\nATIVO\n" \
                "FINALIZADO\n" \
                "STAND-BY\n" \
                "\nQual status do projeto? ").upper().strip()

                if status_tarefa in STATUS_PERMITIDO:

                    for i in lista_tarefas:
                        lista_tarefas = [{'Título da tarefa': titulo_tarefa, 'Status da tarefa': status_tarefa}]
                        projetos[selecionar_codigo]['Tarefas'] = lista_tarefas

                    print("\nTarefa cadastrada com sucesso!\n")

                    cadastrar_novamente = input("\nDeseja cadastrar mais alguma tarefa no projeto [SIM/NÃO]:\n").strip().upper()
                
                else:
                    print("\nStatus inválido!\n")
        else:
            print("\nCódigo inválido!\n")
    else:
        print("\nNão há projetos cadastrados!\n")


def listar_projetos():
    """
    Verifica se há projetos cadastrados e, se houver, é realizado
    a listagem desses projetos, evidenciando 'Nome' e o 'Código'
    """
    if projetos:
        i = 1
        print("\n=== LISTA DE PROJETOS ===\n")

        for codigo, name in projetos.items():
            print(f"{i} - Código do projeto: {codigo} | Nome do projeto: {name ['Nome']}")
            i += 1

    else:
        print("\nNão há projetos cadastrados!\n")


def listar_tarefas():
    if projetos:
        i = 1

        print("\n=== LISTA DE PROJETOS ===\n")
        for code in projetos:
            print(f"{i} - {code}")
            i += 1

        selecionar_codigo = input("\nInforme o código do projeto que deseja visualizar as tarefas: ").strip().upper()
        i = 1

        print("\n=== LISTA DE TAREFAS DO PROJETO ===\n")
        if 'Tarefas' in projetos[selecionar_codigo]:
            for tarefa in projetos[selecionar_codigo]['Tarefas']:
                print(f"Tarefa {i}: {tarefa['Título da tarefa']} | Status: {tarefa['Status da tarefa']}")
                i += 1

        else:
            print("\nSem tarefas cadastradas no projeto!\n")    
    else:
        print("\nNão há projetos cadastrados!\n")

menu_principal = True
while menu_principal: 
    print("\n=== GERENCIADOR DE PROJETOS ===\n")
    print("1 - Cadastrar projeto")
    print("2 - Cadastrar tarefa")
    print("3 - Listar projetos")
    print("4 - Listar tarefas de um projeto")
    print("5 - Atualizar status da tarefa")
    print("6 - Exibir relatório")
    print("7 - Sair\n")

    selecionar_opcao = input("Informe o número referente à opção desejada: ")
    
    try:
        selecionar_opcao = int(selecionar_opcao)
    except ValueError:
        print("\nSomente números!\n")
        continue

    if selecionar_opcao == 1:
        cadastrar_projeto()
    
    elif selecionar_opcao == 2:
        cadastrar_tarefa()

    elif selecionar_opcao == 3:
        listar_projetos()

    elif selecionar_opcao == 4:
        listar_tarefas()

    elif selecionar_opcao == 5:
        pass

    elif selecionar_opcao == 6:
        pass

    elif selecionar_opcao == 7:
        menu_principal = False
        print("\nMenu finalizado com sucesso!")