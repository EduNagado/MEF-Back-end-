import os
import re

#---------------------------------------------------------------------------MENU PRINCIPAL-----------------------------------------------------------------------------------------------------------#

def mostrar_menu_principal():
    print("""
    Menu Principal:
    1- Criar uma conta 
    2- Entrar na conta 
    3- Relatar um problema ou conversar com Assistente
    4- Exibir contas
    5- Sair 
    """)
1
#---------------------------------------------------------------------------MENU SECUNDARIO-----------------------------------------------------------------------------------------------------------#

def mostrar_menu_secundario():
    print("""
    Menu Secundário:
    1- Adicionar veículo
    2- Modificar veículo
    3- Remover veículo
    4- Exibir veículos
    5- Voltar ao menu principal
    """)

#---------------------------------------------------------------------------VALIDAR EMAIL------------------------------------------------------------------------------------------------------------#

def checar_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email.strip()))

#---------------------------------------------------------------------------VALIDAR COM NOME COMPLETO------------------------------------------------------------------------------------------------------------#

def checar_nome(nome):
    return bool(re.match(r'^[a-zA-ZÀ-ÿ\u00C0-\u017F]+([-\'\s]?[a-zA-ZÀ-ÿ\u00C0-\u017F]+)*$', nome.strip()))

#---------------------------------------------------------------------------VALIDAR COM SENHA------------------------------------------------------------------------------------------------------------#

def checar_senha(senha):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\W]{8,}$', senha.strip()))

#---------------------------------------------------------------------------VALIDAR MENU------------------------------------------------------------------------------------------------------------#

def checar_opcao(opcao, limite):
    return opcao.isdigit() and 1 <= int(opcao) <= limite

#---------------------------------------------------------------------------LISTA PARA VEICULOS E CONTAS-----------------------------------------------------------------------------------------------------------#

veiculos = []
contas = []


#---------------------------------------------------------------------------ENTRAR NA CONTA-----------------------------------------------------------------------------------------------------------#

def entrar_conta():
    print("Entrar na Conta...")
    if not contas:
        print("Crie uma conta antes de entrar.")
        return False

    while True:
        usuario = input("Usuário (Nome Completo ou E-mail): ")
        if usuario.strip():
            break
        else:
            print("O usuário (nome completo ou e-mail) não pode estar vazio. Por favor, tente novamente.")

    while True:
        senha_cliente = input("Senha: ")
        if senha_cliente.strip():
            break
        else:
            print("A senha não pode estar vazia. Por favor, tente novamente.")

    for conta in contas:
        if (usuario == conta["nome_completo"] or usuario == conta["email"]) and senha_cliente == conta["senha"]:
            print("Entrada realizada com sucesso!")
            return True
    
    print("Usuário ou senha incorretos.")
    return False


#---------------------------------------------------------------------------CRIAR CONTA------------------------------------------------------------------------------------------------------------#

def criar_conta():
    print("Criando Conta...")
    while True:
        nome_completo = input("Nome completo: ")
        if checar_nome(nome_completo):
            break
        else:
            print("O nome completo não está no formato válido. Por favor, tente novamente.")

    while True:
        email = input("E-mail: ")
        if checar_email(email):
            break
        else:
            print("O e-mail não está no formato válido. Por favor, tente novamente.")

    while True:
        senha = input("Senha: ")
        if checar_senha(senha):
            break
        else:
            print("A senha não está no formato válido. Por favor, tente novamente.")
            print("A senha deve conter uma letra maiúscula, uma letra minúscula, um número e no mínimo 8 caracteres.")

    conta = {
        "nome_completo": nome_completo,
        "email": email,
        "senha": senha,
    }
    contas.append(conta)
    print("Conta criada com sucesso!")


#---------------------------------------------------------------------------MODIFICAR VEICULO------------------------------------------------------------------------------------------------------------#

def modificar_veiculo():
    if not veiculos:
        print("Não há veículos para modificar.")
        return
    
    placa = input("Digite a placa do veículo que deseja modificar: ")
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            print(f"Modificando veículo {veiculo['marca']} {veiculo['modelo']}")
            veiculo["marca"] = input("Nova marca: ") or veiculo["marca"]
            veiculo["modelo"] = input("Novo modelo: ") or veiculo["modelo"]
            veiculo["ano"] = input("Novo ano: ") or veiculo["ano"]
            veiculo["cor"] = input("Nova cor: ") or veiculo["cor"]
            print("Veículo modificado com sucesso!")
            return
    
    print("Veículo não encontrado.")

