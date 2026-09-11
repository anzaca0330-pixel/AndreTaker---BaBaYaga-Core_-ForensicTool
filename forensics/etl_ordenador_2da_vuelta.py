import pandas as pd
import os

# Rutas de entrada y salida
RUTA_ENTRADA_CSV = "/media/andrea-zabala-c/D A T A1/01_EVIDENCIA/reporte_preconteo.csv"
RUTA_SALIDA_CSV = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/01_EVIDENCIA/MATRIZ_MAESTRA_2DA_VUELTA.csv"

def limpiar_y_ordenar_matriz():
    print(f"[KEPLER] Iniciando proceso ETL sobre: {RUTA_ENTRADA_CSV}")
    
    # Cargar CSV usando punto y coma como delimitador
    df = pd.read_csv(RUTA_ENTRADA_CSV, sep=';', dtype=str)
    
    # Rellenar nulos con 0 para evitar errores matemáticos en Benford
    columnas_votos = ['Blancos', 'Nulos', 'Ivan Cepeda', 'Abelardo De la espriella', 'No Marcados']
    for col in columnas_votos:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        
    # Asegurar el formato de ceros a la izquierda para la jerarquía geográfica
    df['cod_departamento'] = df['cod_departamento'].str.zfill(2)
    df['cod_municipio'] = df['cod_municipio'].str.zfill(3)
    df['zona'] = df['zona'].str.zfill(2)
    df['puesto'] = df['puesto'].str.zfill(2)
    df['num_mesa'] = df['num_mesa'].str.zfill(6)
    
    print("[KEPLER] Sanitización completada. Rellenando nulos y ajustando padding.")
    
    # Ordenar jerárquicamente
    print("[KEPLER] Ordenando jerarquía geográfica: Depto -> Mpio -> Zona -> Puesto -> Mesa")
    df = df.sort_values(by=['cod_departamento', 'cod_municipio', 'zona', 'puesto', 'num_mesa'])
    
    # Asegurar que el directorio exista
    os.makedirs(os.path.dirname(RUTA_SALIDA_CSV), exist_ok=True)
    
    # Guardar en la Bóveda Ext4
    df.to_csv(RUTA_SALIDA_CSV, index=False)
    print(f"[KEPLER] MATRIZ MAESTRA GENERADA EXITOSAMENTE EN: {RUTA_SALIDA_CSV}")
    print(f"[KEPLER] Total de actas (mesas) procesadas: {len(df)}")

if __name__ == "__main__":
    limpiar_y_ordenar_matriz()
