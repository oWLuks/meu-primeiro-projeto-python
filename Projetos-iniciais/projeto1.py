#/**************************************************************************************
# Autor: Wagner Lucas
# Componente Curricular: Algoritmos I
# Concluido em: 26/03/2025
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum 
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

print("=" * 121)
print("{:^121}".format("ViaFeira"))
print("=" * 121)
print(
    "{:^121}".format("Após Escolher a Opção Desejada, Digite o Número Correspondente. ")
)
print(
    "{:^121}".format("(Por exemplo: Se você escolheu a Opção 1, digite o número “1”).")
)
print("=" * 121)

passagem  = input("Valor da passagem: R$ ") # Definindo o valor da passagem
inicio = 0
# ====================== Verificador para saber se é numérico =======================
while not passagem.isdigit(): # Verificando se o valor da passagem não é um numérico.
    print("O valor tem que ser numérico! Tente novamente!")
    print("="*121)
    print("{:^121}".format("ViaFeira"))
    print("="*121)
    print("{:^121}".format('Após Escolher a Opção Desejada, Digite o Número Correspondente. '))
    print("{:^121}".format('(Por exemplo: Se você escolheu a Opção 1, digite o número “1”).'))
    print("="*121)
    passagem  = input("Valor da passagem: R$ ") # perguntando novamente até que seja enviado um valor numerico
passagem = float(passagem) # Transformando a variavel passagem um valor float

inicio = 0
recarga = 0 # Valor Recarregado 
# ====================== Variaveis para classe Padrão ================================
saldo_padrao = 0 # Valor Total Recarregado 
qtd_recargas_padrao = 0 # Quantidade de Recargas Feitas
pass_padrao_total = 0 # Valor Total Gasto Com Passagens
qtd_passagens_padrao = 0 # Quantidade de Passagens Feitas
saldo_restante = 0 # Saldo Restante 
# ====================== Variaveis para classe Estudante/Idosos ======================
saldo_ie = 0 # Valor Total Recarregado 
qtd_recargas_ie = 0 # Quantidade de Recargas Feitas
pass_ie_total = 0 # Valor Total Gasto Com Passagens
qtd_passagens_ie = 0 # Quantidade de Passagens Feitas
saldo_restante_ie = 0 # Saldo Restante
# ====================== Variaveis para classe Social=================================
saldo_social = 0 # Valor Total Recarregado 
qtd_recargas_social = 0 # Quantidade de Recargas Feitas
pass_social_total = 0 # Valor Total Gasto Com Passagens
qtd_passagens_social = 0 # Quantidade de Passagens Feitas
saldo_restante_social = 0 # Saldo Restante

while inicio != 2: # Enquanto o valor de inicio não for 2 o looping continuara rodando.
    escolha = 0
# ====================== Criando a tela inicial ====================================
    print("=" * 121)
    print("{:^121}".format("TELA INICIAL"))
    print("=" * 121)
    print("Opções:\n[ 1 ] Escolha sua categoria\n[ 2 ] Encerrar Programa\n ")
    inicio = input("Digite sua opção: ")

