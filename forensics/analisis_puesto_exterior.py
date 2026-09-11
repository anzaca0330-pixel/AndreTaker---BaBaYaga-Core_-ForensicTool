import pandas as pd
import numpy as np
from scipy.stats import chisquare

def extract_second_digit(number):
    if pd.isna(number):
        return -1
    num_str = str(abs(int(number)))
    if len(num_str) < 2:
        return -1
    return int(num_str[1])

def check_benford(digits_series):
    digits = digits_series[digits_series != -1]
    if len(digits) < 30: # Necesitamos un tamaño de muestra mínimo estadísticamente significativo
        return None, None
        
    counts = digits.value_counts().sort_index()
    for i in range(10):
        if i not in counts:
            counts[i] = 0
    counts = counts.sort_index()
    
    total_valid = len(digits)
    benford_2bl_probs = np.array([0.11968, 0.11389, 0.10882, 0.10433, 0.10031, 
                                  0.09668, 0.09337, 0.09035, 0.08757, 0.08500])
    expected_counts = benford_2bl_probs * total_valid
    
    # Manejar ceros en expected_counts agregando un pequeño delta o ignorando
    try:
        chi2_stat, p_value = chisquare(f_obs=counts, f_exp=expected_counts)
        return chi2_stat, p_value
    except:
        return None, None

def diseccionar_puesto_por_puesto():
    print("=== DISECCIÓN GRANULAR: PUESTO POR PUESTO (EXTERIOR) ===")
    ruta_datos = '../01_EVIDENCIA/CONSULADOS_DATASET_Y_FUENTES_ORIGEN/reporte_preconteo_oficial_registraduria_depto88.csv'
    
    try:
        df = pd.read_csv(ruta_datos, sep=';', dtype=str)
        # Convertir a numerico
        df['Ivan Cepeda'] = pd.to_numeric(df['Ivan Cepeda'], errors='coerce')
        df['Abelardo De la espriella'] = pd.to_numeric(df['Abelardo De la espriella'], errors='coerce')
        
        # Filtrar solo Depto 88 (Consulados/Exterior) si existe, o usar todo si el archivo es solo eso
        df_ext = df[df['cod_departamento'] == '88']
        if df_ext.empty:
            print("[!] No se encontraron registros con cod_departamento == 88. Analizando todo el dataset disponible agrupado por depto/puesto.")
            df_ext = df
            
        print(f"[*] Analizando {len(df_ext)} mesas totales.")
        
        # Agrupar por departamento y puesto
        agrupado = df_ext.groupby(['cod_departamento', 'cod_municipio', 'zona', 'puesto'])
        
        anomalias_encontradas = 0
        
        for (depto, mpio, zona, puesto), grupo in agrupado:
            # Cepeda
            d2_cepeda = grupo['Ivan Cepeda'].apply(extract_second_digit)
            _, p_val_cepeda = check_benford(d2_cepeda)
            
            # Espriella
            d2_espriella = grupo['Abelardo De la espriella'].apply(extract_second_digit)
            _, p_val_espriella = check_benford(d2_espriella)
            
            alerta = False
            msg = f"Depto:{depto} Mpio:{mpio} Zona:{zona} Puesto:{puesto} | Mesas: {len(grupo)} | "
            if p_val_cepeda is not None and p_val_cepeda < 0.05:
                msg += f"CEPEDA ANÓMALO (p={p_val_cepeda:.4f}) "
                alerta = True
            if p_val_espriella is not None and p_val_espriella < 0.05:
                msg += f"ESPRIELLA ANÓMALO (p={p_val_espriella:.4f}) "
                alerta = True
                
            if alerta:
                print(f"[ALERTA ROJA] {msg}")
                anomalias_encontradas += 1
                
        print(f"\n[*] Análisis completado. Puestos con anomalías detectadas: {anomalias_encontradas}")
        
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    diseccionar_puesto_por_puesto()
