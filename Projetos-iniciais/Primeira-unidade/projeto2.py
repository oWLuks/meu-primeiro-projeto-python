# /*******************************************************************************
# Autor: Wagner Lucas Monteiro da Silva
# Componente Curricular: Algoritmos I
# Concluido em: 30/08/2025
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# ******************************************************************************************/

# Informações Sobre o Funcionamento Dos Menus
print("===" * 40)
print(
    "{:^121}".format("Após Escolher a Opção Desejada, Digite o Número Correspondente. ")
)
print(
    "{:^121}".format("(Por exemplo: Se você escolheu a Opção 1, digite o número “1”). ")
)
print("===" * 40)

# Variavel do Menu principal
tipo = 0
# ================= VARIÁVEIS ACUMULADORAS ================= #

# Mega-Sena
total_arrecadado_mega = 0.0 # Premio total que foi movimentado no concurso
contador_mega = 0
acumula_mega = 0.0 # Acumulação para proximo concurso
acumulo_finais_mega = 0.0 # Acúmulo para concursos finais 0 ou 5
mega_especial = 0.0
total_liquido_mega = 0.0 # Premios que os jogadores realmente receberam

# Fundos Mega
total_Seg_mega = 0.0
total_fnc_mega = 0.0
total_COP_mega = 0.0
total_FUNPEN_mega = 0.0
total_FNSP_mega = 0.0
total_CAIXA_mega = 0.0
outros_mega = 0.0

# Quina
total_arrecadado_quina = 0.0
contador_quina = 0
acumula_quina = 0.0 # Acumulação para proximo concurso
acumulo_finais_quina = 0.0 # Acúmulo para concursos finais 5
quina_especial = 0.0
total_liquido_quina = 0.0 # Premios que os jogadores realmente receberam

# Fundos Quina
total_Seg_quina = 0.0
total_fnc_quina = 0.0
total_COP_quina = 0.0
total_FUNPEN_quina = 0.0
total_FNSP_quina = 0.0
total_CAIXA_quina = 0.0
outros_quina = 0.0

# Lotofácil
total_arrecadado_loto = 0.0
contador_loto = 0
acumula_loto = 0.0 # Acumulação para proximo concurso
acumulo_finais_loto = 0.0 #acumulo para concursos finais 0 (15 acertos)
loto_especial = 0.0
total_liquido_loto = 0.0 # Premios que os jogadores realmente receberam

# Fundos Loto
total_Seg_loto = 0.0
total_fnc_loto = 0.0
total_COP_loto = 0.0
total_FUNPEN_loto = 0.0
total_FNSP_loto = 0.0
total_CAIXA_loto = 0.0
outros_loto = 0.0

# Funções Organizadoras
def validacao_int(normal):
    while not normal.isdigit() or int(normal) < 1: # Verificação de Entrada
        print("Não é uma opção valida...")
        normal = input("Digite novamente: ")
    normal = int(normal)

def validacao_float(ponto):
    while not ponto.replace(".", "", 1).isdigit(): #Verificação de entrada válida para Float
        print("Numero invalido...")
        ponto = input("Digite qual o valor do bilhete: ")
    ponto = float(ponto)
     
def validacao_normal(player):
    while not player.isdigit() or int(player) < 0: # Verificação de Entrada
        print("Não é uma opção valida...")
        player = input("Digite novamente: ")
    player = int(player)

def validacao_especial(player):
    while not player.isdigit() or int(player) <= 0: # Verificação de Entrada
        print("Não é uma opção valida...")
        player = input("Digite novamente: ")
    player = int(player)
    
# Menu Principal

