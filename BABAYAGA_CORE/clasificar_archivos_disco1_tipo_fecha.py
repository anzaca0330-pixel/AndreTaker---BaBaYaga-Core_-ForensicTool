#!/usr/bin/env python3
"""
clasificar_archivos_disco1_tipo_fecha.py — Clasificación Granular por Tipo y Fecha (Kepler)
Analiza minuciosamente los archivos del Disco 1 ordenándolos por extensión/tipo y por línea de tiempo
"""

import os
import sys
import json
from datetime import datetime

def main():
    print("🌟 KEPLER — Ejecutando Clasificación Granular por Tipo y Fecha en Disco 1...")

    home_dir = "/home/andrea-zabala-c"
    repo_dir = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep"
    output_md = os.path.join(repo_dir, "03_DOCUMENTACION", "CLASIFICACION_GRANULAR_TIPO_FECHA_DISCO1.md")

    # Extensiones por Tipo
    tipos_ext = {
        "📄 Documentos y Textos (.md, .txt, .csv, .json)": [".md", ".txt", ".csv", ".json"],
        "🐍 Código y Scripts (.py, .sh, .js, .html, .css)": [".py", ".sh", ".js", ".html", ".css"],
        "🖼️ Evidencia Gráfica e Imágenes (.png, .jpg, .svg, .webp)": [".png", ".jpg", ".jpeg", ".svg", ".webp"],
        "🗃️ Bases de Datos y Logs (.db, .sqlite, .jsonl, .log)": [".db", ".sqlite", ".jsonl", ".log"],
        "📦 Paquetes y Binarios (.zip, .tar, .gz, .cab, .bin, .apk)": [".zip", ".tar", ".gz", ".cab", ".bin", ".apk"],
        "📑 Documentos PDF (.pdf)": [".pdf"]
    }

    conteo_por_tipo = {cat: 0 for cat in tipos_ext}
    conteo_por_tipo["Otros Formatos"] = 0

    conteo_por_fecha = {
        "🗓️ Septiembre 2026 (Auditoría BIOS / Tycho / Kepler / Matriz)": 0,
        "🗓️ Agosto 2026 (Consolidación / Exilio Montréal)": 0,
        "🗓️ Julio 2026 (Demanda CIDH / Exilio México)": 0,
        "🗓️ Junio 2026 (Ingesta Masiva / 20 Días de Asedio)": 0,
        "🗓️ Previo a Junio 2026 (Archivos Históricos / Firmware Lenovo)": 0
    }

    muestras_recientes = []
    total_archivos = 0

    # Recorrer /home/andrea-zabala-c excluyendo carpetas gigantes ruidosas (.cache, node_modules, etc.)
    excluir_dirs = {".cache", ".npm", ".nvm", "node_modules", ".git", "venv", "test_venv", ".antigravity-ide"}

    for root, dirs, files in os.walk(home_dir):
        # Excluir directorios ruidosos
        dirs[:] = [d for d in dirs if d not in excluir_dirs]

        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, home_dir)
            ext = os.path.splitext(file)[1].lower()
            
            total_archivos += 1

            # 1. Clasificación por Tipo
            tipo_encontrado = False
            for cat, ext_list in tipos_ext.items():
                if ext in ext_list:
                    conteo_por_tipo[cat] += 1
                    tipo_encontrado = True
                    break
            if not tipo_encontrado:
                conteo_por_tipo["Otros Formatos"] += 1

            # 2. Clasificación por Fecha de Modificación
            try:
                mtime = os.path.getmtime(full_path)
                dt = datetime.fromtimestamp(mtime)
                year_month = dt.strftime("%Y-%m")

                if year_month == "2026-09":
                    conteo_por_fecha["🗓️ Septiembre 2026 (Auditoría BIOS / Tycho / Kepler / Matriz)"] += 1
                elif year_month == "2026-08":
                    conteo_por_fecha["🗓️ Agosto 2026 (Consolidación / Exilio Montréal)"] += 1
                elif year_month == "2026-07":
                    conteo_por_fecha["🗓️ Julio 2026 (Demanda CIDH / Exilio México)"] += 1
                elif year_month == "2026-06":
                    conteo_por_fecha["🗓️ Junio 2026 (Ingesta Masiva / 20 Días de Asedio)"] += 1
                else:
                    conteo_por_fecha["🗓️ Previo a Junio 2026 (Archivos Históricos / Firmware Lenovo)"] += 1

                # Guardar muestra representativa de archivos recientes
                if year_month == "2026-09" and len(muestras_recientes) < 25:
                    muestras_recientes.append({
                        "path": rel_path,
                        "fecha": dt.strftime("%Y-%m-%d %H:%M:%S"),
                        "tipo": ext if ext else "sin ext"
                    })

            except Exception:
                pass

    # Generar Informe Registral Granular
    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    with open(output_md, "w", encoding="utf-8") as out:
        out.write("# 🌟 CLASIFICACIÓN GRANULAR DE ARCHIVOS POR TIPO Y FECHA — KEPLER\n")
        out.write(f"**Fecha del Ritual:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC-4  \n")
        out.write(f"**Directorio Analizado:** `/home/andrea-zabala-c` (Disco 1 NVMe)  \n")
        out.write(f"**Total de Archivos Auditados:** {total_archivos}  \n\n")
        out.write("---  \n\n")

        out.write("## 🗂️ 1. CLASIFICACIÓN POR TIPO DE ARCHIVO Y FORMATO\n\n")
        out.write("| Categoría / Formato | Archivos Hallados | Porcentaje del Total |\n")
        out.write("| :--- | :--- | :--- |\n")
        for cat, count in conteo_por_tipo.items():
            pct = (count / total_archivos * 100) if total_archivos > 0 else 0
            out.write(f"| **{cat}** | **{count} archivos** | {pct:.1f}% |\n")
        out.write("\n---\n\n")

        out.write("## 📅 2. CLASIFICACIÓN CRONOLÓGICA POR FASES DE TIEMPO (FECHA DE MODIFICACIÓN)\n\n")
        out.write("| Fase Temporal / Hito Investigativo | Archivos Creados/Modificados | Porcentaje del Total |\n")
        out.write("| :--- | :--- | :--- |\n")
        for fecha_cat, count in conteo_por_fecha.items():
            pct = (count / total_archivos * 100) if total_archivos > 0 else 0
            out.write(f"| **{fecha_cat}** | **{count} archivos** | {pct:.1f}% |\n")
        out.write("\n---\n\n")

        out.write("## 🔍 3. MUESTRA REPRESENTATIVA DE ARCHIVOS GENERADOS EN SEPTIEMBRE DE 2026\n\n")
        out.write("| Archivo / Ruta Relativa | Fecha y Hora Exacta | Formato |\n")
        out.write("| :--- | :--- | :--- |\n")
        for item in muestras_recientes:
            out.write(f"| `{item['path']}` | `{item['fecha']}` | `{item['tipo']}` |\n")

        out.write("\n---\n\n")
        out.write("## 📜 VEREDICTO DE CLASIFICACIÓN GRANULAR DE KEPLER\n\n")
        out.write(f"Se han analizado y clasificado **{total_archivos} archivos** del Disco 1 en mapas de tipo y líneas de tiempo cronológicas. Toda la evolución histórica del proyecto está trazada y sellada.\n")

    print(f"✅ Clasificación granular completada.")
    print(f"📄 Documento registrado en: {output_md}")

if __name__ == "__main__":
    main()
