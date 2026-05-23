# Consultor Digital de Biotipo - Fabrispuma

Este projeto apresenta a formulação de um problema prático de negócios e sua respectiva solução computacional simples em Python para a rede varejista **Fabrispuma**, atendendo a todas as diretrizes pedagógicas para entrega acadêmica/prática (**Etapa 6 - Solução computacional simples**).

---

## 1. Contextualização do Problema

### A Organização: Fabrispuma
A **Fabrispuma** é uma das maiores redes de varejo de colchões e móveis do interior de São Paulo, com mais de 100 lojas físicas e operação de e-commerce nacional. Seu principal segmento é a comercialização de colchões de marcas premium nacionais e importadas.

### O Problema de Negócio
No comércio de colchões de espuma, a escolha do produto adequado não é apenas estética ou de preferência subjetiva: é uma questão de saúde e durabilidade. O **INER (Instituto Nacional de Estudos do Repouso)** estabelece a **Tabela de Biotipo**, relacionando peso e altura para determinar a **Densidade (D)** ideal de espuma. 
- Um colchão com densidade menor que a recomendada sofre deformação precoce (efeito "canoa") e prejudica o alinhamento da coluna do cliente, levando a devoluções de produto por defeito aparente e reclamações na garantia.
- Um colchão excessivamente firme pode causar desconforto e pontos de pressão no corpo.
- No caso de **casais**, a complexidade aumenta: a densidade deve ser baseada na pessoa mais pesada, mas se a diferença for muito grande (ex: superior a 30kg), a espuma comum pode não ser a melhor indicação, recomendando-se colchões de molas ensacadas (Pocket) que isolam o movimento.

### Necessidade Prática da Empresa
Os vendedores precisam de uma ferramenta ágil no terminal de vendas que:
1. Colete o perfil do cliente (e do cônjuge, se houver).
2. Calcule instantaneamente a densidade adequada do INER.
3. Avise os vendedores sobre oportunidades comerciais específicas (como indicar colchões de molas ensacadas para casais com grande discrepância de peso).

---

## 2. O Algoritmo

O algoritmo para a resolução deste problema segue a lógica descrita abaixo:

### Representação do Fluxo (Pseudocódigo)
```text
Algoritmo ConsultorBiotipoFabrispuma
Iniciar loop principal
    Exibir Menu Principal:
        1. Consulta Individual
        2. Consulta de Casal
        3. Consulta Infantil (0 a 3 anos)
        4. Sair
    Receber escolha_menu do usuário
    
    Se escolha_menu for 1:
        Obter e validar peso_cliente e altura_cliente
        Chamar função obter_densidade_iner(peso, altura)
        Exibir a densidade recomendada e orientações pós-venda
    
    Senão, se escolha_menu for 2:
        Obter e validar peso_conjuge1, altura_conjuge1
        Obter e validar peso_conjuge2, altura_conjuge2
        Calcular densidades individuais para ambos
        Definir densidade final do casal baseando-se no biotipo de maior suporte
        Calcular a diferença de peso entre os dois
        Se diferenca_peso > 30 kg:
            Exibir alerta sugerindo colchões de Molas Ensacadas (Pocket)
        Exibir densidade recomendada para o colchão de espuma do casal
        
    Senão, se escolha_menu for 3:
        Obter e validar idade_crianca
        Se idade_crianca <= 3 anos:
            Exibir recomendação de densidade padrão D18
        Senão:
            Orientar para usar a Consulta Individual (biotipo padrão)
            
    Senão, se escolha_menu for 4:
        Exibir mensagem de encerramento
        Parar o loop principal
    
    Senão:
        Exibir mensagem de opção inválida
Fim do loop
Fim do Algoritmo
```

---

## 3. Estrutura do Código e Recursos Python Utilizados

