STATUS_PERMITIDO = ['ATIVO', 'FINALIZADO', 'STAND-BY']
projetos = {}
lista_tarefas = []

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
    """
    Verifica se há projetos cadastrados e, se houver, é realizado
    a listagem desses projetos e a solicitação de dados cadastrais
    das tarefas para serem incluidas dentro desse projeto em 
    específico
    """
    if projetos:
        i = 1

        for code in projetos:
            print(f"{i} - {code}")
            i += 1

        selecionar_codigo = input("\nDigite o código equivalente ao projeto que deseja cadastrar tarefa: ").upper().strip()

        if selecionar_codigo in projetos:
            titulo_tarefa = input("\nInforme o título da tarefa: ").upper()
            codigo_tarefa = input("Defina um código para a tarefa: ").upper().strip()

            status_tarefa = input("\nATIVO\n" \
            "FINALIZADO\n" \
            "STAND-BY\n" \
            "\nQual status do projeto? ").upper().strip()

            if status_tarefa in STATUS_PERMITIDO:
           
                
                lista_tarefas.append({'Título da tarefa': titulo_tarefa, 'Status da tarefa': status_tarefa, 'Código da tarefa': codigo_tarefa})
                projetos[selecionar_codigo]['Tarefas'] = lista_tarefas

                print("\nTarefa cadastrada com sucesso!\n")
                
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
    """
    Verifica se há projetos cadastrados e, se houver, é realizada a
    verificação de tarefas dentro desse projeto. Em seguida, é feita 
    a listae dessas tarefas
    """
    if projetos:
        i = 1

        print("\n=== LISTA DE PROJETOS ===\n")
        for code in projetos:
            print(f"{i} - {code}")
            i += 1

        selecionar_codigo = input("\nInforme o código do projeto que deseja visualizar as tarefas: ").strip().upper()
        i = 1

        if 'Tarefas' in projetos[selecionar_codigo]:
            print("\n=== LISTA DE TAREFAS DO PROJETO ===\n")

            for tarefa in projetos[selecionar_codigo]['Tarefas']:
                print(f"Tarefa {i}: {tarefa['Título da tarefa']}")
                i += 1

        else:
            print("\nSem tarefas cadastradas no projeto!\n")    
    else:
        print("\nNão há projetos cadastrados!\n")


def atualizar_status_da_tarefa():
    if projetos:
        i = 1

        print("\n=== LISTA DE PROJETOS ===\n")
        for code in projetos:
            print(f"{i} - {code}")
            i += 1

        selecionar_codigo = input("\nInforme o código do projeto para acessar tarefas cadastradas: ")

        if 'Tarefas' in projetos[selecionar_codigo]:
            print("\n=== LISTA DE TAREFAS ===\n")

            i = 1
            for tarefas in projetos[selecionar_codigo]['Tarefas']:
                print(f"{i} - {tarefas['Título da tarefa']} | Código: {tarefas['Código da tarefa']} | Status: {tarefas['Status da tarefa']}")
                i += 1
            
            novo_status_tarefa = input("\nATIVO\n" \
            "FINALIZADO\n" \
            "STAND-BY\n" \
            "\nQual status do projeto? ").upper().strip()

            

            

        else:
            print("\nSem tarefas cadastradas nesse projeto1\n")
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