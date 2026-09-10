#!/usr/bin/env python3
"""
extraer_registros_ordenes.py — Extractor y Analizador Temático de Órdenes de BaBaYaga / Tycho
Parsea las 3.626+ órdenes históricas y genera un Índice de Registros Clave por Categorías Forenses
"""

import os
import re
import glob
import json
from datetime import datetime

def main():
    print("🔭  TYCHO & 🧙‍♀️ BABAYAGA — Navegando el Mar de Órdenes...")

    brain_dir = "/home/andrea-zabala-c/.gemini/antigravity-ide/brain"
    output_md = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/03_DOCUMENTACION/INDICE_REGISTROS_CLAVE_ORDENES.md"

    files = glob.glob(os.path.join(brain_dir, "*", ".system_generated", "logs", "transcript.jsonl"))

    categorias = {
        "🛡️ Ciberseguridad, BIOS y Hardware": [
            r"bios", r"nvram", r"efibootmgr", r"lenovo", r"thinkshield", r"pxe", r"rootkit", 
            r"hardware", r"ip", r"takeout", r"firmware", r"purgar", r"escudo", r"aislamiento", r"port"
        ],
        "📊 Análisis Forense E-14, XREF y Benford": [
            r"e14", r"xref", r"benford", r"mebane", r"xobject", r"máscara", r"1bpc", r"vector", 
            r"amazonas", r"putumayo", r"acacias", r"outlier", r"varianza", r"boletín", r"preconteo", r"acta"
        ],
        "📜 Entregables Legales y Cadena de Custodia": [
            r"cidh", r"iachr", r"medida", r"cautelar", r"demanda", r"sha-256", r"hash", r"custodia", 
            r"testigo", r"exilio", r"canadá", r"méxico", r"pericial", r"declaración"
        ],
        "⚙️ Desarrollo, Scripts y Módulos": [
            r"babayaga", r"tycho", r"andretaker", r"script", r"python", r"test", r"run_tests", 
            r"github", r"workflow", r"apk", r"dashboard", r"bot", r"código"
        ],
        "📂 Bóvedas y Sacrificio de Almacenamiento": [
            r"data1", r"anzaca", r"bóveda", r"papelera", r"disco", r"gigabyte", r"gb", r"música", r"espacio"
        ]
    }

    records_by_cat = {cat: [] for cat in categorias}
    total_parsed = 0

    for f in files:
        conv_id = f.split(os.sep)[-4]
        try:
            with open(f, "r", encoding="utf-8") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        if data.get("type") == "USER_INPUT":
                            raw_content = data.get("content", "")
                            # Extraer solo la petición entre <USER_REQUEST> ... </USER_REQUEST>
                            match_req = re.search(r"<USER_REQUEST>(.*?)</USER_REQUEST>", raw_content, re.DOTALL)
                            clean_text = match_req.group(1).strip() if match_req else raw_content.strip()

                            # Eliminar metadatos sobrantes
                            clean_text = re.sub(r"<[^>]+>.*?</[^>]+>", "", clean_text, flags=re.DOTALL).strip()
                            clean_text = re.sub(r"\s+", " ", clean_text)

                            if not clean_text or len(clean_text) < 4:
                                continue

                            total_parsed += 1
                            step = data.get("step_index", 0)
                            text_lower = clean_text.lower()

                            for cat, patterns in categorias.items():
                                if any(re.search(p, text_lower) for p in patterns):
                                    records_by_cat[cat].append({
                                        "conv": conv_id[:8],
                                        "step": step,
                                        "text": clean_text[:160] + ("..." if len(clean_text) > 160 else "")
                                    })
                    except Exception:
                        pass
        except Exception:
            pass

    # Escribir archivo final
    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    with open(output_md, "w", encoding="utf-8") as out:
        out.write("# 🧭 ÍNDICE DE REGISTROS Y ÓRDENES CLAVE DEL REPOSITORIO\n")
        out.write(f"**Fecha del Ritual:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
        out.write(f"**Total de Órdenes Analizadas:** {total_parsed}  \n\n")
        out.write("---  \n\n")

        for cat, items in records_by_cat.items():
            out.write(f"## {cat} ({len(items)} registros hallados)\n\n")
            if not items:
                out.write("*Sin registros destacados.*\n\n")
                continue

            for item in items[:40]:
                out.write(f"* [`conv-{item['conv']}` | Paso {item['step']}] {item['text']}\n")

            if len(items) > 40:
                out.write(f"\n*... y {len(items) - 40} registros adicionales archivados en la memoria profunda.*\n")
            out.write("\n---\n\n")

    print(f"✅ Extracción completada.")
    print(f"📊 {total_parsed} órdenes procesadas.")
    print(f"📄 Índices temáticos generados en: {output_md}")

if __name__ == "__main__":
    main()
