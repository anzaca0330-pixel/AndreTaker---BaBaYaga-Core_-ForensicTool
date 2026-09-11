import fitz
import os
import csv
import sys

def es_sintetico(ruta_pdf):
    try:
        doc = fitz.open(ruta_pdf)
        for pagina in doc:
            lista_imagenes = pagina.get_images(full=True)
            if not lista_imagenes:
                # No hay imágenes en absoluto, puros vectores/texto. ¡Totalmente sintético!
                return True, "Vector Puro (Ausencia total de escaneo)"
            
            # Revisar las propiedades de cada imagen
            for img_info in lista_imagenes:
                xref = img_info[0]
                smask = img_info[1]
                bpc = img_info[4]
                
                # Si una imagen tiene máscara de transparencia (smask > 0) o es de 1 bit por canal (Blind Masking)
                if smask > 0:
                    return True, f"Canal Alfa / Transparencia detectado (XREF: {xref})"
                if bpc == 1:
                    return True, f"Blind Masking 1-BPC detectado (XREF: {xref})"
                    
        # Si tiene imágenes y ninguna tiene transparencia evidente, asumimos que podría ser un escaneo real
        return False, "ORGÁNICO"
    except Exception as e:
        return False, f"ERROR_LECTURA: {str(e)}"

def escanear_directorio(directorio_base):
    print(f"[BABA YAGA] Iniciando cacería en: {directorio_base}")
    archivos_sinteticos = []
    
    total = 0
    falsos = 0
    
    for raiz, dirs, archivos in os.walk(directorio_base):
        for arch in archivos:
            if arch.lower().endswith('.pdf'):
                total += 1
                ruta_completa = os.path.join(raiz, arch)
                es_falso, motivo = es_sintetico(ruta_completa)
                
                if es_falso:
                    falsos += 1
                    archivos_sinteticos.append([ruta_completa, motivo])
                    print(f"[{falsos}] [ALERTA ROJA] {arch}: {motivo}")
                    
    print(f"\n[BABA YAGA] Escaneo finalizado. Total PDFs revisados: {total}")
    print(f"[BABA YAGA] Total Sintéticos/Falsos: {falsos}")
    
    ruta_salida = '/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/01_EVIDENCIA/REPORTE_E24_FALSOS.csv'
    with open(ruta_salida, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Ruta_Archivo", "Firma_Estructural"])
        writer.writerows(archivos_sinteticos)
    print(f"[BABA YAGA] Matriz de Falsificaciones guardada en: {ruta_salida}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        escanear_directorio(sys.argv[1])
    else:
        print("Uso: python3 cazador_sintetico_e24.py <ruta_directorio>")