while tipo != 5:

    print("=" * 120)
    print("{:^120}".format("MENU PRINCIPAL"))
    print("=" * 120)
    print("Opções:\n [ 1 ] Loteria Normal\n [ 2 ] Loteria Especial\n [ 3 ] Estatisticas Gerais\n [ 4 ] Critérios de Distribuição\n [ 5 ] Sair do Programa")
    tipo = input("Digite sua opção: ")

    while not tipo.isdigit() or int(tipo) < 1 or int(tipo) > 5: # Verificador para saber se é uma opção válida
        print("Opção invalida...")
        tipo = input("Digite sua opção: ") 
    tipo = int(tipo)

    if tipo == 1: # Menu Normal
        print("=" * 120)
        print("{:^120}".format("LOTERIA NORMAL"))
        print("=" * 120)
        print(" [ 1 ] Mega-Sena\n [ 2 ] Quina\n [ 3 ] Lotofácil\n ")
        loteria_normal = (input("Digite sua opção: "))

        while not loteria_normal.isdigit() or int(loteria_normal) < 1 or int(loteria_normal) > 3: # Verificação de Entrada Válida
            print("Não existe essa opção...")
            loteria_normal = input("Digite sua opção: ")

        loteria_normal = int(loteria_normal)

        if loteria_normal == 1: # Mega-Sena
            print("-" * 60)
            valor_bilhetes = input("Digite qual o valor do bilhete: ")

            validacao_float(valor_bilhetes) # Validação de entrada para Numeros Float
            
            apostadores = input("Quantas apostas foram realizadas: ")

            validacao_int(apostadores) # Validação de entrada para Numeros inteiros

            # Calculos principais da Mega-sena
            arrecadacao_mega = apostadores * valor_bilhetes
            seguridade = arrecadacao_mega * 0.1732
            fnc = arrecadacao_mega * 0.03
            olimpico = arrecadacao_mega * 0.017
            funpen = arrecadacao_mega * 0.0314
            fnsp = arrecadacao_mega * 0.0926
            caixa = arrecadacao_mega * 0.0957
            outros = arrecadacao_mega * 0.1001

            # Atualização de Variáveis
            total_Seg_mega += seguridade
            total_fnc_mega += fnc
            total_COP_mega += olimpico
            total_FUNPEN_mega += funpen
            total_FNSP_mega += fnsp
            total_CAIXA_mega += caixa
            outros_mega += outros
            contador_mega += 1

            # Ganhadores da Mega-sena
            print("-" * 60)
            sena_mega = input("Digite o numero de ganhadores da Sena: ")

            validacao_normal(sena_mega)

            quina_mega = input("Digite o numero de ganhadores da Quina: ")
                              
            validacao_normal(quina_mega)

            quadra_mega = input("Digite o numero de ganhadores da Quadra: ")
                              
            validacao_normal(quadra_mega)

            # Premio bruto
            premio_bruto = arrecadacao_mega * 0.46 # 46% da Arrecadação total

            # Total de Ganhadores
            total_ganhadores_mega = sena_mega + quina_mega + quadra_mega

            # adiciona o acúmulo caso nao haja vencedores
            premio_bruto += acumula_mega
            acumula_mega = 0.0

            # Verifica e Adiciona o acúmulo dos concursos com final 0 e 5 ao prêmio bruto
            if contador_mega % 10 == 5 or contador_mega % 10 == 0:
                 premio_bruto += acumulo_finais_mega
                 acumulo_finais_mega = 0.0
            else:
                 premio_bruto = premio_bruto
                 acumulo_finais_mega += premio_bruto * 0.22

            # Premiação individual (Bruto)
            total_arrecadado_mega += premio_bruto
            sena_total = premio_bruto * 0.35
            quina_total = premio_bruto * 0.19
            quadra_total = premio_bruto * 0.19
            mega_especial = premio_bruto * 0.05
             
             # Verificação e Acumulo para quando houver/não houver vencedor
            if sena_mega > 0:
                 ganhadores_sena_bruto = sena_total / sena_mega

                 # Calculo pro Imposto de Renda da Sena
                 if ganhadores_sena_bruto > 0.0:
                      imposto_R_sena = ganhadores_sena_bruto * 0.30
                      ganhadores_sena_liquido = ganhadores_sena_bruto - imposto_R_sena
                      total_liquido_mega += ganhadores_sena_liquido * sena_mega
                 else:
                      imposto_R_sena = 0.0
                      ganhadores_sena_liquido = ganhadores_sena_bruto

            else:
                acumula_mega += sena_total
            
            if quina_mega > 0:
                 ganhadores_quina_bruto = quina_total / quina_mega

                 # Calculo pro Imposto de Renda da Quina
                 if ganhadores_quina_bruto > 0.0:
                      imposto_R_quina = ganhadores_quina_bruto * 0.30
                      ganhadores_quina_liquido = ganhadores_quina_bruto - imposto_R_quina
                      total_liquido_mega += ganhadores_quina_liquido * quina_mega
                 else:
                      imposto_R_quina = 0.0
                      ganhadores_quina_liquido = ganhadores_quina_bruto

            else:
                acumula_mega += quina_total

            if quadra_mega > 0:
                 ganhadores_quadra_bruto = quadra_total / quadra_mega

                 # Calculo pro Imposto de Renda da Quadra
                 if ganhadores_quadra_bruto > 0.0:
                      imposto_R_quadra = ganhadores_quadra_bruto * 0.30
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto - imposto_R_quadra
                      total_liquido_mega += ganhadores_quadra_liquido * quadra_mega
                 else:
                      imposto_R_quadra = 0.0
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto

            else:
                acumula_mega += quadra_total

            # Calcular a média da Loteria Mega-sena
            if total_ganhadores_mega > 0:
                 premio_medio_mega = total_liquido_mega / total_ganhadores_mega
            else:
                 premio_medio_mega = 0.0

            # Estatisticas Individuais
            print(" ")
            print("=" * 60)
            print("{:^60}".format("Comprovante - Mega-Sena"))
            print("=" * 60)
            print(f"Arrecadação total: R$ {arrecadacao_mega:.2f}")
            print(f"Prêmio bruto total: R$ {premio_bruto:.2f}")
            print(f"Prêmio médio: R$ {premio_medio_mega:.2f}")
            print("-" * 60)
            print(" Prêmios Por Ganhador: ")
            print("-" * 60)

                # Ganhadores da Sena
            print(f" Sena: ( {sena_mega} ganhadores )")
            if sena_mega > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_sena_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_sena:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_sena_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {sena_total:.2f}")  

                # Ganhadores da quina
            print(f" \nquina: ( {quina_mega} ganhadores )")
            if quina_mega > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quina_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quina:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quina_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {quina_total:.2f}")

                # Ganhadores da quadra
            print(f" \nquadra: ( {quadra_mega} ganhadores )")
            if quadra_mega > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quadra_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quadra:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quadra_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {quadra_total:.2f}")
                
                # Distribuição para os Fundos
            print("-" * 60)
            print(" Destinação Para os Fundos: ")
            print("-" * 60)
            print(f" Seguridade Social: R$ {seguridade:.2f}")
            print(f" Fundo Nacional de Cultura: R$ {fnc:.2f}")
            print(f" Comitê Olímpico e Paralímpico: R$ {olimpico:.2f}")
            print(f" Fundo Penitenciário Nacional: R$ {funpen:.2f}")
            print(f" Fundo Nacional de Segurança Pública: R$ {fnsp:.2f}")
            print(f" Custos Operacionais (CAIXA): R$ {caixa:.2f}")
            print(f" Outros Encargos e Taxas Legais: R$ {outros:.2f}")
            print("=" * 60)


        if loteria_normal == 2: # Quina
            print("-" * 60)
            valor_bilhetes = input("Digite qual o valor do bilhete: ")

            validacao_float(valor_bilhetes)

            apostadores = input("Quantas apostas foram realizadas: ")

            validacao_int(apostadores)

            # Calculos principais da Quina
            arrecadacao_quina = apostadores * valor_bilhetes
            seguridade = arrecadacao_quina * 0.1732
            fnc = arrecadacao_quina * 0.03
            olimpico = arrecadacao_quina * 0.017
            funpen = arrecadacao_quina * 0.0314
            fnsp = arrecadacao_quina * 0.0926
            caixa = arrecadacao_quina * 0.0957
            outros = arrecadacao_quina * 0.0601

            # Atualização de Variáveis
            total_Seg_quina += seguridade
            total_fnc_quina += fnc
            total_COP_quina += olimpico
            total_FUNPEN_quina += funpen
            total_FNSP_quina += fnsp
            total_CAIXA_quina += caixa
            outros_quina += outros
            contador_quina += 1

        # Ganhadores da Quina
            print("-" * 60)
            quina_quina = input("Digite o numero de ganhadores da quina: ")
                              
            validacao_normal(quina_quina)

            quadra_quina = input("Digite o numero de ganhadores da Quadra: ")
                              
            validacao_normal(quadra_quina)

            terno_quina = input("Digite o numero de ganhadores do Terno: ")
                              
            validacao_normal(terno_quina)        

            # Premio bruto
            premio_bruto = arrecadacao_quina * 0.50 # 50% da Arrecadação total

            # Total de Ganhadores
            total_ganhadores_quina = quina_quina + quadra_quina + terno_quina

            # adiciona o acumulo caso nao haja vencedores + o Acumulo pro proximo concurso
            premio_bruto += acumula_quina
            acumula_quina = 0.0

            # Verifica e Adiciona o acumulo dos concursos com final 5 ao prêmio bruto
            if contador_quina % 10 == 5:
                 premio_bruto += acumulo_finais_quina
                 acumulo_finais_quina = 0.0
            else:
                 premio_bruto = premio_bruto
                 acumulo_finais_quina += premio_bruto * 0.15
            
            # Acumulo para proximo concurso 
            acumula_quina += premio_bruto * 0.10

            # Premiação individual (Bruto)
            total_arrecadado_quina += premio_bruto
            quina_total = premio_bruto * 0.35
            quadra_total = premio_bruto * 0.15
            terno_total = premio_bruto * 0.10
            quina_especial = premio_bruto * 0.15
             
             # Verificação e Acumulo para quando houver/não houver vencedor
            if quina_quina > 0:
                 ganhadores_quina_bruto = quina_total / quina_quina

                 # Calculo pro Imposto de Renda da Quina
                 if ganhadores_quina_bruto > 0.0:
                      imposto_R_quina = ganhadores_quina_bruto * 0.30
                      ganhadores_quina_liquido = ganhadores_quina_bruto - imposto_R_quina
                      total_liquido_quina += ganhadores_quina_liquido * quina_quina
                 else:
                      imposto_R_quina = 0.0
                      ganhadores_quina_liquido = ganhadores_quina_bruto

            else:
                acumula_quina += quina_total
            
            if quadra_quina > 0:
                 ganhadores_quadra_bruto = quadra_total / quadra_quina

                 # Calculo pro Imposto de Renda da Quadra
                 if ganhadores_quadra_bruto > 0.0:
                      imposto_R_quadra = ganhadores_quadra_bruto * 0.30
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto - imposto_R_quadra
                      total_liquido_quina += ganhadores_quadra_liquido * quadra_quina
                 else:
                      imposto_R_quadra = 0.0
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto

            else:
                acumula_quina += quadra_total

            if terno_quina > 0:
                 ganhadores_terno_bruto = terno_total / terno_quina

                 # Calculo pro Imposto de Renda da Terno
                 if ganhadores_terno_bruto > 0.0:
                      imposto_R_terno = ganhadores_terno_bruto * 0.30
                      ganhadores_terno_liquido = ganhadores_terno_bruto - imposto_R_terno
                      total_liquido_quina += ganhadores_terno_liquido * terno_quina
                 else:
                      imposto_R_terno = 0.0
                      ganhadores_terno_liquido = ganhadores_terno_bruto

            else:
                acumula_quina += terno_total

            # Calcular a média da Loteria Quina
            if total_ganhadores_quina > 0:
                 premio_medio_quina = total_liquido_quina / total_ganhadores_quina
            else:
                 premio_medio_quina = 0.0

            # Estatisticas Individuais
            print(" ")
            print("=" * 60)
            print("{:^60}".format("Comprovante - Quina"))
            print("=" * 60)
            print(f"Arrecadação total: R$ {arrecadacao_quina:.2f}")
            print(f"Prêmio bruto total: R$ {premio_bruto:.2f}")
            print(f"Prêmio médio: R$ {premio_medio_quina:.2f}")
            print("-" * 60)
            print(" Prêmios Por Ganhador: ")
            print("-" * 60)

                # Ganhadores da quina
            print(f" Quina: ( {quina_quina} ganhadores )")
            if quina_quina > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quina_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quina:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quina_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {quina_total:.2f}")  

                # Ganhadores da quadra
            print(f" \nQuadra: ( {quadra_quina} ganhadores )")
            if quadra_quina > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quadra_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quadra:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quadra_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {quadra_total:.2f}")

                # Ganhadores do terno
            print(f" \nTerno: ( {terno_quina} ganhadores )")
            if terno_quina > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_terno_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_terno:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_terno_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {terno_total:.2f}")
                
                # Distribuição para os Fundos
            print("-" * 60)
            print(" Destinação Para os Fundos: ")
            print("-" * 60)
            print(f" Seguridade Social: R$ {seguridade:.2f}")
            print(f" Fundo Nacional de Cultura: R$ {fnc:.2f}")
            print(f" Comitê Olímpico e Paralímpico: R$ {olimpico:.2f}")
            print(f" Fundo Penitenciário Nacional: R$ {funpen:.2f}")
            print(f" Fundo Nacional de Segurança Pública: R$ {fnsp:.2f}")
            print(f" Custos Operacionais (CAIXA): R$ {caixa:.2f}")
            print(f" Outros Encargos e Taxas Legais: R$ {outros:.2f}")
            print("=" * 60)

        if loteria_normal == 3: # Lotofácil
            print("-" * 60)
            valor_bilhetes = input("Digite qual o valor do bilhete: ")

            validacao_float(valor_bilhetes)

            apostadores = input("Quantas apostas foram realizadas: ")

            validacao_int(apostadores)


            # Calculos principais da Lotofácil
            arrecadacao_loto = apostadores * valor_bilhetes
            seguridade = arrecadacao_loto * 0.1732
            fnc = arrecadacao_loto * 0.03
            olimpico = arrecadacao_loto * 0.017 # 17,32%
            funpen = arrecadacao_loto * 0.0314 # 17,32%
            fnsp = arrecadacao_loto * 0.0926 # 17,32%
            caixa = arrecadacao_loto * 0.0957 # 17,32%
            outros = arrecadacao_loto * 0.1266 # 17,32%

            # Atualização de Variáveis
            total_Seg_loto += seguridade
            total_fnc_loto += fnc
            total_COP_loto += olimpico
            total_FUNPEN_loto += funpen
            total_FNSP_loto += fnsp
            total_CAIXA_loto += caixa
            outros_loto += outros
            contador_loto += 1

            # Ganhadores da lotofácil
            print("-" * 60)
            premio_principal = input("Digite o numero de ganhadores dos Prêmios Principais (15 e 14 acertos): ")
                              
            validacao_normal(premio_principal)

            premiacao_fixa = input("Digite o numero de ganhadores da Premiação Fixa (11, 12, 13 acertos): ")
                              
            validacao_normal(premiacao_fixa)

            # Premio bruto
            premio_bruto = arrecadacao_loto * 0.4335 # 43,35% da Arrecadação total

            # Total de Ganhadores
            total_ganhadores_loto = premio_principal + premiacao_fixa

            # adiciona o acumulo caso nao haja vencedores
            premio_bruto += acumula_loto
            acumula_loto = 0.0

            # Verifica e Adiciona o acumulo dos concursos com final 0 ao prêmio bruto
            if contador_loto % 10 == 0:
                 premio_bruto += acumulo_finais_loto
                 acumulo_finais_loto = 0.0
            else:
                 premio_bruto = premio_bruto
                 acumulo_finais_loto += premio_bruto * 0.10 # 10%
            
            # Premiação individual (Bruto)
            total_arrecadado_loto += premio_bruto
            principal_total = premio_bruto * 0.62 # 62%
            fixa_total = premio_bruto * 0.15 # 15%
            loto_especial = premio_bruto * 0.13 # 13%
             
             # Verificação e Acumulo para quando houver/não houver vencedor
            if premio_principal > 0:
                 ganhadores_principal_bruto = principal_total / premio_principal

                 # Calculo pro Imposto de Renda da Premiaçao Principal
                 if ganhadores_principal_bruto > 0.0:
                      imposto_R_principal = ganhadores_principal_bruto * 0.30
                      ganhadores_principal_liquido = ganhadores_principal_bruto - imposto_R_principal
                      total_liquido_loto += ganhadores_principal_liquido * premio_principal
                 else:
                      imposto_R_principal = 0.0
                      ganhadores_principal_liquido = ganhadores_principal_bruto

            else:
                acumula_loto += principal_total
            
            if premiacao_fixa > 0:
                 ganhadores_fixa_bruto = fixa_total / premiacao_fixa

                 # Calculo pro Imposto de Renda da Premiação Fixa
                 if ganhadores_fixa_bruto > 0.0:
                      imposto_R_fixa = ganhadores_fixa_bruto * 0.30
                      ganhadores_fixa_liquido = ganhadores_fixa_bruto - imposto_R_fixa
                      total_liquido_loto += ganhadores_fixa_liquido * premiacao_fixa
                 else:
                      imposto_R_fixa = 0.0
                      ganhadores_fixa_liquido = ganhadores_fixa_bruto

            else:
                acumula_loto += fixa_total


            # Calcular a média da Loteria Lotofácil
            if total_ganhadores_loto > 0:
                 premio_medio_loto = total_liquido_loto / total_ganhadores_loto
            else:
                 premio_medio_loto = 0.0

            # Estatisticas Individuais
            print(" ")
            print("=" * 60)
            print("{:^60}".format("Comprovante - Lotofácil"))
            print("=" * 60)
            print(f"Arrecadação total: R$ {arrecadacao_loto:.2f}")
            print(f"Prêmio bruto total: R$ {premio_bruto:.2f}")
            print(f"Prêmio médio: R$ {premio_medio_loto:.2f}")
            print("-" * 60)
            print(" Prêmios Por Ganhador: ")
            print("-" * 60)

                # Ganhadores dos Prêmios Principais
            print(f" Prêmios Principais (15 e 14 acertos): ( {premio_principal} ganhadores )")
            if premio_principal > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_principal_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_principal:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_principal_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {principal_total:.2f}")  

                # Ganhadores da Premiação Fixa
            print(f" \nPremiação Fixa (11, 12, 13 acertos): ( {premiacao_fixa} ganhadores )")
            if premiacao_fixa > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_fixa_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_fixa:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_fixa_liquido:.2f}")
            else:
                print(f" Valor acumulado: R$ {fixa_total:.2f}")

                
                # Distribuição para os Fundos
            print("-" * 60)
            print(" Destinação Para os Fundos: ")
            print("-" * 60)
            print(f" Seguridade Social: R$ {seguridade:.2f}")
            print(f" Fundo Nacional de Cultura: R$ {fnc:.2f}")
            print(f" Comitê Olímpico e Paralímpico: R$ {olimpico:.2f}")
            print(f" Fundo Penitenciário Nacional: R$ {funpen:.2f}")
            print(f" Fundo Nacional de Segurança Pública: R$ {fnsp:.2f}")
            print(f" Custos Operacionais (CAIXA): R$ {caixa:.2f}")
            print(f" Outros Encargos e Taxas Legais: R$ {outros:.2f}")
            print("=" * 60)


           
    elif tipo == 2: # Menu Especial
        print("=" * 120)
        print("{:^120}".format("LOTERIA ESPECIAL"))
        print("=" * 120)
        print(" [ 1 ] Mega da Virada\n [ 2 ] Quina de São João\n [ 3 ] Lotofácil da independência")
        loteria_especial = input("Digite sua opção: ")

        while not loteria_especial.isdigit() or int(loteria_especial) < 1 or int(loteria_especial) > 3: # Verificação de Entrada Válida
            print("Não existe essa opção...")
            loteria_especial = input("Digite sua opção: ")
        loteria_especial = int(loteria_especial)

        if loteria_especial == 1: # Mega da virada
            print("-" * 60)
            valor_bilhetes = input("Digite qual o valor do bilhete: ")

            validacao_float(valor_bilhetes)

            apostadores = input("Quantas apostas foram realizadas: ")

            validacao_int(apostadores)


            # Calculos principais da Mega da virada
            arrecadacao_mega = apostadores * valor_bilhetes
            seguridade = arrecadacao_mega * 0.1732 # 17,32%
            fnc = arrecadacao_mega * 0.03 # 3%
            olimpico = arrecadacao_mega * 0.017 # 1,7%
            funpen = arrecadacao_mega * 0.0314 # 3,14%
            fnsp = arrecadacao_mega * 0.0926 # 9,26%
            caixa = arrecadacao_mega * 0.0957 # 9,57%
            outros = arrecadacao_mega * 0.1001 # 10,01%

            # Atualização de Variáveis
            total_Seg_mega += seguridade
            total_fnc_mega += fnc
            total_COP_mega += olimpico
            total_FUNPEN_mega += funpen
            total_FNSP_mega += fnsp
            total_CAIXA_mega += caixa
            outros_mega += outros
            contador_mega += 1

            # Ganhadores da Mega da virada
            print("-" * 60)
            sena_mega = input("Digite o numero de ganhadores da Sena: ")
                              
            validacao_especial(sena_mega)

            quina_mega = input("Digite o numero de ganhadores da Quina: ")
                              
            validacao_especial(quina_mega)

            quadra_mega = input("Digite o numero de ganhadores da Quadra: ")
                              
            validacao_especial(quadra_mega)           

            # Premio bruto
            premio_bruto = (arrecadacao_mega * 0.46) + mega_especial # 46% da Arrecadação total + Acúmulo
            valor_acumulado_usado = mega_especial
            mega_especial = 0.0

            # Total de Ganhadores
            total_ganhadores_mega = sena_mega + quina_mega + quadra_mega

            # Verifica e Adiciona o acúmulo dos concursos com final 0 e 5 ao prêmio bruto
            if contador_mega % 10 == 5 or contador_mega % 10 == 0:
                 premio_bruto += acumulo_finais_mega
                 acumulo_finais_mega = 0.0
            else:
                 premio_bruto = premio_bruto
                 acumulo_finais_mega += premio_bruto * 0.22 # 22%

            # Premiação individual (Bruto)
            total_arrecadado_mega += premio_bruto
            sena_total = premio_bruto * 0.35 # 35%
            quina_total = premio_bruto * 0.19 # 19%
            quadra_total = premio_bruto * 0.19 # 19%
            mega_especial = premio_bruto * 0.05 # 5%

            # Redistribuição Dos Premios
            if sena_mega == 0:
                 quina_total += sena_total
                 sena_total = 0.0

            if quina_mega == 0:
                 quadra_total += quina_total
                 quina_total = 0.0
             
             # Verificação e Acumulo para quando houver/não houver vencedor
            if sena_mega > 0:
                 ganhadores_sena_bruto = sena_total / sena_mega

                 # Calculo pro Imposto de Renda da Sena
                 if ganhadores_sena_bruto > 0.0:
                      imposto_R_sena = ganhadores_sena_bruto * 0.30
                      ganhadores_sena_liquido = ganhadores_sena_bruto - imposto_R_sena
                      total_liquido_mega += ganhadores_sena_liquido * sena_mega
                 else:
                      imposto_R_sena = 0.0
                      ganhadores_sena_liquido = ganhadores_sena_bruto

            if quina_mega > 0:
                 ganhadores_quina_bruto = quina_total / quina_mega

                 # Calculo pro Imposto de Renda da Quina
                 if ganhadores_quina_bruto > 0.0:
                      imposto_R_quina = ganhadores_quina_bruto * 0.30
                      ganhadores_quina_liquido = ganhadores_quina_bruto - imposto_R_quina
                      total_liquido_mega += ganhadores_quina_liquido * quina_mega
                 else:
                      imposto_R_quina = 0.0
                      ganhadores_quina_liquido = ganhadores_quina_bruto

            if quadra_mega > 0:
                 ganhadores_quadra_bruto = quadra_total / quadra_mega

                 # Calculo pro Imposto de Renda da Quadra
                 if ganhadores_quadra_bruto > 0.0:
                      imposto_R_quadra = ganhadores_quadra_bruto * 0.30
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto - imposto_R_quadra
                      total_liquido_mega += ganhadores_quadra_liquido * quadra_mega
                 else:
                      imposto_R_quadra = 0.0
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto

            # Calcular a média da Mega da virada
            if total_ganhadores_mega > 0:
                 premio_medio_mega = total_liquido_mega / total_ganhadores_mega
            else:
                 premio_medio_mega = 0.0

            # Estatisticas Individuais
            print(" ")
            print("=" * 60)
            print("{:^60}".format("Comprovante - Mega da Virada"))
            print("=" * 60)
            print(f"Arrecadação total: R$ {arrecadacao_mega:.2f}")
            print(f"Valor do Acumulado (5% dos concursos normais): R$ {valor_acumulado_usado:.2f}")
            print(f"Prêmio bruto total: R$ {premio_bruto:.2f}")
            print(f"Prêmio médio: R$ {premio_medio_mega:.2f}")
            print("-" * 60)
            print(" Prêmios Por Ganhador: ")
            print("-" * 60)

                # Ganhadores da Sena
            print(f" Sena: ( {sena_mega} ganhadores )")
            if sena_mega > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_sena_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_sena:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_sena_liquido:.2f}")

                # Ganhadores da quina
            print(f" \nquina: ( {quina_mega} ganhadores )")
            if quina_mega > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quina_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quina:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quina_liquido:.2f}")

                # Ganhadores da quadra
            print(f" \nquadra: ( {quadra_mega} ganhadores )")
            if quadra_mega > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quadra_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quadra:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quadra_liquido:.2f}")
                
                # Distribuição para os Fundos
            print("-" * 60)
            print(" Destinação Para os Fundos: ")
            print("-" * 60)
            print(f" Seguridade Social: R$ {seguridade:.2f}")
            print(f" Fundo Nacional de Cultura: R$ {fnc:.2f}")
            print(f" Comitê Olímpico e Paralímpico: R$ {olimpico:.2f}")
            print(f" Fundo Penitenciário Nacional: R$ {funpen:.2f}")
            print(f" Fundo Nacional de Segurança Pública: R$ {fnsp:.2f}")
            print(f" Custos Operacionais (CAIXA): R$ {caixa:.2f}")
            print(f" Outros Encargos e Taxas Legais: R$ {outros:.2f}")
            print("=" * 60)


        if loteria_especial == 2: # Quina de São João
            print("-" * 60)
            valor_bilhetes = input("Digite qual o valor do bilhete: ")

            validacao_float(valor_bilhetes)

            apostadores = input("Quantas apostas foram realizadas: ")

            validacao_int(apostadores)


            # Calculos principais da Quina da São João
            arrecadacao_quina = apostadores * valor_bilhetes
            seguridade = arrecadacao_quina * 0.1732 # 17,32%
            fnc = arrecadacao_quina * 0.03 # 3%
            olimpico = arrecadacao_quina * 0.017 # 1,7%
            funpen = arrecadacao_quina * 0.0314 # 3,14%
            fnsp = arrecadacao_quina * 0.0926 # 9,26%
            caixa = arrecadacao_quina * 0.0957 # 9,57%
            outros = arrecadacao_quina * 0.0601 # 6,1%

            # Atualização de Variáveis
            total_Seg_quina += seguridade
            total_fnc_quina += fnc
            total_COP_quina += olimpico
            total_FUNPEN_quina += funpen
            total_FNSP_quina += fnsp
            total_CAIXA_quina += caixa
            outros_quina += outros
            contador_quina += 1

        # Ganhadores da Quina de São João
            print("-" * 60)
            quina_quina = input("Digite o numero de ganhadores da quina: ")
                              
            validacao_especial(quina_quina)

            quadra_quina = input("Digite o numero de ganhadores da Quadra: ")
                              
            validacao_especial(quadra_quina)

            terno_quina = input("Digite o numero de ganhadores do Terno: ")
                              
            validacao_especial(terno_quina)            

            # Premio bruto
            premio_bruto = (arrecadacao_quina * 0.50) + quina_especial # 50% da Arrecadação total + Acúmulo
            valor_acumulado_usado = quina_especial
            quina_especial = 0.0

            # Total de Ganhadores
            total_ganhadores_quina = quina_quina + quadra_quina + terno_quina

            # adiciona o Acumulo pro proximo concurso
            premio_bruto += acumula_quina
            acumula_quina = 0.0

            # Verifica e Adiciona o acumulo dos concursos com final 5 ao prêmio bruto
            if contador_quina % 10 == 5:
                 premio_bruto += acumulo_finais_quina
                 acumulo_finais_quina = 0.0
            else:
                 premio_bruto = premio_bruto
                 acumulo_finais_quina += premio_bruto * 0.15 # 15%
            
            # Acumulo para proximo concurso 
            acumula_quina += premio_bruto * 0.10

            # Premiação individual (Bruto)
            total_arrecadado_quina += premio_bruto
            quina_total = premio_bruto * 0.35 # 35%
            quadra_total = premio_bruto * 0.15 # 15%
            terno_total = premio_bruto * 0.10 # 10%
            quina_especial = premio_bruto * 0.15 # 15%

            # Redistribuição Dos Premios
            if quina_quina == 0:
                 quadra_total += quina_total
                 quina_total = 0.0

            if quadra_quina == 0:
                 terno_total += quadra_total
                 quadra_total = 0.0
             
             # Verificação e Acumulo para quando houver/não houver vencedor
            if quina_quina > 0:
                 ganhadores_quina_bruto = quina_total / quina_quina

                 # Calculo pro Imposto de Renda da Quina
                 if ganhadores_quina_bruto > 0.0:
                      imposto_R_quina = ganhadores_quina_bruto * 0.30
                      ganhadores_quina_liquido = ganhadores_quina_bruto - imposto_R_quina
                      total_liquido_quina += ganhadores_quina_liquido * quina_quina
                 else:
                      imposto_R_quina = 0.0
                      ganhadores_quina_liquido = ganhadores_quina_bruto
            
            if quadra_quina > 0:
                 ganhadores_quadra_bruto = quadra_total / quadra_quina

                 # Calculo pro Imposto de Renda da Quadra
                 if ganhadores_quadra_bruto > 0.0:
                      imposto_R_quadra = ganhadores_quadra_bruto * 0.30
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto - imposto_R_quadra
                      total_liquido_quina += ganhadores_quadra_liquido * quadra_quina
                 else:
                      imposto_R_quadra = 0.0
                      ganhadores_quadra_liquido = ganhadores_quadra_bruto

            if terno_quina > 0:
                 ganhadores_terno_bruto = terno_total / terno_quina

                 # Calculo pro Imposto de Renda da Terno
                 if ganhadores_terno_bruto > 0.0:
                      imposto_R_terno = ganhadores_terno_bruto * 0.30
                      ganhadores_terno_liquido = ganhadores_terno_bruto - imposto_R_terno
                      total_liquido_quina += ganhadores_terno_liquido * terno_quina
                 else:
                      imposto_R_terno = 0.0
                      ganhadores_terno_liquido = ganhadores_terno_bruto

            # Calcular a média da Loteria Quina de São João
            if total_ganhadores_quina > 0:
                 premio_medio_quina = total_liquido_quina / total_ganhadores_quina
            else:
                 premio_medio_quina = 0.0

            # Estatisticas Individuais
            print(" ")
            print("=" * 60)
            print("{:^60}".format("Comprovante - Quina de São João"))
            print("=" * 60)
            print(f"Arrecadação total: R$ {arrecadacao_quina:.2f}")
            print(f"Valor do Acumulado (15% dos concursos normais): R$ {valor_acumulado_usado:.2f}")
            print(f"Prêmio bruto total: R$ {premio_bruto:.2f}")
            print(f"Prêmio médio: R$ {premio_medio_quina:.2f}")
            print("-" * 60)
            print(" Prêmios Por Ganhador: ")
            print("-" * 60)

                # Ganhadores da quina
            print(f" Quina: ( {quina_quina} ganhadores )")
            if quina_quina > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quina_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quina:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quina_liquido:.2f}")

                # Ganhadores da quadra
            print(f" \nQuadra: ( {quadra_quina} ganhadores )")
            if quadra_quina > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_quadra_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_quadra:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_quadra_liquido:.2f}")

                # Ganhadores do terno
            print(f" \nTerno: ( {terno_quina} ganhadores )")
            if terno_quina > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_terno_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_terno:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_terno_liquido:.2f}")
                
                # Distribuição para os Fundos
            print("-" * 60)
            print(" Destinação Para os Fundos: ")
            print("-" * 60)
            print(f" Seguridade Social: R$ {seguridade:.2f}")
            print(f" Fundo Nacional de Cultura: R$ {fnc:.2f}")
            print(f" Comitê Olímpico e Paralímpico: R$ {olimpico:.2f}")
            print(f" Fundo Penitenciário Nacional: R$ {funpen:.2f}")
            print(f" Fundo Nacional de Segurança Pública: R$ {fnsp:.2f}")
            print(f" Custos Operacionais (CAIXA): R$ {caixa:.2f}")
            print(f" Outros Encargos e Taxas Legais: R$ {outros:.2f}")
            print("=" * 60)

        if loteria_especial == 3: # Lotofácil da Independência
            print("-" * 60)
            valor_bilhetes = input("Digite qual o valor do bilhete: ")

            validacao_float(valor_bilhetes)

            apostadores = input("Quantas apostas foram realizadas: ")

            validacao_int(apostadores)


            # Calculos principais da Lotofácil da Independência
            arrecadacao_loto = apostadores * valor_bilhetes
            seguridade = arrecadacao_loto * 0.1732 # 17,32%
            fnc = arrecadacao_loto * 0.03 # 3%
            olimpico = arrecadacao_loto * 0.017 # 1,7%
            funpen = arrecadacao_loto * 0.0314 # 3,14%
            fnsp = arrecadacao_loto * 0.0926 # 9,26%
            caixa = arrecadacao_loto * 0.0957 # 9,57%
            outros = arrecadacao_loto * 0.1266 # 12,66%

            # Atualização de Variáveis
            total_Seg_loto += seguridade
            total_fnc_loto += fnc
            total_COP_loto += olimpico
            total_FUNPEN_loto += funpen
            total_FNSP_loto += fnsp
            total_CAIXA_loto += caixa
            outros_loto += outros
            contador_loto += 1

            # Ganhadores da Lotofácil da Independência
            print("-" * 60)
            premio_principal = input("Digite o numero de ganhadores dos Prêmios Principais (15 e 14 acertos): ")
                              
            validacao_especial(premio_principal)

            premiacao_fixa = input("Digite o numero de ganhadores da Premiação Fixa (11, 12, 13 acertos): ")
                              
            validacao_especial(premiacao_fixa)
              
            # Premio bruto
            premio_bruto = (arrecadacao_loto * 0.4335) + loto_especial # 43,35% da Arrecadação total + acúmulo
            valor_acumulado_usado = loto_especial
            loto_especial = 0.0

            # Total de Ganhadores
            total_ganhadores_loto = premio_principal + premiacao_fixa

            # Verifica e Adiciona o acumulo dos concursos com final 0 ao prêmio bruto
            if contador_loto % 10 == 0:
                 premio_bruto += acumulo_finais_loto
                 acumulo_finais_loto = 0.0
            else:
                 premio_bruto = premio_bruto
                 acumulo_finais_loto += premio_bruto * 0.10
            
            # Premiação individual (Bruto)
            total_arrecadado_loto += premio_bruto
            principal_total = premio_bruto * 0.62
            fixa_total = premio_bruto * 0.15
            loto_especial = premio_bruto * 0.13

            # Redistribuição Dos Premios
            if premio_principal == 0:
                 fixa_total += principal_total
                 principal_total = 0.0

             # Verificação para quando houver vencedor
            if premio_principal > 0:
                 ganhadores_principal_bruto = principal_total / premio_principal

                 # Calculo pro Imposto de Renda do Prêmio Principal
                 if ganhadores_principal_bruto > 0.0:
                      imposto_R_principal = ganhadores_principal_bruto * 0.30
                      ganhadores_principal_liquido = ganhadores_principal_bruto - imposto_R_principal
                      total_liquido_loto += ganhadores_principal_liquido * premio_principal
                 else:
                      imposto_R_principal = 0.0
                      ganhadores_principal_liquido = ganhadores_principal_bruto

            if premiacao_fixa > 0:
                 ganhadores_fixa_bruto = fixa_total / premiacao_fixa

                 # Calculo pro Imposto de Renda da Premiação Fixa
                 if ganhadores_fixa_bruto > 0.0:
                      imposto_R_fixa = ganhadores_fixa_bruto * 0.30
                      ganhadores_fixa_liquido = ganhadores_fixa_bruto - imposto_R_fixa
                      total_liquido_loto += ganhadores_fixa_liquido * premiacao_fixa
                 else:
                      imposto_R_fixa = 0.0
                      ganhadores_fixa_liquido = ganhadores_fixa_bruto

            # Calcular a média da Loteria Lotofácil da Independência
            if total_ganhadores_loto > 0:
                 premio_medio_loto = total_liquido_loto / total_ganhadores_loto
            else:
                 premio_medio_loto = 0.0

            # Estatisticas Individuais
            print()
            print("=" * 60)
            print("{:^60}".format("Comprovante - Lotofácil da Independência"))
            print("=" * 60)
            print(f"Arrecadação total: R$ {arrecadacao_loto:.2f}")
            print(f"Valor do Acumulado (13% dos concursos normais): R$ {valor_acumulado_usado:.2f}")
            print(f"Prêmio bruto total: R$ {premio_bruto:.2f}")
            print(f"Prêmio médio: R$ {premio_medio_loto:.2f}")
            print("-" * 60)
            print(" Prêmios Por Ganhador: ")
            print("-" * 60)

                # Ganhadores dos Prêmios Principais
            print(f" Prêmios Principais (15 e 14 acertos): ( {premio_principal} ganhadores )")
            if premio_principal > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_principal_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_principal:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_principal_liquido:.2f}")

                # Ganhadores da Premiação FIxa
            print(f" \nPremiação Fixa (11, 12, 13 acertos): ( {premiacao_fixa} ganhadores )")
            if premiacao_fixa > 0:
                print(f" Valor bruto (individual): R$ {ganhadores_fixa_bruto:.2f}")
                print(f" Imposto de Renda (individual): R$ {imposto_R_fixa:.2f}")
                print(f" Valor líquido (individual): R$ {ganhadores_fixa_liquido:.2f}")


                # Distribuição para os Fundos
            print("-" * 60)
            print(" Destinação Para os Fundos: ")
            print("-" * 60)
            print(f" Seguridade Social: R$ {seguridade:.2f}")
            print(f" Fundo Nacional de Cultura: R$ {fnc:.2f}")
            print(f" Comitê Olímpico e Paralímpico: R$ {olimpico:.2f}")
            print(f" Fundo Penitenciário Nacional: R$ {funpen:.2f}")
            print(f" Fundo Nacional de Segurança Pública: R$ {fnsp:.2f}")
            print(f" Custos Operacionais (CAIXA): R$ {caixa:.2f}")
            print(f" Outros Encargos e Taxas Legais: R$ {outros:.2f}")
            print("=" * 60)


    elif tipo == 3:

        print("=" * 120)
        print("{:^120}".format("Estatisticas Gerais"))
        print("=" * 120)

        # Verificar se teve algum jogo registrado
        total_jogos = total_arrecadado_mega + total_liquido_quina + total_liquido_loto

        if total_jogos == 0:
             print("O Sistema não possui dados para formular as Estatisticas Gerais..")

        else:

            # Verificando qual a loteria mais rentavel para o jogador
            mais_rentavel_jogador = total_liquido_mega
            loteria_rentavel_jogador = "Mega-Sena"

            if total_liquido_quina > mais_rentavel_jogador:
                mais_rentavel_jogador, loteria_rentavel_jogador = total_liquido_quina, "Quina"
            if total_liquido_loto > mais_rentavel_jogador:
                mais_rentavel_jogador, loteria_rentavel_jogador = total_liquido_loto, "Lotofácil"

            # Verificando qual a loteria mais rentavel para a Caixa
            mais_rentavel_caixa = total_CAIXA_mega
            loteria_rentavel_caixa = "Mega-sena"

            if total_CAIXA_quina > mais_rentavel_caixa:
                mais_rentavel_caixa = total_CAIXA_quina
                loteria_rentavel_caixa = "Quina"

            if total_CAIXA_loto > mais_rentavel_caixa:
                mais_rentavel_caixa = total_CAIXA_loto
                loteria_rentavel_caixa = "Lotofácil"

            # Verificando qual a loteria mais rentavel para cada fundo

            # Seguridade social
            maior_seg = total_Seg_mega
            loteria_maior_seg = "Mega-Sena"

            if total_Seg_quina > maior_seg:
                maior_seg, loteria_maior_seg = total_Seg_quina, "Quina"
            if total_Seg_loto > maior_seg:
                maior_seg, loteria_maior_seg = total_Seg_loto, "Lotofácil"

            # Fundo Nacional de Cultura
            maior_fnc = total_fnc_mega
            loteria_maior_fnc = "Mega-Sena"

            if total_fnc_quina > maior_fnc:
                maior_fnc, loteria_maior_fnc = total_fnc_quina, "Quina"
            if total_fnc_loto > maior_fnc:
                maior_fnc, loteria_maior_fnc = total_fnc_loto, "Lotofácil"
            
            # Comitê Olimpico e Paralimpico
            maior_cop = total_COP_mega
            loteria_maior_COP = "Mega-Sena"

            if total_COP_quina > maior_cop:
                maior_cop, loteria_maior_COP = total_COP_quina, "Quina"
            if total_COP_loto > maior_cop:
                maior_cop, loteria_maior_COP = total_COP_loto, "Lotofácil"

            # Fundo Penitenciario Nacional
            maior_FUNPEN = total_FUNPEN_mega
            loteria_maior_FUNPEN = "Mega-Sena"

            if total_FUNPEN_quina > maior_FUNPEN:
                maior_FUNPEN, loteria_maior_FUNPEN = total_FUNPEN_quina, "Quina"
            if total_FUNPEN_loto > maior_FUNPEN:
                maior_FUNPEN, loteria_maior_FUNPEN = total_FUNPEN_loto, "Lotofácil"

            # Fundo Nacional de Segurança Pública
            maior_FNSP = total_FNSP_mega
            loteria_maior_FNSP = "Mega-Sena"

            if total_FNSP_quina > maior_FNSP:
                maior_FNSP, loteria_maior_FNSP = total_FNSP_quina, "Quina"
            if total_FNSP_loto > maior_FNSP:
                maior_FNSP, loteria_maior_FNSP = total_FNSP_loto, "Lotofácil"

            # Outros Encargos e Taxas Legais
            maior_outros = outros_mega
            loteria_maior_outros = "Mega-Sena"

            if outros_quina > maior_outros:
                maior_outros, loteria_maior_outros = outros_quina, "Quina"
            if outros_loto > maior_outros:
                maior_outros, loteria_maior_outros = outros_loto, "Lotofácil"
            
            # Exibição das Estatisticas Gerais
            print(f"Mais rentável para os Jogadores: {loteria_rentavel_jogador} (R$ {mais_rentavel_jogador:.2f})")
            print(f"Mais rentável para a Caixa: {loteria_rentavel_caixa} (R$ {mais_rentavel_caixa:.2f})")
            print(f"Mais rentável para a Seguridade Social: {loteria_maior_seg} (R$ {maior_seg:.2f})")
            print(f"Mais rentável para o FNC: {loteria_maior_fnc} (R$ {maior_fnc:.2f})")
            print(f"Mais rentável para o COP: {loteria_maior_COP} (R$ {maior_cop:.2f})")
            print(f"Mais rentável para o FUNPEN: {loteria_maior_FUNPEN} (R$ {maior_FUNPEN:.2f})")
            print(f"Mais rentável para o FNSP: {loteria_maior_FNSP} (R$ {maior_FNSP:.2f})")
            print(f"Mais rentável para Outros Encargos e Taxas Legais: {loteria_maior_outros} (R$ {maior_outros:.2f})")


    elif tipo == 4:  # Critérios de Distribuição
        print("=" * 120)
        print("{:^120}".format("CRITÉRIOS DE DISTRIBUIÇÃO"))
        print("=" * 120)
        print(" [ 1 ] Mega-Sena\n [ 2 ] Quina\n [ 3 ] Lotofácil\n ")
        distribuicao = (input("Digite sua opção: "))

        while not distribuicao.isdigit() or int(distribuicao) < 1 or int(distribuicao) > 3: # Verificação de Entrada Válida
            print("Não existe essa opção...")
            distribuicao = input("Digite sua opção: ")

        distribuicao = int(distribuicao)
    
        if distribuicao == 1:
            print("=" * 60)
            print("{:^60}".format("CRITÉRIOS - MEGA-SENA"))
            print("=" * 60)
            print("-" * 60)
            print("{:^60}".format("Prêmio Bruto: 46% da arrecadação"))
            print("-" * 60)
            print("Sena (6 acertos): 35% do prêmio bruto")
            print("Quina (5 acertos): 19% do prêmio bruto")
            print("Quadra (4 acertos): 19% do prêmio bruto")
            print("Acumula para concursos finais 0 ou 5: 22% do prêmio bruto")
            print("Mega da Virada: 5% do prêmio bruto\n")
            print("-" * 60)
            print("{:^60}".format("FUNDOS"))
            print("-" * 60)
            print("Seguridade Social: 17,32%")
            print("FNC: 3%")
            print("Comitê Olímpico e Paralímpico: 1,7%")
            print("FUNPEN: 3,14%")
            print("FNSP: 9,26%")
            print("CAIXA: 9,57%")
            print("Outros: 10,01%")
        
        if distribuicao == 2:
            print("=" * 60)
            print("{:^60}".format("CRITÉRIOS - QUINA"))
            print("=" * 60)
            print("-" * 60)
            print("{:^60}".format("Prêmio Bruto: 50% da arrecadação"))
            print("-" * 60)
            print("Quina (5 acertos): 35% do prêmio bruto")
            print("Quadra (4 acertos): 15% do prêmio bruto")
            print("Terno (3 acertos): 10% do prêmio bruto")
            print("Quina de São João: 15% do prêmio bruto")
            print("Acumula para concursos finais 5: 15% do prêmio bruto")
            print("Acumulo para próximo concurso: 10% do prêmio bruto\n")
            print("-" * 60)
            print("{:^60}".format("FUNDOS"))
            print("-" * 60)
            print("Seguridade Social: 17,32%")
            print("FNC: 3%")
            print("Comitê Olímpico e Paralímpico: 1,7%")
            print("FUNPEN: 3,14%")
            print("FNSP: 9,26%")
            print("CAIXA: 9,57%")
            print("Outros: 6,01%")
        
        if distribuicao == 3:
            print("=" * 60)
            print("{:^60}".format("CRITÉRIOS - LOTOFÁCIL"))
            print("=" * 60)
            print("-" * 60)
            print("{:^60}".format("Prêmio Bruto: 43,35% da arrecadação"))
            print("-" * 60)
            print("Prêmios principais (15 e 14 acertos): 62% do prêmio bruto")
            print("Lotofácil da Independência: 13% do prêmio bruto")
            print("Acumulo para final 0: 10% do prêmio bruto")
            print("Premiação fixa (11, 12, 13): 15% do prêmio bruto\n")
            print("-" * 60)
            print("{:^60}".format("FUNDOS"))
            print("-" * 60)
            print("Seguridade Social: 17,32%")
            print("FNC: 3%")
            print("Comitê Olímpico e Paralímpico: 1,7%")
            print("FUNPEN: 3,14%")
            print("FNSP: 9,26%")
            print("CAIXA: 9,57%")
            print("Outros: 12,66%")
        

    elif tipo == 5:
         print("Desligando os sistemas...")