#---------------------------------------------------------------------------REMOVER VEICULO------------------------------------------------------------------------------------------------------------#

def remover_veiculo():
    if not veiculos:
        print("Não há veículos para remover.")
        return
    
    placa = input("Digite a placa do veículo que deseja remover: ")
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            veiculos.remove(veiculo)
            print("Veículo removido com sucesso!")
            return
    
    print("Veículo não encontrado.")

#---------------------------------------------------------------------------ADICIONAR VEICULO------------------------------------------------------------------------------------------------------------#

def adicionar_veiculo():
    print("Adicionar novo veículo")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cor = input("Cor: ")
    placa = input("Placa: ")

    veiculo = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "cor": cor,
        "placa": placa
    }
    veiculos.append(veiculo)
    print("Veículo adicionado com sucesso!")

#---------------------------------------------------------------------------EXIBIR VEICULO------------------------------------------------------------------------------------------------------------#

def exibir_veiculos():
    if not veiculos:
        print("Não há veículos cadastrados.")
        return
    
    print("Veículos cadastrados:")
    for veiculo in veiculos:
        print(f"Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Ano: {veiculo['ano']}, Cor: {veiculo['cor']}, Placa: {veiculo['placa']}")

#---------------------------------------------------------------------------RELATAR PROBLEMAS COM A IA------------------------------------------------------------------------------------------#

def relatar_problema_assistente():
    print("Relatar um problema ou conversar com o Assistente...")
    while True:
        print("""
    Escolha uma das opções abaixo:
    1- Relatar problema
    2- Conversar com Assistente
    3- Voltar ao menu principal
        """)
        opcao_secundaria = input("Opção: ")

        if checar_opcao(opcao_secundaria, 3):
            opcao_secundaria = int(opcao_secundaria)

            if opcao_secundaria == 1:
                print("Descreva o problema que está enfrentando:")
                problema = input()
                print("Obrigado por descrever o problema! Vamos analisar e entrar em contato em breve.")
            elif opcao_secundaria == 2:
                print("Você pode fazer uma pergunta ou conversar com o Assistente.")
                pergunta = input("Pergunta: ")
                print(f"Assistente: Você perguntou '{pergunta}', mas o Assistente ainda não foi implementado!")
            elif opcao_secundaria == 3:
                break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

#---------------------------------------------------------------------------EXIBIR CONTA------------------------------------------------------------------------------------------------------------#

def exibir_contas():
    if not contas:
        print("Não há contas para exibir.")
        return

    print("Contas:")
    for conta in contas:
        print(f"Nome Completo: {conta['nome_completo']}, Email: {conta['email']}")

#---------------------------------------------------------------------------INICIAR------------------------------------------------------------------------------------------------------------#
def iniciar():
    print("Iniciando o Aplicativo...")

    usuario_logado = False
    while True:
        if not usuario_logado:
            mostrar_menu_principal()
            opcao = input("Opção: ")

            if checar_opcao(opcao, 5):
                opcao = int(opcao)
                if opcao == 1:
                    criar_conta()
                elif opcao == 2:
                    if entrar_conta():
                        usuario_logado = True
                        while usuario_logado:
                            mostrar_menu_secundario()
                            opcao_sec = input("Opção: ")
                            if checar_opcao(opcao_sec, 5):
                                opcao_sec = int(opcao_sec)
                                if opcao_sec == 1:
                                    adicionar_veiculo()
                                elif opcao_sec == 2:
                                    modificar_veiculo()
                                elif opcao_sec == 3:
                                    remover_veiculo()
                                elif opcao_sec == 4:
                                    exibir_veiculos()
                                elif opcao_sec == 5:
                                    usuario_logado = False
                                    print("Voltando ao menu principal...")
                            else:
                                print("Digite um número válido! (1 a 5)")
                elif opcao == 3:
                    relatar_problema_assistente()
                elif opcao == 4:
                    exibir_contas()
                elif opcao == 5:
                    print("Saindo do aplicativo...")
                    break
            else:
                print("Digite um número válido! (1 a 5)")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


iniciar()
