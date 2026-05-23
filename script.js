// Controlar a navegação de abas (Tabs)
function switchTab(tabId) {
    // Esconder todas as abas
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remover a classe ativa de todos os botões
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Mostrar a aba correspondente e destacar o botão clicado
    document.getElementById(`tab-${tabId}`).classList.add('active');
    event.currentTarget.classList.add('active');
    
    // Ocultar resultados ao trocar de aba para evitar dados misturados
    closeResult();
}

// Controlar a exibição colapsável da tabela do INER
function toggleTable() {
    const tableBody = document.getElementById('table-body');
    const header = document.querySelector('.ref-header');
    
    if (tableBody.classList.contains('collapsed')) {
        tableBody.classList.remove('collapsed');
        header.classList.add('active');
    } else {
        tableBody.classList.add('collapsed');
        header.classList.remove('active');
    }
}

// Fechar caixa de resultados
function closeResult() {
    document.getElementById('result-container').classList.add('hidden');
}

// Lógica de cálculo de densidade do INER (idêntica ao script Python)
function obterDensidadeINER(peso, altura) {
    // Altura até 1.50m
    if (altura <= 1.50) {
        if (peso <= 50) return "D23";
        else if (peso <= 60) return "D26";
        else if (peso <= 70) return "D28";
        else return "D33 ou superior*";
    }
    // Altura 1.51m a 1.60m
    else if (altura <= 1.60) {
        if (peso <= 50) return "D23";
        else if (peso <= 60) return "D26";
        else if (peso <= 70) return "D28";
        else if (peso <= 80) return "D33";
        else return "D40 ou superior*";
    }
    // Altura 1.61m a 1.70m
    else if (altura <= 1.70) {
        if (peso <= 50) return "D23";
        else if (peso <= 60) return "D26";
        else if (peso <= 70) return "D28";
        else if (peso <= 90) return "D33";
        else if (peso <= 100) return "D40";
        else if (peso <= 120) return "D45";
        else return "D45 ou superior*";
    }
    // Altura 1.71m a 1.80m
    else if (altura <= 1.80) {
        if (peso <= 50) return "D20";
        else if (peso <= 60) return "D23";
        else if (peso <= 70) return "D28";
        else if (peso <= 90) return "D33";
        else if (peso <= 120) return "D40";
        else if (peso <= 150) return "D45";
        else return "D45 ou superior*";
    }
    // Altura 1.81m a 1.90m
    else if (altura <= 1.90) {
        if (peso <= 60) return "D26";
        else if (peso <= 70) return "D26";
        else if (peso <= 80) return "D28";
        else if (peso <= 100) return "D33";
        else if (peso <= 120) return "D40";
        else if (peso <= 150) return "D45";
        else return "D45 ou superior*";
    }
    // Altura acima de 1.90m (>= 1.91m)
    else {
        if (peso <= 90) return "D28";
        else if (peso <= 100) return "D33";
        else if (peso <= 150) return "D40";
        else return "D45 ou superior*";
    }
}

// Helper para converter string de densidade em número comparável (ex: "D33" -> 33)
function extrairValorDensidade(densidadeStr) {
    let clean = densidadeStr.replace("D", "").replace(" ou superior*", "").replace(" ou superior", "");
    let val = parseInt(clean);
    return isNaN(val) ? 99 : val;
}

