# -*- coding: utf-8 -*-
"""
Solução Computacional Simples - Consultor de Biotipo Fabrispuma
Empresa: Fabrispuma (Lojas de Colchões e Móveis)
Objetivo: Automatizar e orientar a escolha de colchões de espuma com base na tabela do INER.

Requisitos atendidos (Etapa 6):
- Variáveis: armazenamento e manipulação de dados de entrada e saída.
- Estruturas Condicionais (if, elif, else): lógica de classificação de biotipos e menus.
- Estruturas de Repetição (while): controle do menu principal e validação de dados de entrada.
- Funções Simples: modularização e reutilização de blocos lógicos.
- Código Comentado: explicações didáticas em todo o código.
"""

def obter_densidade_iner(peso: float, altura: float) -> str:
    """
    Função Simples que implementa a tabela oficial de biotipo do INER (Instituto
    Nacional de Estudos do Repouso).
    Recebe o peso (kg) e a altura (m) e retorna a densidade recomendada.
    Utiliza estruturas condicionais encadeadas para classificar a densidade correta.
    """
    # Condicional 1: Avalia se a altura está na faixa de até 1.50m
    if altura <= 1.50:
        if peso <= 50.0:
            return "D23"
        elif peso <= 60.0:
            return "D26"
        elif peso <= 70.0:
            return "D28"
        else:
            # Para pesos elevados em alturas baixas, a tabela recomenda cuidado e auxílio extra
            return "D33 ou superior (Recomenda-se avaliação médica/técnica)"

    # Condicional 2: Avalia se a altura está na faixa de 1.51m a 1.60m
    elif altura <= 1.60:
        if peso <= 50.0:
            return "D23"
        elif peso <= 60.0:
            return "D26"
        elif peso <= 70.0:
            return "D28"
        elif peso <= 80.0:
            return "D33"
        else:
            return "D40 ou superior (Recomenda-se avaliação médica/técnica)"

    # Condicional 3: Avalia se a altura está na faixa de 1.61m a 1.70m
    elif altura <= 1.70:
        if peso <= 50.0:
            return "D23"
        elif peso <= 60.0:
            return "D26"
        elif peso <= 70.0:
            return "D28"
        elif peso <= 90.0:
            return "D33"
        elif peso <= 100.0:
            return "D40"
        elif peso <= 120.0:
            return "D45"
        else:
            return "D45 ou superior (Recomenda-se avaliação técnica)"

    # Condicional 4: Avalia se a altura está na faixa de 1.71m a 1.80m
    elif altura <= 1.80:
        if peso <= 50.0:
            return "D20"
        elif peso <= 60.0:
            return "D23"
        elif peso <= 70.0:
            return "D28"
        elif peso <= 90.0:
            return "D33"
        elif peso <= 120.0:
            return "D40"
        elif peso <= 150.0:
            return "D45"
        else:
            return "D45 ou superior (Recomenda-se avaliação técnica)"

    # Condicional 5: Avalia se a altura está na faixa de 1.81m a 1.90m
    elif altura <= 1.90:
        if peso <= 60.0:
            return "D26"
        elif peso <= 70.0:
            return "D26"
        elif peso <= 80.0:
            return "D28"
        elif peso <= 100.0:
            return "D33"
        elif peso <= 120.0:
            return "D40"
        elif peso <= 150.0:
            return "D45"
        else:
            return "D45 ou superior (Recomenda-se avaliação técnica)"

    # Condicional 6: Para alturas acima de 1.90m (>= 1.91m)
    else:
        if peso <= 90.0:
            return "D28"
        elif peso <= 100.0:
            return "D33"
        elif peso <= 150.0:
            return "D40"
        else:
            return "D45 ou superior (Recomenda-se avaliação médica/técnica)"


def obter_numero_positivo(mensagem: str) -> float:
    """
    Função Simples que solicita um número ao usuário e garante sua validação.
    Utiliza estrutura de repetição (while) e controle de erro (try/except)
    para impedir valores nulos, negativos ou caracteres não numéricos.
    """
    while True: # Estrutura de repetição infinita até obter uma entrada válida
        try:
            # Recebe o input do usuário, substituindo vírgula por ponto decimal se necessário
            valor_texto = input(mensagem).replace(',', '.')
            valor = float(valor_texto) # Tenta converter a string para número real (float)
            
            if valor > 0:
                return valor # Retorna o valor caso seja positivo, quebrando o loop
            else:
                print("Erro: O valor deve ser um número maior que zero. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número numérico válido.")


