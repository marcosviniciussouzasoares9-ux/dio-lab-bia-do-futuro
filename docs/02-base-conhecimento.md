# Base de Conhecimento
# Prompts do Agente
> [!TIP]
>**Prompt Sugerido para esta etapa:**
>```
>Crie um system prompt para um agente chamado “FinBot”, um educador financeiro. Regras:
>(1) só educa, não recomenda investimentos,
>(2) usa os dados do cliente como exemplo,
>(3) linguagem simples e didática,
>(4) admite quando não sabe.
>Inclua 3 exemplos de interação e 2 edge cases.
>[cole o template 03-prompts.md]

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve no FinBot ? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, dar continuidade ao atendimento de forma mais eficiente. |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e necessidades do aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser ensinados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didática. |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram utilizados como base, com pequenas adaptações para melhorar a análise:

Padronização de categorias de gastos (ex: alimentação, transporte, lazer)
Organização das datas para facilitar análise temporal
Inclusão de campos adicionais, como tipo de transação (entrada/saída)
Estruturação dos dados para facilitar leitura via Python (pandas e json)

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.
O agente FinBot acessa a base de dados diretamente por meio de arquivos locais no formato CSV e JSON, armazenados na pasta data/.

No início da execução da aplicação, esses arquivos são carregados utilizando Python:

A biblioteca pandas é utilizada para ler os arquivos CSV, como o histórico de transações
A biblioteca json é utilizada para carregar os arquivos JSON, como perfil do investidor e produtos financeiros

Após o carregamento, os dados ficam armazenados em memória e são acessados pelo sistema sempre que necessário.

Durante a interação com o usuário, o agente consulta esses dados de forma dinâmica para:

Analisar padrões de gastos
Identificar comportamentos financeiros
Gerar respostas personalizadas

Dessa forma, o FinBot consegue fornecer respostas mais precisas, contextualizadas e baseadas em dados reais, evitando informações genéricas ou imprecisas.

```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados podem ser inseridos diretamente no prompt para fornecer contexto ao agente. No entanto, em soluções mais robustas, o ideal é que esses dados sejam carregados dinamicamente, permitindo maior flexibilidade e eficiência no uso das informações.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANZAÇÕES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

HISTORICO DE ATENDIMENTO DO CLIENTE:


PRODUTOS DISPONIVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.
O exemplo de contexto montado é baseado nos dados originais da base de conhecimento, porém esses dados são sintetizados, mantendo apenas as informações mais relevantes. Isso é feito para otimizar o consumo de tokens e tornar o processamento mais eficiente. No entanto, é importante destacar que, mais importante do que economizar tokens, é garantir que todas as informações relevantes estejam presentes no contexto, pois isso impacta diretamente na qualidade das respostas do agente.
```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000)

RESUMO DE GASTOS:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
- Fundo de Ações (risco alto)
```