// Injetar e exibir resultado no HTML
function showResult(density, summaryText, detailsHTML, alertConfig = null) {
    const resultBox = document.getElementById('result-container');
    const resultDensity = document.getElementById('result-density');
    const resultSummary = document.getElementById('result-summary');
    const resultDetails = document.getElementById('result-details-content');
    const alertPanel = document.getElementById('result-alert-panel');
    
    resultDensity.innerText = density;
    resultSummary.innerText = summaryText;
    resultDetails.innerHTML = detailsHTML;
    
    if (alertConfig) {
        alertPanel.classList.remove('hidden');
        document.getElementById('alert-title').innerText = alertConfig.title;
        document.getElementById('alert-text').innerText = alertConfig.text;
    } else {
        alertPanel.classList.add('hidden');
    }
    
    resultBox.classList.remove('hidden');
    
    // Rola a tela suavemente até a caixa de resultado
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Ação do formulário Individual
function calcularIndividual(e) {
    e.preventDefault();
    
    const nome = document.getElementById('ind-nome').value.trim();
    const peso = parseFloat(document.getElementById('ind-peso').value);
    const altura = parseFloat(document.getElementById('ind-altura').value);
    
    const densidade = obterDensidadeINER(peso, altura);
    const clienteNome = nome ? nome : "Cliente";
    
    const detailsHTML = `
        <div class="detail-item">
            <span class="detail-label">Nome do Cliente</span>
            <span class="detail-value">${clienteNome}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Peso Digitado</span>
            <span class="detail-value">${peso.toFixed(1)} kg</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Altura Digitada</span>
            <span class="detail-value">${altura.toFixed(2)} m</span>
        </div>
    `;
    
    const alertConfig = {
        title: "Dica de Consultoria Fabrispuma",
        text: "Escolher o colchão de densidade adequada mantém as vértebras em repouso na posição natural, prevenindo dores lombares e o desgaste precoce da espuma."
    };
    
    showResult(densidade, `Escolha ideal de biotipo calculada para ${clienteNome}.`, detailsHTML, alertConfig);
}

// Ação do formulário Casal
function calcularCasal(e) {
    e.preventDefault();
    
    const nome1 = document.getElementById('c1-nome').value.trim();
    const peso1 = parseFloat(document.getElementById('c1-peso').value);
    const altura1 = parseFloat(document.getElementById('c1-altura').value);
    
    const nome2 = document.getElementById('c2-nome').value.trim();
    const peso2 = parseFloat(document.getElementById('c2-peso').value);
    const altura2 = parseFloat(document.getElementById('c2-altura').value);
    
    const densidade1 = obterDensidadeINER(peso1, altura1);
    const densidade2 = obterDensidadeINER(peso2, altura2);
    
    const val1 = extrairValorDensidade(densidade1);
    const val2 = extrairValorDensidade(densidade2);
    
    let densidadeFinal = "";
    let parceiroReferencia = "";
    
    // Regra do INER: selecionar pela pessoa que necessita de mais sustentação (maior densidade)
    if (val1 >= val2) {
        densidadeFinal = densidade1;
        parceiroReferencia = nome1 ? nome1 : "Cônjuge 1";
    } else {
        densidadeFinal = densidade2;
        parceiroReferencia = nome2 ? nome2 : "Cônjuge 2";
    }
    
    const detailsHTML = `
        <div class="detail-item">
            <span class="detail-label">Biotipo ${nome1 ? nome1 : 'Cônjuge 1'} (${peso1.toFixed(0)}kg)</span>
            <span class="detail-value">${densidade1}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Biotipo ${nome2 ? nome2 : 'Cônjuge 2'} (${peso2.toFixed(0)}kg)</span>
            <span class="detail-value">${densidade2}</span>
        </div>
        <div class="detail-item" style="border-top: 1px solid rgba(255,255,255,0.08); margin-top: 5px; padding-top: 10px;">
            <span class="detail-label" style="color: var(--primary);">Parceiro Referência</span>
            <span class="detail-value" style="color: var(--primary);">${parceiroReferencia}</span>
        </div>
    `;
    
    const diferencaPeso = Math.abs(peso1 - peso2);
    let alertConfig = null;
    
    // Alerta de vendas consultivas
    if (diferencaPeso > 30) {
        alertConfig = {
            title: "Oportunidade Comercial - Molas Ensacadas",
            text: `Identificamos uma diferença de peso acentuada (${diferencaPeso.toFixed(0)} kg) entre o casal. Para evitar o efeito gangorra e o ruído de movimento, recomendamos sugerir colchões de MOLAS ENSACADAS (Pocket) em vez de espuma convencional.`
        };
    } else {
        alertConfig = {
            title: "Regra de Ouro do Varejo",
            text: "No caso de casal, orienta-se escolher o colchão pelo parceiro de maior biotipo para garantir que a sustentação da coluna de ambos seja ideal."
        };
    }
    
    showResult(densidadeFinal, "Densidade recomendada para o colchão de casal.", detailsHTML, alertConfig);
}

// Ação do formulário Infantil
function calcularInfantil(e) {
    e.preventDefault();
    
    const nome = document.getElementById('inf-nome').value.trim();
    const idade = parseFloat(document.getElementById('inf-idade').value);
    const criancaNome = nome ? nome : "a Criança";
    
    let densidade = "";
    let summary = "";
    let alertConfig = null;
    let detailsHTML = "";
    
    if (idade <= 3.0) {
        densidade = "D18";
        summary = `Densidade oficial recomendada para ${criancaNome}.`;
        detailsHTML = `
            <div class="detail-item">
                <span class="detail-label">Criança</span>
                <span class="detail-value">${criancaNome}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Idade</span>
                <span class="detail-value">${idade.toFixed(1)} ano(s) (Até 3 anos)</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Faixa Etária</span>
                <span class="detail-value">Bebê de Colo / Infantil</span>
            </div>
        `;
        alertConfig = {
            title: "Importância da espuma D18",
            text: "Para bebês até 3 anos, o INER preconiza a densidade D18. Ela fornece a firmeza calibrada para apoiar a estrutura óssea em desenvolvimento sem comprometer o conforto macio necessário para as articulações do bebê."
        };
    } else {
        densidade = "Individual";
        summary = "Para crianças maiores de 3 anos, utilize o cálculo padrão por Peso e Altura.";
        detailsHTML = `
            <div class="detail-item">
                <span class="detail-label">Criança</span>
                <span class="detail-value">${criancaNome}</span>
            </div>
            <div class="detail-item">
                <span class="detail-label">Idade</span>
                <span class="detail-value">${idade.toFixed(1)} anos (> 3 anos)</span>
            </div>
        `;
        alertConfig = {
            title: "Nota do Consultor",
            text: "Crianças com mais de 3 anos começam a ter curvas de biotipo semelhantes às adultas. Vá para a aba 'Consulta Individual' e informe peso e altura."
        };
    }
    
    showResult(densidade, summary, detailsHTML, alertConfig);
}