# ====================== Verificador para saber se é numérico =======================
    while not inicio.isdigit() or int(inicio) <= 0 or int(inicio) > 2:
        print("Escolha uma opção válida! Tente novamente.")
        print("=" * 121)
        print("{:^121}".format("TELA INICIAL"))
        print("=" * 121)
        print ("[ 1 ] Escolha sua categoria\n[ 2 ] Sair do Programa")
        inicio = input("Digite sua opção: ") 
    inicio = int(inicio)

    if inicio == 1: # Caso seja escolhida a opção 1 sera mostrado todas as classes
        print("=" * 121)
        print("{:^121}".format("Escolha sua categoria"))
        print("=" * 121)
        print("[ 1 ] Padrao\n[ 2 ] Idoso/Estudante\n[ 3 ] Social")

        categoria = input("Digite sua opção: ")

        while not categoria.isdigit() or int(categoria) <= 0 or int(categoria) > 3: # Verificando se o valor digitado é numérico e também verificando se a a opção digitada esta entre as opções existentes
            print("Escolha uma opção válida! Tente novamente.")
            print("[ 1 ] Padrao\n[ 2 ] Idoso/Estudante\n[ 3 ] Social")
            categoria = input("Digite sua opção: ")
        categoria = int(categoria) # caso seja digitado um valor numérico, transforma a variavel categoria em inteiro
    
    # ========================== Menu Incial ====================================    
        while escolha != 4:
            print("=" * 121)
            print("{:^121}".format("ViaFeira"))
            print("=" * 121)
            print(
                "[ 1 ] Recarga\n[ 2 ] Comprar passagem\n[ 3 ] Imprimir relatório\n[ 4 ] Voltar Para Tela Inicial"
            )
            escolha = input("Digite sua opção: ")
            
            while not escolha.isdigit() or int(escolha) <= 0 and int(escolha) > 4: # Verificando se o valor digitado é numérico e também verificando se a a opção digitada está entre as opções existentes
                print("Escolha uma opção válida! Tente novamente.")
                print("=" * 121)
                print("{:^121}".format("O QUE DESEJA?"))
                print("=" * 121)
                print('[ 1 ] Recarga\n[ 2 ] Comprar passagem\n[ 3 ] Imprimir relatório\n[ 4 ] Voltar para tela inicial')
                escolha = input("Escolha sua opção: ")
            escolha = int(escolha)

            if escolha == 1:  # Efetuar a Recarga
                recarga = input("Digite o valor da recarga: R$ ")
                while not recarga.isdigit():
                    print("Escolha uma opção válida! Tente novamente.")
                    recarga = input("Digite o valor da recarga: R$ ")
                recarga = float(recarga)
                print(f"Voce recarregou R$ {recarga}")
             # ----------------- Variável P/ Relatório --------------------- #
                if categoria == 1: # Armazenamento das quantidades de vezes e valores recarregados(as) da categoria Padrão
                    saldo_padrao += recarga
                    qtd_recargas_padrao += 1

                elif categoria == 2: # Armazenamento das quantidades de vezes e valores recarregados(as) da categoria Estudante/Idoso
                    saldo_ie += recarga
                    qtd_recargas_ie += 1
                elif categoria == 3: # Armazenamento das quantidades de vezes e valores recarregados(as) da categoria social
                    saldo_social += recarga
                    qtd_recargas_social += 1
             # ------------------------------------------------------------- #
            elif escolha == 2:  # Comprar Passagem
                print("=" * 121)
                print(f"Valor da passagem: R${passagem}")

                if categoria == 1:
                    passagem_padrao = passagem # Paga Passagem Inteira
                    if recarga >= passagem: # Verificação se o saldo é maior ou igual á passagem
                        saldo_restante = recarga - passagem
                        print( f"Você adquiriu uma passagem no valor de: R$ {passagem_padrao}")
                        pass_padrao_total += passagem_padrao
                        qtd_passagens_padrao += 1
                    else:
                        print(f"Você Não Tem Saldo Suficiente, Por favor Recarregue. Saldo: {recarga}")
             
                elif categoria == 2:
                    passagem_ie = passagem / 2 # Paga Metade da Passagem
                    if recarga >= passagem_ie:  # Verificação se o saldo é maior ou igual á passagem
                        saldo_restante_ie = recarga - passagem_ie
                        print(f"Você adquiriu uma passagem no valor de: R$ {passagem_ie}")
                        pass_ie_total += passagem_ie
                        qtd_passagens_ie += 1
                    else:
                        print(f"Você Não Tem Saldo Suficiente, Por favor Recarregue. Saldo: {recarga}")     
             
                elif categoria == 3:
                    passagem_social = passagem * 0.2 # Paga 20% da Passagem
                    if recarga >= passagem_social:  # Verificação se o saldo é maior ou igual á passagem
                        saldo_restante_social = recarga - passagem_social
                        print(f"Você adquiriu uma passagem no valor de: R$ {passagem_social}")
                        pass_social_total += passagem_social
                        qtd_passagens_social += 1
                    else:
                        print(f"Você Não Tem Saldo Suficiente, Por favor Recarregue. Saldo: {recarga}")           
             
            elif escolha == 3:  # Imprimir o Relatório
                # Relatório da Categoria Padrão
                print("=" * 121)
                print(f"Padrão")
                print("=" * 121)
                print(f"O total de recargas feitas foi de R${saldo_padrao}")
                print(f"Foram feitas o total de {qtd_recargas_padrao} recargas")
                print(f"A Quantidade de passagens compradas foram de {qtd_passagens_padrao}")
                print(f"O valor total gasto com passagens foi de R${pass_padrao_total}")
                print(f"Saldo restante R${saldo_restante}")
                # Relatório da Categoria Estudante/Idoso
                print("=" * 121)
                print(f"Estudante/Idoso")
                print("=" * 121)
                print(f"O total de recargas feitas foi de R${saldo_ie}")
                print(f"Foram feitas o total de {qtd_recargas_ie} recargas")
                print(f"A Quantidade de passagens compradas foram de {qtd_passagens_ie}")
                print(f"O valor total gasto com passagens foi de R${pass_ie_total}")
                print(f"Saldo restante R${saldo_restante_ie}")
                # Relatório da Categoria Social
                print("=" * 121)
                print(f"Social")
                print("=" * 121)
                print(f"O total de recargas feitas foi de R${saldo_social}")
                print(f"Foram feitas o total de {qtd_recargas_social} recargas")
                print(f"A Quantidade de passagens compradas foram de {qtd_passagens_social}")
                print(f"O valor total gasto com passagens foi de R${pass_social_total}")
                print(f"Saldo restante R${saldo_restante_social}")
print("=" * 121)
print("{:^121}".format("OBRIGADO POR USAR MEU PROGRAMA!"))
print("=" * 121)