#!/usr/bin/env python3
"""
⚡ BABAYAGA CORE — MOTOR FORENSE EN VIVO (LIVE BENCHMARK & METROLOGY RUNNER)
Ecosistema Pericial AndreTaker / BaBaYaga Core
Permite a cualquier perito, auditor o tribunal ejecutar pruebas de rendimiento y análisis en tiempo real.
"""

import os
import sys
import time
import hashlib
import subprocess
import glob
from datetime import datetime, timezone

# ANSI Colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner():
    print(f"\n{CYAN}{BOLD}" + "="*75)
    print("⚡ BABAYAGA CORE v2.0 — TEST METROLÓGICO Y BENCHMARK EN VIVO")
    print("🔬 Laboratorio Independiente de Ciberforense Electoral — AndreTaker")
    print("="*75 + f"{RESET}\n")

def run_live_benchmark():
    print_banner()
    
    # Locate sample files
    sample_dirs = [
        "/media/andrea-zabala-c/D A T A1/01_EVIDENCIA/DESCARGAS_MASIVAS_REGISTRADURIA/PRIMERA_VUELTA/DOCUMENTOS_COMISIONES",
        os.path.join(os.path.dirname(__file__), "../00_MUESTRAS_EVIDENCIA"),
        os.path.join(os.path.dirname(__file__), "demo"),
        os.path.expanduser("~/Desktop/ENTREGABLES_FORENSES_E14")
    ]
    
    pdfs = []
    for s_dir in sample_dirs:
        if os.path.exists(s_dir):
            for root, _, files in os.walk(s_dir):
                for f in files:
                    if f.lower().endswith('.pdf'):
                        pdfs.append(os.path.join(root, f))
                        if len(pdfs) >= 50:
                            break
                if len(pdfs) >= 50:
                    break
        if len(pdfs) >= 50:
            break

    if not pdfs:
        print(f"{RED}❌ No se encontraron archivos PDF de muestra para ejecutar el benchmark.{RESET}")
        return

    total_files = len(pdfs)
    print(f"📦 {BOLD}Lote de Prueba Detectado:{RESET} {total_files} actas oficiales.")
    print(f"🚀 {YELLOW}Iniciando disección en tiempo real (Hashing SHA-256 + Raster XObject + Binario XREF)...{RESET}\n")

    results = []
    start_global = time.perf_counter()
    total_bytes = 0

    for idx, pdf in enumerate(pdfs, 1):
        t0 = time.perf_counter()
        
        # 1. Size
        sz = os.path.getsize(pdf)
        total_bytes += sz
        
        # 2. SHA-256
        t_h0 = time.perf_counter()
        h = hashlib.sha256()
        with open(pdf, 'rb') as f:
            while chunk := f.read(65536):
                h.update(chunk)
        sha_val = h.hexdigest()
        t_hash = (time.perf_counter() - t_h0) * 1000
        
        # 3. Raster inspection
        t_r0 = time.perf_counter()
        proc = subprocess.run(['pdfimages', '-list', pdf], capture_output=True, text=True)
        img_lines = [l for l in proc.stdout.splitlines() if len(l.strip()) > 0]
        img_cnt = max(0, len(img_lines) - 2)
        t_raster = (time.perf_counter() - t_r0) * 1000
        
        # 4. Binary check
        t_b0 = time.perf_counter()
        with open(pdf, 'rb') as f:
            head = f.read(1024 * 256)
        has_xo = b'/XObject' in head
        has_flate = b'/FlateDecode' in head
        t_bin = (time.perf_counter() - t_b0) * 1000
        
        t_total = (time.perf_counter() - t0) * 1000
        
        results.append({
            'name': os.path.basename(pdf),
            'size_kb': sz / 1024,
            'sha256': sha_val,
            't_hash': t_hash,
            't_raster': t_raster,
            't_bin': t_bin,
            't_total': t_total,
            'imgs': img_cnt
        })
        
        bar = "█" * int(idx / total_files * 30) + "-" * (30 - int(idx / total_files * 30))
        print(f"\r  [{bar}] {idx}/{total_files} | {t_total:.1f} ms/acta | {os.path.basename(pdf)[:25]}...", end='', flush=True)

    end_global = time.perf_counter()
    total_time = end_global - start_global
    total_mb = total_bytes / (1024 * 1024)
    avg_ms = (total_time / total_files) * 1000
    fps = total_files / total_time
    mb_s = total_mb / total_time

    print("\n\n" + f"{GREEN}{BOLD}" + "="*75)
    print("🏁 BENCHMARK COMPLETADO CON ÉXITO")
    print("="*75 + f"{RESET}")
    print(f"  📊 {BOLD}Total Archivos Procesados:{RESET} {total_files}")
    print(f"  💾 {BOLD}Volumen Total Ingerido:{RESET}   {total_mb:.2f} MB ({total_bytes:,} bytes)")
    print(f"  ⏱️  {BOLD}Tiempo Total de Ejecución:{RESET} {total_time:.3f} segundos")
    print(f"  ⚡ {BOLD}Latencia Promedio por Acta:{RESET} {CYAN}{avg_ms:.2f} ms / acta{RESET}")
    print(f"  🔥 {BOLD}Velocidad de Ingesta:{RESET}       {GREEN}{fps:.2f} actas / seg{RESET}")
    print(f"  🚀 {BOLD}Tasa de Transferencia:{RESET}     {YELLOW}{mb_s:.2f} MB / seg{RESET}")
    print("="*75 + "\n")

if __name__ == "__main__":
    run_live_benchmark()