def exibir_cabecalho(titulo: str):
    """
    Função Simples para formatação de interface no terminal.
    Imprime linhas decorativas e centraliza o título.
    """
    largura = 65
    print("\n" + "=" * largura)
    print(f" {titulo} ".center(largura, " "))
    print("=" * largura)


def calcular_individual():
    """
    Função Simples que coordena o fluxo de consulta para um único cliente.
    Cria variáveis para armazenar nome, peso, altura e resultado.
    """
    exibir_cabecalho("CONSULTA INDIVIDUAL DE BIOTIPO")
    
    # Uso de Variáveis para receber dados
    nome_cliente = input("Nome do Cliente: ").strip()
    peso_cliente = obter_numero_positivo("Digite o peso do cliente (kg): ")
    altura_cliente = obter_numero_positivo("Digite a altura do cliente (metros, ex: 1.75): ")
    
    # Chama a função de cálculo e armazena o resultado em uma variável
    densidade_recomendada = obter_densidade_iner(peso_cliente, altura_cliente)
    
    # Exibição estruturada do resultado
    print("\n" + "-" * 50)
    print(f"Resultado da Consulta para: {nome_cliente if nome_cliente else 'Cliente Especial'}")
    print(f"- Peso: {peso_cliente:.2f} kg")
    print(f"- Altura: {altura_cliente:.2f} m")
    print(f"--> DENSIDADE RECOMENDADA (Tabela INER): {densidade_recomendada}")
    print("-" * 50)
    print("Dica Fabrispuma: Escolher a densidade correta previne deformações precoces\n"
          "no colchão de espuma e garante a saúde da coluna vertebral.")


def calcular_casal():
    """
    Função Simples para consulta de casais.
    Aplica a regra de ouro do INER: no caso de casal, escolhe-se o colchão
    pela pessoa de maior peso para que a sustentação seja adequada a ambos.
    Diferenças de peso acentuadas (> 30kg) disparam alertas comerciais de molas ensacadas.
    """
    exibir_cabecalho("CONSULTA DE BIOTIPO PARA CASAL")
    
    # Uso de Variáveis para o primeiro cônjuge
    nome1 = input("Nome do Primeiro Cônjuge: ").strip()
    peso1 = obter_numero_positivo(f"Digite o peso de {nome1 if nome1 else 'Cônjuge 1'} (kg): ")
    altura1 = obter_numero_positivo(f"Digite a altura de {nome1 if nome1 else 'Cônjuge 1'} (metros): ")
    
    # Uso de Variáveis para o segundo cônjuge
    nome2 = input("Nome do Segundo Cônjuge: ").strip()
    peso2 = obter_numero_positivo(f"Digite o peso de {nome2 if nome2 else 'Cônjuge 2'} (kg): ")
    altura2 = obter_numero_positivo(f"Digite a altura de {nome2 if nome2 else 'Cônjuge 2'} (metros): ")
    
    # Calcula as densidades ideais individuais
    densidade1 = obter_densidade_iner(peso1, altura1)
    densidade2 = obter_densidade_iner(peso2, altura2)
    
    # Função interna auxiliar para extrair o peso ou a representação numérica da densidade
    # para sabermos qual delas é a mais alta
    def extrair_peso_densidade(densidade_str: str) -> int:
        for termo in ["D", " ou superior (Recomenda-se avaliação médica/técnica)", " ou superior", " ou superior (Recomenda-se avaliação técnica)"]:
            densidade_str = densidade_str.replace(termo, "")
        try:
            return int(densidade_str.strip())
        except ValueError:
            return 99 # Indica a maior categoria se houver inconsistência
            
    num_densidade1 = extrair_peso_densidade(densidade1)
    num_densidade2 = extrair_peso_densidade(densidade2)
    
    # Uso de Estrutura Condicional para decidir qual biotipo guiará a escolha
    if num_densidade1 >= num_densidade2:
        densidade_casal = densidade1
        parceiro_referencia = nome1 if nome1 else "Cônjuge 1"
    else:
        densidade_casal = densidade2
        parceiro_referencia = nome2 if nome2 else "Cônjuge 2"
        
    # Exibe resultados detalhados
    print("\n" + "-" * 55)
    print("Resultado da Consulta de Casal:")
    print(f"- {nome1 if nome1 else 'Cônjuge 1'}: {peso1:.1f}kg e {altura1:.2f}m -> Individual: {densidade1}")
    print(f"- {nome2 if nome2 else 'Cônjuge 2'}: {peso2:.1f}kg e {altura2:.2f}m -> Individual: {densidade2}")
    print(f"\n=> DENSIDADE RECOMENDADA PARA O CASAL: {densidade_casal}")
    print(f"   (Calculado com base no biotipo de {parceiro_referencia})")
    print("-" * 55)
    
    # Alerta inteligente da Fabrispuma sobre diferença de peso acentuada
    diferenca_peso = abs(peso1 - peso2)
    if diferenca_peso > 30.0:
        print("\n[!] ALERTA DE ATENDIMENTO FABRISPUMA:")
        print(f"Detectamos uma diferença de peso significativa ({diferenca_peso:.1f} kg) entre o casal.")
        print("Para evitar a transferência de movimento (quando um se move na cama e incomoda o outro)")
        print("e assegurar a durabilidade, recomendamos considerar colchões de MOLAS ENSACADAS (Pocket).")


