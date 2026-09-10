#!/usr/bin/env python3
"""
ejecutar_orbita1_merkle.py — Procesador de la Órbita 1 (Técnica & Merkle Tree Discovery)
Genera el Árbol de Merkle SHA-256 del repositorio y descubre estructuras internas de datos
"""

import os
import sys
import hashlib
import sqlite3
import json
from datetime import datetime

def calcular_sha256(filepath):
    sha = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(65536):
                sha.update(chunk)
        return sha.hexdigest()
    except Exception as e:
        return None

def construir_merkle_root(hashes_list):
    if not hashes_list:
        return None
    current_level = sorted(hashes_list)
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            if i + 1 < len(current_level):
                combined = (current_level[i] + current_level[i+1]).encode('utf-8')
            else:
                combined = (current_level[i] + current_level[i]).encode('utf-8')
            next_level.append(hashlib.sha256(combined).hexdigest())
        current_level = next_level
    return current_level[0]

def main():
    print("📐 TYCHO, BABA YAGA & ARTHURRIOS — Procesando Órbita 1 (Técnica / Merkle Tree)...")

    repo_dir = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep"
    output_md = os.path.join(repo_dir, "02_ANALISIS", "ORBITA_1_AUDITORIA_TECNICA_MERKLE.md")

    # 1. Escaneo de Archivos y Cálculo de Hashes
    file_hashes = {}
    db_structures = []
    internal_dirs = set()

    for root, dirs, files in os.walk(repo_dir):
        # Excluir .git para el hash de evidencia del repositorio
        if ".git" in root:
            continue
        rel_root = os.path.relpath(root, repo_dir)
        if rel_root != ".":
            internal_dirs.add(rel_root.split(os.sep)[0])

        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, repo_dir)
            
            # Si es base de datos SQLite, inspeccionar estructura interna
            if file.endswith('.db') or file.endswith('.sqlite'):
                try:
                    conn = sqlite3.connect(full_path)
                    cur = conn.cursor()
                    tables = [row[0] for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
                    db_structures.append({
                        "db_path": rel_path,
                        "tables": tables,
                        "size_bytes": os.path.getsize(full_path)
                    })
                    conn.close()
                except Exception as ex:
                    pass

            file_hash = calcular_sha256(full_path)
            if file_hash:
                file_hashes[rel_path] = file_hash

    # 2. Construir el Merkle Root
    all_hashes = list(file_hashes.values())
    merkle_root = construir_merkle_root(all_hashes)

    # 3. Descubrimiento de Estructuras Internas por Módulos
    modulos_internos = {}
    for path in file_hashes:
        partes = path.split(os.sep)
        categoria = partes[0] if len(partes) > 1 else "RAÍZ"
        if categoria not in modulos_internos:
            modulos_internos[categoria] = 0
        modulos_internos[categoria] += 1

    # 4. Generar Informe de Auditoría Técnica de la Órbita 1
    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# 📐 ÓRBITA I: AUDITORÍA TÉCNICA, ÁRBOL DE MERKLE Y ESTRUCTURAS INTERNAS\n")
        f.write(f"**Fecha del Ritual:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC-4  \n")
        f.write(f"**Ejecutores:** Tycho (Silicio), Baba Yaga (Motor) y Arthurios (Integridad)  \n")
        f.write(f"**Archivos Analizados:** {len(file_hashes)}  \n\n")
        f.write("---  \n\n")

        f.write("## 🔐 1. ÁRBOL DE MERKLE Y FIRMA RAÍZ MAESTRA (MERKLE ROOT)\n\n")
        f.write(f"```text\n")
        f.write(f"MERKLE ROOT MAESTRO DE LA ÓRBITA 1:\n")
        f.write(f"SHA-256: {merkle_root}\n")
        f.write(f"```\n\n")
        f.write("> *Cualquier alteración de un solo bit en la estructura interna romperá de inmediato esta firma de Merkle.*  \n\n")
        f.write("---  \n\n")

        f.write("## 🗺️ 2. MAPEO DE ESTRUCTURAS INTERNAS DESCUBIERTAS EN EL REPOSITORIO\n\n")
        f.write("| Módulo / Estructura Interna | Archivos / Componentes | Descripción Forense |\n")
        f.write("| :--- | :--- | :--- |\n")
        for mod, count in sorted(modulos_internos.items(), key=lambda x: x[1], reverse=True):
            f.write(f"| `{mod}` | **{count} archivos** | Estructura interna de datos/código indizada. |\n")
        f.write("\n---\n\n")

        f.write("## 🗄️ 3. ESTRUCTURAS DE BASES DE DATOS SQLITE INTERNAS DESCUBIERTAS\n\n")
        if db_structures:
            for db in db_structures:
                f.write(f"### 🗃️ Base de Datos: `{db['db_path']}` ({db['size_bytes']} bytes)\n")
                f.write(f"- **Tablas Internas:** {', '.join(f'`{t}`' for t in db['tables']) if db['tables'] else 'Sin tablas'}\n\n")
        else:
            f.write("*Sin bases de datos SQLite locales detectadas en este módulo.*\n\n")

        f.write("---  \n\n")
        f.write("## 📋 4. MUESTRA REPRESENTATIVA DE HASHES SHA-256 DE ARCHIVOS CLAVE\n\n")
        for rel_path, h in list(file_hashes.items())[:30]:
            f.write(f"* [`{h[:16]}...`] `{rel_path}`\n")
        
        if len(file_hashes) > 30:
            f.write(f"\n*... y {len(file_hashes) - 30} hashes adicionales sellados en el árbol de Merkle.*  \n")

    print(f"✅ Procesamiento de la Órbita 1 completado.")
    print(f"🔐 Merkle Root Maestro: {merkle_root}")
    print(f"📄 Informe guardado en: {output_md}")

if __name__ == "__main__":
    main()
