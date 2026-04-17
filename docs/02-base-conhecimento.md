# Base de Conhecimento

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

Os dados não são inseridos diretamente no system prompt.

Em vez disso:

O sistema consulta os dados dinamicamente conforme a pergunta do usuário
Apenas as informações relevantes são enviadas para o modelo de linguagem
Isso evita sobrecarga de contexto e melhora a precisão das respostas

Exemplo:

Pergunta sobre gastos → usa transacoes.csv
Pergunta sobre investimentos → usa perfil_investidor.json + produtos_financeiros.json
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Conservador
- Saldo disponível: R$ 5.000

Resumo de Gastos:
- Alimentação: R$ 1.200
- Transporte: R$ 400
- Lazer: R$ 300

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Combustível - R$ 200
```