def calcular_infantil():
    """
    Função Simples para orientação de colchões para recém-nascidos e bebês.
    Garante a recomendação regulamentar de D18 para crianças até 3 anos.
    """
    exibir_cabecalho("CONSULTA INFANTIL (BEBÊS E CRIANÇAS)")
    
    nome_crianca = input("Nome da Criança: ").strip()
    idade_crianca = obter_numero_positivo("Digite a idade da criança (em anos, ex: 1.5): ")
    
    # Estrutura condicional para validar a faixa etária da recomendação D18
    if idade_crianca <= 3.0:
        print("\n" + "-" * 50)
        print(f"Resultado para {nome_crianca if nome_crianca else 'Bebê'}:")
        print(f"- Idade: {idade_crianca:.1f} ano(s) (Até 3 anos)")
        print("--> DENSIDADE RECOMENDADA: D18 (Padrão INER)")
        print("-" * 50)
        print("Observação: A espuma D18 é especificamente recomendada para a fase de crescimento")
        print("de bebês até 3 anos, protegendo a coluna sensível contra excesso de rigidez.")
    else:
        print("\n[!] Aviso: Para crianças acima de 3 anos, o biotipo começa a se aproximar")
        print("do padrão adulto. Utilize a opção de 'Consulta Individual' informando o peso e altura reais.")


def main():
    """
    Função Principal que executa o fluxo do programa.
    Utiliza estrutura de repetição (while) para controlar a permanência no menu principal
    e estruturas condicionais (if, elif, else) para executar a opção selecionada.
    """
    # Loop de Repetição Principal do Sistema
    while True:
        exibir_cabecalho("CONSULTOR DIGITAL DE COLCHÕES - FABRISPUMA")
        print("1. Consultar Densidade de Espuma Individual")
        print("2. Consultar Densidade de Espuma para Casal")
        print("3. Consultar Densidade para Crianças (Bebês até 3 anos)")
        print("4. Sair do Programa")
        print("=" * 65)
        
        # Variável para capturar a escolha do usuário no menu
        opcao = input("Selecione uma opção (1-4): ").strip()
        
        # Estrutura Condicional para direcionar o fluxo de acordo com a opção
        if opcao == "1":
            calcular_individual()
        elif opcao == "2":
            calcular_casal()
        elif opcao == "3":
            calcular_infantil()
        elif opcao == "4":
            print("\nObrigado por utilizar o Consultor Digital Fabrispuma. Bons sonhos!")
            break # Encerra o loop while e fecha o programa
        else:
            print("\nErro: Opção inválida! Digite um número de 1 a 4.")
            
        # Pausa para que o usuário possa ler o resultado antes de limpar ou retornar ao menu
        input("\nPressione [Enter] para voltar ao menu principal...")


# Executa o programa apenas se ele for rodado diretamente (não importado)
if __name__ == "__main__":
    main()
