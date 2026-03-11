# Caracterização de Grafos de Escala Livre com Dados de Redes de Comunicação

Projeto simples de grafos para a disciplina, focado em leitura de dados (emails da empresa Enron), construção do grafo e métricas básicas. Também inclui análise de lei de potência e características de escala livre.

## Como usar

### 1. Usando `uv`

1. Instale as dependências e sincronize o ambiente virtual:

```bash
uv sync
```

### 2. Sem `uv`

1. Crie e ative um ambiente virtual (opcional, mas recomendado).

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 3. Código

O código principal está no **notebook** `src/entrega_1.ipynb`. E nossas implementações em `src/simple_graph.py` e `src/bag.py`.

## Dados

- `src/data/Email-Enron.txt`: arquivo base do grafo. Fonte: [Link dos dados](https://snap.stanford.edu/data/email-Enron.html)

## EQUIPE:
- [@tiagostmg](https://github.com/tiagostmg)
- [@rcacau](https://github.com/rcacau)
- [@IgorPra](https://github.com/IgorPra)
