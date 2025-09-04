# Análise de Farms - Reino 3618

Dashboard web para análise do impacto das farms no Reino 3618 do Rise of Kingdoms.

## 📊 Visão Geral

Este projeto analisa os dados dos 310 governadores mais poderosos do Reino 3618 e identifica as farms, mostrando como elas impactam a distribuição de poder no reino.

### Critérios de Identificação de Farms
- CH = 25 (City Hall nível 25)
- Clickable = TRUE
- Aliança ≠ "Thousand Sunny br"

## 🚀 Como Usar

1. Abra o arquivo `index.html` em qualquer navegador moderno
2. O dashboard carrega automaticamente os dados de `dados_filtrados.json`
3. Visualize:
   - Estatísticas gerais em cards
   - Gráfico de pizza com distribuição de poder
   - Gráfico de barras comparativo
   - Top 10 farms por poder

## 📱 Recursos

- **Design Responsivo**: Otimizado para desktop, tablet e mobile
- **Visualizações Interativas**: Gráficos usando Chart.js
- **Dados Atualizados**: Baseados nos primeiros 310 governadores

## 📁 Estrutura do Projeto

```
├── index.html              # Dashboard principal
├── dados_filtrados.json    # Dados das farms identificadas
├── analise_reino.json      # Estatísticas gerais
├── filtro_planilha.py      # Script para filtrar farms
├── analisar_dados.py       # Script de análise de dados
└── README.md              # Este arquivo
```

## 🛠️ Scripts Python

### `filtro_planilha.py`
Filtra a planilha original identificando as farms baseado nos critérios definidos.

### `analisar_dados.py`
Gera as estatísticas e análises dos dados filtrados.

## 📈 Estatísticas Atuais

- **Poder Total (Top 310)**: 8.901.031.920
- **Poder das Farms**: 2.596.766.566 (29.17%)
- **Total de Farms**: 114

## 🌐 Tecnologias Utilizadas

- HTML5
- CSS3 (Tailwind CSS)
- JavaScript (Vanilla)
- Chart.js para visualizações
- Python para análise de dados

## 📄 Licença

Projeto de análise para fins educacionais e informativos.