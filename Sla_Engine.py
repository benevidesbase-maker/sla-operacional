import pandas as pd

# =================================================
# CONFIGURAÇÕES GERAIS
# =================================================
META_SLA = 0.96


# =================================================
# VALIDAÇÕES
# =================================================
def validar_sla(df: pd.DataFrame):
    """
    Valida se o arquivo de SLA possui as colunas mínimas
    necessárias para o cálculo.
    """
    colunas_obrigatorias = {
        "Nome da base de entrega",
        "Qtd a entregar",
        "未签收-客户问题件",
        "未签收-其他问题件",
    }

    faltantes = colunas_obrigatorias - set(df.columns)
    if faltantes:
        raise ValueError(f"Colunas ausentes no SLA: {faltantes}")

    # A coluna O (índice 14) precisa existir
    if df.shape[1] < 15:
        raise ValueError(
            "O SLA não possui a coluna O (Qtd Entregues no prazo)"
        )


# =================================================
# MOTOR DE CÁLCULO SLA
# =================================================
def calcular_sla(df_sla: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula métricas de SLA de forma neutra,
    sem qualquer regra organizacional.
    """
    validar_sla(df_sla)

    df = df_sla.copy()

    # -----------------------------
    # Conversões numéricas
    # -----------------------------
    df["Qtd a entregar"] = (
        pd.to_numeric(df["Qtd a entregar"], errors="coerce")
        .fillna(0)
        .astype(int)
    )

    df["Qtd Entregues no prazo"] = (
        pd.to_numeric(df.iloc[:, 14], errors="coerce")
        .fillna(0)
        .astype(int)
    )

    # -----------------------------
    # Pacotes problemáticos
    # -----------------------------
    df["Pacotes Problematicos"] = (
        pd.to_numeric(df["未签收-客户问题件"], errors="coerce").fillna(0)
        + pd.to_numeric(df["未签收-其他问题件"], errors="coerce").fillna(0)
    ).astype(int)

    # -----------------------------
    # SLA (%)
    # -----------------------------
    df["SLA (%)"] = (
        (df["Qtd Entregues no prazo"] / df["Qtd a entregar"])
        .replace([float("inf"), -float("inf")], 0)
        .fillna(0)
        * 100
    ).round(2)

    # -----------------------------
    # Faltantes para meta
    # -----------------------------
    necessario = df["Qtd a entregar"] * META_SLA
    df["Qtd de pacotes faltantes para 96%"] = (
        necessario - df["Qtd Entregues no prazo"]
    ).apply(lambda x: max(0, int(round(x))))

    # -----------------------------
    # Status SLA
    # -----------------------------
    df["Status SLA"] = pd.cut(
        df["SLA (%)"],
        bins=[-1, 93, 96, float("inf")],
        labels=["🔴 Crítico", "🟡 Atenção", "🟢 SLA Batido"],
    )

    return df


# =================================================
# RESUMO (KPIs)
# =================================================
def gerar_resumo(df: pd.DataFrame) -> dict:
    """
    Gera resumo agregado do SLA.
    """
    if df.empty:
        return {
            "Total a entregar": 0,
            "Entregues no prazo": 0,
            "Pacotes problemáticos": 0,
            "SLA Geral (%)": 0,
        }

    return {
        "Total a entregar": int(df["Qtd a entregar"].sum()),
        "Entregues no prazo": int(df["Qtd Entregues no prazo"].sum()),
        "Pacotes problemáticos": int(df["Pacotes Problematicos"].sum()),
        "SLA Geral (%)": round(df["SLA (%)"].mean(), 2),
    }
