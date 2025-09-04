import pandas as pd
import json

def analisar_dados():
    arquivo_excel = "3618_all_governors_20250903_212630(1).xlsx"
    arquivo_json = "dados_filtrados.json"
    
    # Ler top 310 da planilha
    df = pd.read_excel(arquivo_excel)
    df_top310 = df.head(310)
    
    # Calcular poder total dos top 310
    col_poder = None
    for col in df.columns:
        if 'power' in col.lower() or 'poder' in col.lower():
            col_poder = col
            break
    
    if not col_poder:
        print("Coluna de poder não encontrada")
        return
    
    poder_total_top310 = df_top310[col_poder].sum()
    
    # Ler dados filtrados (farms)
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        dados_farms = json.load(f)
    
    # Calcular poder total das farms
    poder_total_farms = sum(farm['Power'] for farm in dados_farms)
    
    # Calcular estatísticas
    total_farms = len(dados_farms)
    porcentagem_farms = (poder_total_farms / poder_total_top310) * 100
    
    resultado = {
        'poder_total_top310': int(poder_total_top310),
        'poder_total_farms': int(poder_total_farms),
        'total_farms': total_farms,
        'porcentagem_farms': round(porcentagem_farms, 2),
        'total_top310': 310
    }
    
    # Salvar resultado em JSON
    with open('analise_reino.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    
    print(f"Poder total top 310: {poder_total_top310:,}")
    print(f"Poder total farms: {poder_total_farms:,}")
    print(f"Total de farms: {total_farms}")
    print(f"% do poder nas farms: {porcentagem_farms:.2f}%")
    
    return resultado

if __name__ == "__main__":
    analisar_dados()