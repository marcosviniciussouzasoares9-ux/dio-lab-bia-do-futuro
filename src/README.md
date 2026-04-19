# Passo a Passo de execução

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama 

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull llama3.2:1b

# 3. Testar se funciona
ollama run llama3.2:1b "Olá!"
```

## Exemplo de requirements.txt

Todo o código fonte está no arquivo `app.py`.

## Como Rodar
```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py
```
##Evidências

<img width="1106" height="788" alt="image" src="https://github.com/user-attachments/assets/a8e1033f-62e5-420b-807e-4976b0535758" />

