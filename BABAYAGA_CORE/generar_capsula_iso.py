#!/usr/bin/env python3
"""
FORJA DE CÁPSULA WORM (ISO) - NÚCLEO PERICIAL BABA YAGA
Tycho / AndreTaker - Preservación en Policarbonato Inmutable
"""

import os
import shutil
import subprocess
import time

ISO_NAME = "NUCLEO_PERICIAL_BABAYAGA_2026.iso"
STAGING_DIR = "/home/andrea-zabala-c/Desktop/STAGING_ISO_BABAYAGA"
OUTPUT_ISO_PATH = f"/home/andrea-zabala-c/Desktop/{ISO_NAME}"

# Rutas críticas de evidencia que formarán el núcleo
SOURCES = {
    "HASHES_SHA256_MAESTROS": "/home/andrea-zabala-c/Desktop/PAQUETE_CSVS_Y_HASHES_SHA256_DRIVE/01_BASES_NACIONALES_Y_HASHES_MAESTROS",
    "SCRIPTS_FORENSES_ORIGINALES": "/home/andrea-zabala-c/Desktop/SCRIPTS_FORENSES",
    "BITACORAS_Y_ARQUITECTURA": "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/03_DOCUMENTACION"
}

def main():
    print("=" * 60)
    print("🛡️ INICIANDO FORJA DE CÁPSULA FORENSE WORM (ISO) 🛡️")
    print("=" * 60)
    
    # 1. Preparar staging
    if os.path.exists(STAGING_DIR):
        print(f"Limpiando directorio de ensamblaje: {STAGING_DIR}")
        shutil.rmtree(STAGING_DIR)
    os.makedirs(STAGING_DIR)

    # 2. Copiar evidencias al staging
    for folder_name, source_path in SOURCES.items():
        dest_path = os.path.join(STAGING_DIR, folder_name)
        if os.path.exists(source_path):
            print(f"Clonando acervo: {folder_name} ...")
            shutil.copytree(source_path, dest_path, ignore=shutil.ignore_patterns('*.pyc', '__pycache__', '.venv', '.git'))
        else:
            print(f"⚠️ Advertencia: No se encontró la ruta {source_path}")

    # 3. Generar la imagen ISO usando genisoimage (estándar en Xubuntu)
    print("\n💿 Forjando imagen ISO de policarbonato...")
    try:
        # Comando para crear ISO 9660 con extensiones Joliet y Rock Ridge
        cmd = [
            "genisoimage",
            "-J", "-joliet-long", "-R", "-V", "NUCLEO_PERICIAL",
            "-o", OUTPUT_ISO_PATH,
            STAGING_DIR
        ]
        
        resultado = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if resultado.returncode == 0:
            size_mb = os.path.getsize(OUTPUT_ISO_PATH) / (1024 * 1024)
            print(f"\n✅ ÉXITO: Cápsula ISO forjada correctamente.")
            print(f"📍 Ruta: {OUTPUT_ISO_PATH}")
            print(f"⚖️ Tamaño: {size_mb:.2f} MB (Cabe perfectamente en un DVD o CD)")
            print("\n🔥 Siguiente paso: Quémala en un disco usando Brasero o Xfburn en tu Xubuntu.")
        else:
            print(f"\n❌ Error forjando la ISO: {resultado.stderr}")
            print("¿Tienes 'genisoimage' instalado? (sudo apt install genisoimage)")
            
    except FileNotFoundError:
        print("\n❌ Error: El comando 'genisoimage' no está instalado en el sistema.")
        print("Instálalo ejecutando: sudo apt install genisoimage")
    
    # Limpieza
    if os.path.exists(STAGING_DIR):
        shutil.rmtree(STAGING_DIR)
        print("\n🧹 Directorio de ensamblaje purgado.")

if __name__ == "__main__":
    main()
