# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

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

Os arquivos CSV e JSON são carregados no início da aplicação utilizando Python:

CSV: carregados com a biblioteca pandas
JSON: carregados com a biblioteca json

Esses dados ficam disponíveis em memória durante a execução e são utilizados conforme a necessidade das interações.

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