O script [`solucao_computacional.py`](file:///C:/Users/sampaa/.gemini/antigravity/scratch/fabrispuma_mattress_advisor/solucao_computacional.py) foi construído utilizando apenas os recursos nativos do Python solicitados na Etapa 6, sem dependências externas:

1. **Variáveis**:
   - Usadas para armazenar informações textuais (`nome_cliente`, `opcao`, `densidade_casal`) e numéricas reais (`peso`, `altura`, `diferenca_peso`, `idade_crianca`).
2. **Estruturas Condicionais (`if`, `elif`, `else`)**:
   - Utilizadas no menu para direcionar para a opção desejada.
   - Utilizadas na função `obter_densidade_iner` para classificar as faixas de biotipo da tabela INER de forma rigorosa.
   - Utilizadas para verificar se a idade da criança é de até 3 anos.
   - Utilizadas para avaliar se a diferença de peso do casal exige a recomendação de molas ensacadas.
3. **Estruturas de Repetição (`while`)**:
   - O loop `while True` controla o menu principal do sistema, permitindo realizar infinitas consultas até que o operador selecione a opção "Sair" (que ativa o comando `break`).
   - Um loop `while True` interno na função `obter_numero_positivo` impede que o programa quebre ou trave caso o usuário digite um valor não numérico (com tratamento de exceção `try-except`).
4. **Funções Simples (`def`)**:
   - `obter_densidade_iner(peso, altura)`: Encapsula a lógica complexa da Tabela de Biotipo.
   - `obter_numero_positivo(mensagem)`: Garante que as entradas sejam números válidos.
   - `exibir_cabecalho(titulo)`: Padroniza a formatação visual do programa.
   - `calcular_individual()`, `calcular_casal()`, `calcular_infantil()`: Modularizam as regras específicas de cada cenário de venda.
   - `main()`: Orquestra o funcionamento do loop e do menu.

---

## 4. Como Executar o Script

Para executar a solução e testar as funcionalidades, utilize o terminal do seu sistema operacional (ou terminal do VS Code) no diretório onde o arquivo está salvo:

```powershell
python solucao_computacional.py
```

### Exemplos Práticos de Funcionamento (Entrada/Saída)

#### Caso A: Consulta Individual
- **Entradas**:
  - Nome: *Joana D'Arc*
  - Peso: *65 kg*
  - Altura: *1.68 m*
- **Saída Esperada**:
  ```text
  --------------------------------------------------
  Resultado da Consulta para: Joana D'Arc
  - Peso: 65.00 kg
  - Altura: 1.68 m
  --> DENSIDADE RECOMENDADA (Tabela INER): D28
  --------------------------------------------------
  ```

#### Caso B: Consulta de Casal com Diferença de Peso
- **Entradas**:
  - Cônjuge 1: *Carlos* | Peso: *62 kg* | Altura: *1.72 m* (Requer D28)
  - Cônjuge 2: *Roberto* | Peso: *98 kg* | Altura: *1.85 m* (Requer D33)
- **Saída Esperada**:
  ```text
  -------------------------------------------------------
  Resultado da Consulta de Casal:
  - Carlos: 62.0kg e 1.72m -> Individual: D28
  - Roberto: 98.0kg e 1.85m -> Individual: D33

  => DENSIDADE RECOMENDADA PARA O CASAL: D33
     (Calculado com base no biotipo de Roberto)
  -------------------------------------------------------

  [!] ALERTA DE ATENDIMENTO FABRISPUMA:
  Detectamos uma diferença de peso significativa (36.0 kg) entre o casal.
  Para evitar a transferência de movimento (quando um se move na cama e incomoda o outro)
  e assegurar a durabilidade, recomendamos considerar colchões de MOLAS ENSACADAS (Pocket).
  ```

#### Caso C: Consulta Infantil
- **Entradas**:
  - Nome da Criança: *Arthur*
  - Idade: *2 anos*
- **Saída Esperada**:
  ```text
  --------------------------------------------------
  Resultado para Arthur:
  - Idade: 2.0 ano(s) (Até 3 anos)
  --> DENSIDADE RECOMENDADA: D18 (Padrão INER)
  --------------------------------------------------
  ```
