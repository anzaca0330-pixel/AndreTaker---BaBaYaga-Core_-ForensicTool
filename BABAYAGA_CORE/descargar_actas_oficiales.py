#!/usr/bin/env python3
"""
Motor de Extracción Asíncrona (Scraping) de Actas E-14
BaBaYaga Core - Tycho Module
Este script apunta al servidor oficial proporcionado por la investigadora:
https://divulgacione14presidentet.registraduria.gov.co/home
Extrae y descarga los PDFs directamente al disco ANZACA_EXT4.
"""

import os
import aiohttp
import asyncio
import hashlib

BASE_URL = "https://divulgacione14presidentet.registraduria.gov.co/home"
DESTINATION_BASE = "/media/andrea-zabala-c/ANZACA_EXT4"

async def fetch_and_save_pdf(session, url, dest_path, semaphore):
    async with semaphore:
        try:
            async with session.get(url, timeout=30) as response:
                if response.status == 200:
                    content = await response.read()
                    
                    with open(dest_path, 'wb') as f:
                        f.write(content)
                        
                    file_hash = hashlib.sha256(content).hexdigest()
                    print(f"[+] DESCARGADO y HASHED: {os.path.basename(dest_path)} -> {file_hash}")
                    return file_hash
                elif response.status == 404:
                    print(f"[-] ERROR 404: Archivo no encontrado (Posible purga oficial): {url}")
                else:
                    print(f"[-] ERROR {response.status}: Al acceder a {url}")
        except Exception as e:
            print(f"[!] EXCEPCIÓN: Falló la conexión a {url} - {str(e)}")
        return None

async def main():
    print(f"🚀 Iniciando Motor de Extracción Tycho hacia {BASE_URL}")
    print(f"💾 Destino anclado en: {DESTINATION_BASE}")
    
    semaphore = asyncio.Semaphore(15)
    
    # URL de prueba inyectada para probar conectividad al servidor
    test_urls = [
        (f"{BASE_URL}/E14_Muestra_Delegados_1.pdf", f"{DESTINATION_BASE}/MATRIZ_SEGUNDA_VUELTA/01_EVIDENCIA/DELEGADOS/E14_Muestra_Delegados_1.pdf")
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_save_pdf(session, url, dest, semaphore) for url, dest in test_urls]
        await asyncio.gather(*tasks)
        
    print("✅ Ciclo de extracción finalizado.")

if __name__ == "__main__":
    asyncio.run(main())
