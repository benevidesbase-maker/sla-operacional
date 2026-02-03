import pandas as pd

META_SLA = 0.96

# =================================================
# PROCV FIXO – RESPONSÁVEIS POR BASE
# =================================================
RESPONSAVEIS_BASE = pd.DataFrame([
    {"Nome da base de entrega": "F BAO-PA", "Sua cidade": "Baião", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "CLAUDIO ROBERTO PANTOJA DE LIMA JUNIOR"},
    {"Nome da base de entrega": "VCP -PA", "Sua cidade": "Cametá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "CLAUDIO ROBERTO PANTOJA DE LIMA JUNIOR"},
    {"Nome da base de entrega": "MCJ -PA", "Sua cidade": "Mocajuba", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "CLAUDIO ROBERTO PANTOJA DE LIMA JUNIOR"},
    {"Nome da base de entrega": "PA ANA", "Sua cidade": "Ananindeua", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "DARLEY WALLACE CUNHA QUARESMA"},
    {"Nome da base de entrega": "CNA -PA", "Sua cidade": "Canaã dos Carajás", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "CKS -PA", "Sua cidade": "Parauapebas", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F ORL-PA", "Sua cidade": "Ourilândia do Norte", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F SFX-PA", "Sua cidade": "São Félix do Xingu", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F RDC -PA", "Sua cidade": "Redenção", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F XIG-PA", "Sua cidade": "Xinguara", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F ELD-PA", "Sua cidade": "Eldorado do Carajás", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "SDA -PA", "Sua cidade": "São Domingos do Araguaia", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F PCA-PA", "Sua cidade": "Pacajá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F ITI-PA", "Sua cidade": "Itupiranga", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F JCD-PA", "Sua cidade": "Jacundá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F TUR-PA", "Sua cidade": "Tucuruí", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "NRE -PA", "Sua cidade": "Novo Repartimento", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F NMB-PA", "Sua cidade": "Marabá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "AMP -PA", "Sua cidade": "Marabá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "BVD -PA", "Sua cidade": "Benevides", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "JOHAN RAFAEL QUEIROZ PACHECO"},
    {"Nome da base de entrega": "VGA -PA", "Sua cidade": "Vigia", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "JOHAN RAFAEL QUEIROZ PACHECO"},
    {"Nome da base de entrega": "CST -PA", "Sua cidade": "Castanhal", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "JOHAN RAFAEL QUEIROZ PACHECO"},
    {"Nome da base de entrega": "F IGA-PA", "Sua cidade": "Igarapé Açú", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "JOHAN RAFAEL QUEIROZ PACHECO"},
    {"Nome da base de entrega": "BRC -PA", "Sua cidade": "Barcarena", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "LOURIVAL RAIOL PORTAL FILHO"},
    {"Nome da base de entrega": "ABT -PA", "Sua cidade": "Abaetetuba", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "LOURIVAL RAIOL PORTAL FILHO"},
    {"Nome da base de entrega": "IGM -PA", "Sua cidade": "Igarapé-Miri", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "LOURIVAL RAIOL PORTAL FILHO"},
    {"Nome da base de entrega": "MJU -PA", "Sua cidade": "Moju", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "LOURIVAL RAIOL PORTAL FILHO"},
    {"Nome da base de entrega": "ICR -PA", "Sua cidade": "Belém", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "MRM -PA", "Sua cidade": "Belém", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "PDR -PA", "Sua cidade": "Belém", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "BEL -PA", "Sua cidade": "Belém", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "F PDP-PA", "Sua cidade": "Ponta de Pedras", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "F MTB-PA", "Sua cidade": "Marituba", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "F ANA-PA", "Sua cidade": "Ananindeua", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "COQ -PA", "Sua cidade": "Ananindeua", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "MCP FLUVIAL -AP", "Sua cidade": "Macapá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "F MCP-AP", "Sua cidade": "Macapá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "F MCP 02-AP", "Sua cidade": "Macapá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "F MAC-AP", "Sua cidade": "Macapá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "ANA FLUVIAL - PA", "Sua cidade": "Ananindeua", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "ANA -PA", "Sua cidade": "Ananindeua", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "F CRH-PA", "Sua cidade": "Curralinho", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "PRICILA DO ESPIRITO SANTO DE LIMA"},
    {"Nome da base de entrega": "PA MRB", "Sua cidade": "Marabá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "RAIMUNDO LIMA FILHO"},
    {"Nome da base de entrega": "F TPN-PA", "Sua cidade": "Belém", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "MARCELO HENRIQUE COSTA NOVAES"},
    {"Nome da base de entrega": "NMB -PA", "Sua cidade": "Marabá", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "FERNANDO SILVA OLIVEIRA"},
    {"Nome da base de entrega": "F IGM-PA", "Sua cidade": "Igarapé-Miri", "Coordenador": "ORLEAN DA SILVA DO NASCIMENTO", "Responsavel da base": "LOURIVAL RAIOL PORTAL FILHO"},
])

# =================================================
# FUNÇÕES
# =================================================
def validar_sla(df):
    colunas = {
        "Nome da base de entrega",
        "Qtd a entregar",
        "未签收-客户问题件",
        "未签收-其他问题件"
    }
    faltantes = colunas - set(df.columns)
    if faltantes:
        raise ValueError(f"Colunas ausentes no SLA: {faltantes}")

    if df.shape[1] < 15:
        raise ValueError("O SLA não possui a coluna O (Qtd Entregues no prazo)")


def calcular_sla(df_sla):
    validar_sla(df_sla)
    df = df_sla.copy()

    df["Qtd Entregues no prazo"] = pd.to_numeric(df.iloc[:, 14], errors="coerce").fillna(0)
    df["Qtd a entregar"] = pd.to_numeric(df["Qtd a entregar"], errors="coerce").fillna(0)

    df = df.merge(RESPONSAVEIS_BASE, on="Nome da base de entrega", how="left")
    df = df[df["Responsavel da base"].notna()]

    df["Pacotes Problematicos"] = (
        pd.to_numeric(df["未签收-客户问题件"], errors="coerce").fillna(0)
        + pd.to_numeric(df["未签收-其他问题件"], errors="coerce").fillna(0)
    ).astype(int)

    df["SLA (%)"] = (df["Qtd Entregues no prazo"] / df["Qtd a entregar"] * 100).round(2)

    necessario = df["Qtd a entregar"] * META_SLA
    df["Qtd de pacotes faltantes para 96%"] = (
        necessario - df["Qtd Entregues no prazo"]
    ).apply(lambda x: max(0, round(x, 2)))

    df["Status SLA"] = pd.cut(
        df["SLA (%)"],
        bins=[-1, 93, 96, float("inf")],
        labels=["🔴 Crítico", "🟡 Atenção", "🟢 SLA Batido"]
    )

    return df


def gerar_resumo(df):
    return {
        "Total a entregar": int(df["Qtd a entregar"].sum()),
        "Entregues no prazo": int(df["Qtd Entregues no prazo"].sum()),
        "Pacotes problemáticos": int(df["Pacotes Problematicos"].sum()),
        "SLA Geral (%)": round(df["SLA (%)"].mean(), 2) if len(df) else 0
    }
