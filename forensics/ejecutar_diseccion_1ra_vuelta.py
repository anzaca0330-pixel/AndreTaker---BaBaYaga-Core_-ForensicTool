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

def run_benford_2bl(data_series, name):
    print(f"--- Análisis Benford 2BL: {name} ---")
    # Extraer el segundo dígito
    digits = data_series.apply(extract_second_digit)
    digits = digits[digits != -1] # Filtrar inválidos/un solo dígito
    
    if len(digits) == 0:
        print("[!] No hay datos suficientes para Benford.")
        return
        
    counts = digits.value_counts().sort_index()
    # Asegurar que todos los dígitos del 0 al 9 estén presentes
    for i in range(10):
        if i not in counts:
            counts[i] = 0
    counts = counts.sort_index()
    
    total_valid = len(digits)
    actual_probs = counts / total_valid
    
    # Probabilidades teóricas 2BL
    benford_2bl_probs = np.array([0.11968, 0.11389, 0.10882, 0.10433, 0.10031, 
                                  0.09668, 0.09337, 0.09035, 0.08757, 0.08500])
    expected_counts = benford_2bl_probs * total_valid
    
    # Chi-Square Test
    chi2_stat, p_value = chisquare(f_obs=counts, f_exp=expected_counts)
    
    print(f"Total de registros válidos: {total_valid}")
    print(f"Chi-Cuadrado (Estadístico): {chi2_stat:.2f}")
    print(f"P-Value: {p_value:.6e}")
    
    if p_value < 0.05:
        print("[!] ALERTA FORENSE: Divergencia Matemática Detectada. Distribución NO natural.")
    else:
        print("[+] Distribución dentro de los parámetros orgánicos (Sin alteración evidente).")
    print("")

def diseccionar_primera_vuelta():
    print("=== INICIANDO BISTURÍ FORENSE (PRIMERA VUELTA) ===")
    
    ruta_micro = '../01_EVIDENCIA/DATA_1RA_VUELTA/REPORTE_FRAUDE_POR_MUNICIPIO.csv'
    try:
        df_micro = pd.read_csv(ruta_micro, sep=',')
        print(f"[*] Ingestando {df_micro.shape[0]} reportes municipales...")
        
        # Analizando Registraduría (Output E-24 Web Alterado)
        print("[*] Diseccionando datos Oficiales (Web Registraduría)...")
        run_benford_2bl(df_micro['cepeda_reg'], "Votos Cepeda (Registraduría)")
        run_benford_2bl(df_micro['espriella_reg'], "Votos Espriella (Registraduría)")
        
        # Analizando Testigos (Input Claveros Original)
        print("[*] Diseccionando datos Físicos (Testigos Electorales)...")
        run_benford_2bl(df_micro['cepeda_testigos'], "Votos Cepeda (Testigos)")
        run_benford_2bl(df_micro['espriella_testigos'], "Votos Espriella (Testigos)")
        
    except Exception as e:
        print(f"[!] Error leyendo el dataset: {e}")

if __name__ == "__main__":
    diseccionar_primera_vuelta()
