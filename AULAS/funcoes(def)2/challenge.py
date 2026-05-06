import pandas as pd
import numpy as np

# ==========================================
# 1. INGESTÃO E ESTRUTURAÇÃO DE DADOS
# ==========================================
def carregar_dados_simulados():
    """Gera um DataFrame com dados fictícios e algumas inconsistências propositais."""
    dados = [
        {'id_equipamento': 'EQP-001', 'regiao': 'Norte', 'tipo_operacao': 'Campo', 'proximidade_agua': 'Nao', 'condicao_ambiental': 'Boa', 'historico_incidentes': 0, 'data': '12/04/2023'},
        {'id_equipamento': 'EQP-002', 'regiao': 'Sul', 'tipo_operacao': 'Transporte', 'proximidade_agua': 'Sim', 'condicao_ambiental': 'Adversa', 'historico_incidentes': 2, 'data': '15-04-2023'},
        {'id_equipamento': 'EQP-003', 'regiao': 'Leste', 'tipo_operacao': 'Campo', 'proximidade_agua': np.nan, 'condicao_ambiental': 'Extrema', 'historico_incidentes': 5, 'data': '20/04/2023'},
        {'id_equipamento': 'EQP-004', 'regiao': 'Norte', 'tipo_operacao': 'manutencao', 'proximidade_agua': 'Sim', 'condicao_ambiental': 'Boa', 'historico_incidentes': 1, 'data': '22/04/2023'},
        {'id_equipamento': 'EQP-005', 'regiao': 'Oeste', 'tipo_operacao': 'Transporte', 'proximidade_agua': 'Nao', 'condicao_ambiental': np.nan, 'historico_incidentes': 0, 'data': '01/05/2023'}
    ]
    print("[OK] Base de dados carregada com sucesso!\n")
    return pd.DataFrame(dados)

# ==========================================
# 2. PREPARAÇÃO E LIMPEZA DOS DADOS
# ==========================================
def limpar_dados(df):
    """Trata nulos, padroniza categorias e corrige tipos de dados."""
    df_limpo = df.copy()
    
    # Tratamento de valores nulos (Preenchendo com valores padrão)
    df_limpo['proximidade_agua'] = df_limpo['proximidade_agua'].fillna('Nao')
    df_limpo['condicao_ambiental'] = df_limpo['condicao_ambiental'].fillna('Boa')
    
    # Padronização de categorias (Tudo para a primeira letra maiúscula)
    df_limpo['tipo_operacao'] = df_limpo['tipo_operacao'].str.title()
    
    # Conversão de tipos (Datas) - Tratando inconsistências no formato
    df_limpo['data'] = pd.to_datetime(df_limpo['data'], format='mixed', dayfirst=True)
    
    print("[OK] Dados limpos e padronizados!\n")
    return df_limpo

# ==========================================
# 3. FEATURE ENGINEERING & 4. ANÁLISE DE RISCO
# ==========================================
def calcular_score_risco(linha):
    """
    Usa condicionais (if/elif/else) para criar variáveis analíticas e calcular o score.
    Retorna um dicionário com as novas features.
    """
    risco_operacional = 0
    risco_ambiental = 0
    
    # Regras de Risco Operacional
    if linha['tipo_operacao'] == 'Transporte':
        risco_operacional += 2
    if linha['proximidade_agua'] == 'Sim':
        risco_operacional += 3
        
    # Regras de Risco Ambiental
    if linha['condicao_ambiental'] == 'Adversa':
        risco_ambiental += 2
    elif linha['condicao_ambiental'] == 'Extrema':
        risco_ambiental += 4
        
    # Frequência de Incidentes (Peso 1.5)
    freq_incidentes = linha['historico_incidentes'] * 1.5
    
    # Score Total
    score_total = risco_operacional + risco_ambiental + freq_incidentes
    
    # Classificação de Risco
    if score_total < 3:
        classificacao = 'Baixo'
    elif 3 <= score_total < 7:
        classificacao = 'Médio'
    else:
        classificacao = 'Alto'
        
    return pd.Series([risco_operacional, risco_ambiental, freq_incidentes, score_total, classificacao])

