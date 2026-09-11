import os
import subprocess
import glob
from colorama import Fore, Style, init

init(autoreset=True)

def analizar_pdf(ruta_pdf):
    hallazgos = {
        'Estructura_XREF_Anomala': False,
        'Capa_1bpc_Inyectada': False,
        'Error_Ejecucion': False
    }
    
    # 1. Análisis XREF (qpdf)
    try:
        resultado_qpdf = subprocess.run(['qpdf', '--check', ruta_pdf], 
                                        capture_output=True, text=True, timeout=10)
        output_qpdf = resultado_qpdf.stderr + resultado_qpdf.stdout
        
        if "reported number of objects" in output_qpdf and "is not one plus the highest" in output_qpdf:
            hallazgos['Estructura_XREF_Anomala'] = True
    except Exception as e:
        hallazgos['Error_Ejecucion'] = True

    # 2. Análisis de Capas de Imagen (pdfimages)
    try:
        resultado_pdfimages = subprocess.run(['pdfimages', '-list', ruta_pdf], 
                                             capture_output=True, text=True, timeout=10)
        output_pdfimages = resultado_pdfimages.stdout
        
        lineas = output_pdfimages.split('\n')
        for linea in lineas[2:]: 
            if 'image' in linea:
                columnas = linea.split()
                if len(columnas) >= 8:
                    bpc = columnas[7]
                    color = columnas[5]
                    if bpc == '1' and (color == 'gray' or color == 'devgray'):
                        hallazgos['Capa_1bpc_Inyectada'] = True
                        break
    except Exception as e:
        hallazgos['Error_Ejecucion'] = True
        
    return hallazgos

def modo_diablo():
    print(Fore.RED + "==========================================================")
    print(Fore.RED + "☠️  INICIANDO BABA YAGA CORE - MODO DIABLO (EXTRACCIÓN TOTAL) ☠️")
    print(Fore.RED + "==========================================================")
    
    # Buscar todos los PDFs en la evidencia rescatada de la primera vuelta
    directorio_base = '../01_EVIDENCIA/EVIDENCIAS_RESCATADAS_1RA_VUELTA'
    archivos_pdf = glob.glob(os.path.join(directorio_base, '*.pdf'))
    
    print(Fore.YELLOW + f"[*] Escaneando {len(archivos_pdf)} archivos con el Bisturí Forense...\n")
    
    infectados_totales = 0
    
    for pdf in archivos_pdf:
        nombre = os.path.basename(pdf)
        print(f"Buscando en: {nombre}...")
        hallazgos = analizar_pdf(pdf)
        
        msg = f"  -> {nombre}: "
        infectado = False
        
        if hallazgos['Error_Ejecucion']:
            msg += Fore.MAGENTA + "[ERROR LECTURA BINARIA] "
            
        if hallazgos['Estructura_XREF_Anomala']:
            msg += Fore.RED + "[XREF +2 MUTADA] "
            infectado = True
            
        if hallazgos['Capa_1bpc_Inyectada']:
            msg += Fore.RED + "[MÁSCARA 1bpc DETECTADA] "
            infectado = True
            
        if infectado:
            infectados_totales += 1
            print(msg)
        else:
            print(Fore.GREEN + msg + "[ORGÁNICO - SIN MUTACIÓN]")
            
    print(Fore.RED + "\n==========================================================")
    print(Fore.RED + f"DIAGNÓSTICO FINAL: {infectados_totales}/{len(archivos_pdf)} ARCHIVOS ESTRUCTURALMENTE CORROMPIDOS.")
    print(Fore.RED + "EL BLIND MASKING HA SIDO EXPUESTO.")

if __name__ == "__main__":
    modo_diablo()
