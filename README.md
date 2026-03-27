# Análise de Estruturas de Dados

Geração de gráficos de barras para comparar o desempenho de diferentes estruturas de dados (hashtable, lista e lista ligada) em relação a tempo de execução, uso de memória e consumo de energia da CPU.

## Estruturas analisadas

- **Hashtable**
- **Lista**
- **Lista Ligada**

## Métricas

- **Tempo de execução** — duração de cada operação em segundos
- **Uso de memória** — memória máxima utilizada em MB
- **Consumo de energia da CPU** — convertido de microjoules para Watts, dividido em:
  - Package CPU (consumo total do processador)
  - Core CPU (consumo dos núcleos)
  - DRAM (consumo da memória RAM)

## Requisitos

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)

## Instalação

### 1. Instalar o uv

```bash
pip install uv
```

### 2. Criar o ambiente virtual e instalar dependências

```bash
uv sync
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

## Uso
Execute esse comando:

```bash
uv run main.py
```

## Observações
> Os valores de energia nos CSVs estão em **microjoules**. O script converte para **Watts** usando `watts = (microjoules / 1_000_000) / duration`.