def processar_analise_risco(df):
    """Aplica o feature engineering no DataFrame."""
    # Criando novas colunas com base na função de cálculo
    colunas_novas = ['risco_operacional', 'risco_ambiental', 'freq_incidentes', 'score_risco', 'zona_critica']
    df[colunas_novas] = df.apply(calcular_score_risco, axis=1)
    
    print("[OK] Análise de risco e Feature Engineering concluídos!\n")
    return df

# ==========================================
# 5. GERAÇÃO DE ALERTAS
# ==========================================
def gerar_alertas(df):
    """Usa listas e dicionários para mapear e exibir os alertas preventivos."""
    alertas = [] # Lista para armazenar dicionários de alertas
    
    for _, linha in df.iterrows():
        motivos = []
        if linha['zona_critica'] == 'Alto':
            if linha['proximidade_agua'] == 'Sim' and linha['condicao_ambiental'] != 'Boa':
                motivos.append("Risco elevado de operação próxima à água em condições ruins.")
            if linha['historico_incidentes'] >= 3:
                motivos.append("Alto histórico de incidentes prévios.")
            
            # Adiciona dicionário à lista
            alertas.append({
                'equipamento': linha['id_equipamento'],
                'regiao': linha['regiao'],
                'motivos': motivos
            })
            
    print("--- ALERTAS PREVENTIVOS GERADOS ---")
    if not alertas:
        print("Nenhum alerta crítico no momento.")
    else:
        for alerta in alertas:
            print(f"⚠️ ATENÇÃO: Equipamento {alerta['equipamento']} ({alerta['regiao']})")
            for motivo in alerta['motivos']:
                print(f"  - {motivo}")
    print("-----------------------------------\n")

# ==========================================
# 6. RELATÓRIOS
# ==========================================
def exibir_relatorios(df):
    """Gera relatórios usando agregações do Pandas."""
    print("--- RELATÓRIOS GERADOS ---")
    
    print("\n1. Equipamentos com Maior Risco (Ordenado por Score):")
    df_ordenado = df.sort_values(by='score_risco', ascending=False)[['id_equipamento', 'score_risco', 'zona_critica']]
    print(df_ordenado.to_string(index=False))
    
    print("\n2. Ranking de Risco Médio por Região:")
    ranking_regiao = df.groupby('regiao')['score_risco'].mean().reset_index()
    ranking_regiao = ranking_regiao.sort_values(by='score_risco', ascending=False)
    print(ranking_regiao.to_string(index=False))
    
    print("\n3. Ranking de Risco Médio por Tipo de Operação:")
    ranking_op = df.groupby('tipo_operacao')['score_risco'].mean().reset_index()
    ranking_op = ranking_op.sort_values(by='score_risco', ascending=False)
    print(ranking_op.to_string(index=False))
    print("-----------------------------------\n")

# ==========================================
# 7. MENU INTERATIVO
# ==========================================
def menu_interativo():
    df = None
    
    while True:
        print("\n=== SISTEMA DE GESTÃO DE RISCO OPERACIONAL ===")
        print("1. Carregar Dados")
        print("2. Limpar e Preparar Dados")
        print("3. Executar Análise de Risco (Feature Engineering)")
        print("4. Exibir Alertas Preventivos")
        print("5. Gerar Relatórios Analíticos")
        print("6. Sair")
        print("==============================================")
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == '1':
            df = carregar_dados_simulados()
        elif opcao == '2':
            if df is not None:
                df = limpar_dados(df)
            else:
                print("[ERRO] Carregue os dados primeiro (Opção 1).")
        elif opcao == '3':
            if df is not None and 'proximidade_agua' in df.columns:
                df = processar_analise_risco(df)
            else:
                print("[ERRO] Carregue e limpe os dados primeiro (Opções 1 e 2).")
        elif opcao == '4':
            if df is not None and 'zona_critica' in df.columns:
                gerar_alertas(df)
            else:
                print("[ERRO] Execute a Análise de Risco primeiro (Opção 3).")
        elif opcao == '5':
             if df is not None and 'zona_critica' in df.columns:
                exibir_relatorios(df)
             else:
                print("[ERRO] Execute a Análise de Risco primeiro (Opção 3).")
        elif opcao == '6':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Tente novamente.")

# Executa o sistema
if __name__ == "__main__":
    menu_interativo()