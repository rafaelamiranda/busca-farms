import pandas as pd
import json
import os

def filtrar_dados_planilha():
    arquivo_excel = "3618_all_governors_20250903_212630(1).xlsx"
    arquivo_json = "dados_filtrados.json"
    
    try:
        df = pd.read_excel(arquivo_excel)
        
        # Filtrar TODAS as farms, não apenas as do top 310
        colunas = df.columns.tolist()
        col_ch = colunas[3]
        col_clickable = colunas[4] 
        
        col_alianca = None
        for col in colunas:
            if 'alliance' in col.lower() or 'aliança' in col.lower() or 'guild' in col.lower():
                col_alianca = col
                break
        
        filtro = (df[col_ch] == 25) & (df[col_clickable] == True)
        
        if col_alianca:
            filtro = filtro & (df[col_alianca] != "Thousand Sunny br")
        
        dados_filtrados = df[filtro]
        dados_json = dados_filtrados.to_dict('records')
        
        # Substituir NaN por string vazia
        for registro in dados_json:
            for chave, valor in registro.items():
                if pd.isna(valor):
                    registro[chave] = ""
        
        dados_existentes = []
        if os.path.exists(arquivo_json):
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                dados_existentes = json.load(f)
        
        dados_existentes.extend(dados_json)
        
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados_existentes, f, ensure_ascii=False, indent=2)
        
        print(f"Processados {len(df)} registros totais")
        print(f"Filtrados {len(dados_filtrados)} farms encontradas")
        print(f"Total no JSON: {len(dados_existentes)} registros")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    filtrar_dados_planilha()