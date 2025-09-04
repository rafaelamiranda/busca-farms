import pandas as pd
import json

def analisar_dados():
    arquivo_excel = "3618_all_governors_20250903_212630(1).xlsx"
    arquivo_json = "dados_filtrados.json"
    
    # Ler top 300 da planilha
    df = pd.read_excel(arquivo_excel)
    df_top300 = df.head(300)
    
    # Calcular poder total dos top 300
    col_poder = None
    for col in df.columns:
        if 'power' in col.lower() or 'poder' in col.lower():
            col_poder = col
            break
    
    if not col_poder:
        print("Coluna de poder não encontrada")
        return
    
    poder_total_top300 = df_top300[col_poder].sum()
    
    # Ler dados filtrados (farms)
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        todas_farms = json.load(f)
    
    # Filtrar apenas as farms que estão no top 300
    farms_top300 = []
    for farm in todas_farms:
        if farm.get('#', 0) <= 300:  # Considerar apenas farms dentro do top 300
            farms_top300.append(farm)
    
    # Calcular poder total das farms que estão no top 300
    poder_total_farms = sum(farm['Power'] for farm in farms_top300)
    
    # Calcular estatísticas
    total_farms_top300 = len(farms_top300)  # Farms dentro do top 300
    total_farms_todas = len(todas_farms)    # Todas as farms encontradas
    porcentagem_farms = (poder_total_farms / poder_total_top300) * 100
    
    resultado = {
        'poder_total_top300': int(poder_total_top300),
        'poder_total_farms': int(poder_total_farms),
        'total_farms_top300': total_farms_top300,
        'total_farms_todas': total_farms_todas,
        'porcentagem_farms': round(porcentagem_farms, 2),
        'total_top300': 300
    }
    
    # Salvar resultado em JSON
    with open('analise_reino.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    
    print(f"Poder total top 300: {poder_total_top300:,}")
    print(f"Poder total farms (apenas top 300): {poder_total_farms:,}")
    print(f"Farms no top 300: {total_farms_top300}")
    print(f"Total de farms encontradas: {total_farms_todas}")
    print(f"% do poder nas farms: {porcentagem_farms:.2f}%")
    
    return resultado

if __name__ == "__main__":
    analisar_dados()