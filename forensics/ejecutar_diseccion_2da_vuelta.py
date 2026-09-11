import pandas as pd
import numpy as np
from scipy.stats import chisquare

def analizar_benford_2da_vuelta():
    print("[TYCHO] Iniciando disección estadística (Segunda Vuelta - Motor Benford 2BL)")
    ruta = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/01_EVIDENCIA/MATRIZ_MAESTRA_2DA_VUELTA.csv"
    
    # Probabilidades teóricas de Benford (2do dígito)
    benford_2bl = {
        0: 0.11968, 1: 0.11389, 2: 0.10882, 3: 0.10433,
        4: 0.10031, 5: 0.09668, 6: 0.09337, 7: 0.09035,
        8: 0.08757, 9: 0.08500
    }
    
    try:
        df = pd.read_csv(ruta)
    except FileNotFoundError:
        print("[TYCHO] ERROR: Matriz Maestra de 2da Vuelta no encontrada.")
        return

    # Extraer 2do dígito para Ivan Cepeda
    votos_cepeda = df['Ivan Cepeda'].dropna().astype(str).str.replace(r'\.0$', '', regex=True)
    votos_cepeda = votos_cepeda[votos_cepeda.str.len() >= 2]
    d2_cepeda = votos_cepeda.str[1].astype(int)
    freq_cepeda = d2_cepeda.value_counts(normalize=True).sort_index()

    # Extraer 2do dígito para Abelardo De la espriella
    votos_abelardo = df['Abelardo De la espriella'].dropna().astype(str).str.replace(r'\.0$', '', regex=True)
    votos_abelardo = votos_abelardo[votos_abelardo.str.len() >= 2]
    d2_abelardo = votos_abelardo.str[1].astype(int)
    freq_abelardo = d2_abelardo.value_counts(normalize=True).sort_index()

    print("\n--- DISTRIBUCIÓN NACIONAL (SEGUNDA VUELTA) ---")
    print("Dígito | Benford (Teórico) | I. Cepeda (Real) | A. De la Espriella (Real)")
    print("-" * 75)
    
    for d in range(10):
        t_b = benford_2bl[d]
        f_c = freq_cepeda.get(d, 0)
        f_a = freq_abelardo.get(d, 0)
        print(f"  {d}    |      {t_b:.4f}       |     {f_c:.4f}       |        {f_a:.4f}")
        
    # Chi-Square Test I. Cepeda
    obs_cepeda = [freq_cepeda.get(d, 0) * len(d2_cepeda) for d in range(10)]
    exp_cepeda = [benford_2bl[d] * len(d2_cepeda) for d in range(10)]
    chi2_c, p_c = chisquare(obs_cepeda, f_exp=exp_cepeda)
    
    # Chi-Square Test A. De la espriella
    obs_abelardo = [freq_abelardo.get(d, 0) * len(d2_abelardo) for d in range(10)]
    exp_abelardo = [benford_2bl[d] * len(d2_abelardo) for d in range(10)]
    chi2_a, p_a = chisquare(obs_abelardo, f_exp=exp_abelardo)

    print("\n--- PRUEBA DE DIVERGENCIA (CHI-CUADRADO) ---")
    print(f"P-Value I. Cepeda:           {p_c:.4e}")
    print(f"P-Value A. De la Espriella:  {p_a:.4e}")
    
    if p_c < 0.05 or p_a < 0.05:
        print("\n[ALERTA ROJA] Divergencia estadística masiva detectada. La Segunda Vuelta presenta manipulación estructural a escala nacional.")
    else:
        print("\n[NORMAL] No se detectó divergencia a nivel nacional.")

if __name__ == "__main__":
    analizar_benford_2da_vuelta()
