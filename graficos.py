import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import shutil

OUTPUT_DIR = "maps"

def fazer_graficos_csv(dados:str):
    os.makedirs("./maps", exist_ok=True)

    df_energia = pd.read_csv(f"./data/{dados}_energia.csv", sep=";")
    df_tempo   = pd.read_csv(f"./data/{dados}_tempo_execucao.csv")
    df_mem     = pd.read_csv(f"./data/{dados}_memoria.csv")

    df_energia["package_watts"] = (df_energia["package_0"] / 1_000_000) / df_energia["duration"]
    df_energia["core_watts"]    = (df_energia["core_0"]    / 1_000_000) / df_energia["duration"]
    df_energia["dram_watts"]    = (df_energia["dram_0"]    / 1_000_000) / df_energia["duration"]

    tags = df_energia["tag"]
    x = range(len(tags))
    width = 0.25
    colors = ["#4C72B0", "#DD8452", "#55A868"]

    # ==================== GRÁFICO 1: ENERGIA CPU ====================
    fig, ax = plt.subplots(figsize=(8, 5))

    b1 = ax.bar([i - width for i in x], df_energia["package_watts"], width, label="Consumo Total em CPU (W)", color=colors[0])

    ax.set_title(f"Consumo de Energia da CPU por Operação (Watts) em {dados}", fontsize=14, fontweight="bold")
    ax.set_xlabel("Operação")
    ax.set_ylabel("Watts (W)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(tags, rotation=15, ha="right")
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.4f"))
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(f"{OUTPUT_DIR}/{dados}_energia.png", dpi=150)
    plt.close()

    # ==================== GRÁFICO 2: TEMPO DE EXECUÇÃO ====================
    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(df_tempo["nome"], df_tempo["tempo_de_execucao"], color=colors[:len(df_tempo)], width=0.5)
    ax.bar_label(bars, fmt="%.6f", padding=3, fontsize=9)

    ax.set_title(f"Tempo de Execução por Operação (segundos) em {dados}", fontsize=14, fontweight="bold")
    ax.set_xlabel("Operação")
    ax.set_ylabel("Tempo (s)")
    ax.legend(bars, df_tempo["nome"], title="Operações")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(f"{OUTPUT_DIR}/{dados}_tempo_execucao.png", dpi=150)
    plt.close()

    # ==================== GRÁFICO 3: MEMÓRIA ====================
    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(df_mem["nome"], df_mem["uso_maximo_memoria"], color=colors[:len(df_mem)], width=0.5)
    ax.bar_label(bars, fmt="%.2f MB", padding=3, fontsize=9)

    ax.set_title(f"Uso Máximo de Memória por Operação (MB) em {dados}", fontsize=14, fontweight="bold")
    ax.set_xlabel("Operação")
    ax.set_ylabel("Memória (MB)")
    ax.legend(bars, df_mem["nome"], title="Operações")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    fig.tight_layout()
    fig.savefig(f"{OUTPUT_DIR}/{dados}_memoria.png", dpi=150)
    plt.close()

    print(f"Gráficos de {dados} gerados em:", OUTPUT_DIR)