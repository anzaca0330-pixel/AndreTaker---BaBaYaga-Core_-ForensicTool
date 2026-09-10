# ⚡ REPORTE DE METROLOGÍA Y RENDIMIENTO COMPUTACIONAL
### Motor Forense: BaBaYaga Core v2.0 / Tycho Metrology Engine
**Investigadora Principal:** Andrea Zabala Cárcamo (Johannes / AnZaCa)  
**Fecha de Benchmark:** 2026-09-09 23:16:45 UTC  
**Hardware Host:** Estación Forense Linux (Kernel multiproceso)  
**Entorno de Datos:** Disco Externo `/media/andrea-zabala-c/D A T A1/`  

---

## 🚀 1. TELEMETRÍA DE RENDIMIENTO GLOBAL

| Métrica Forense | Valor Registrado | Unidad de Medida |
| :--- | :--- | :--- |
| **Archivos Auditados en Lote** | **`100`** | Actas Oficiales de 1ª Vuelta |
| **Volumen de Datos Crudos** | **`2477.15`** | Megabytes (MB) |
| **Tiempo Total de Ejecución** | **`40.308`** | Segundos |
| **Latencia Promedio por Acta** | **`403.08`** | **Milisegundos (ms / acta)** |
| **Throughput de Ingestión** | **`2.48`** | **Actas / Segundo (FPS)** |
| **Throughput de Ancho de Banda** | **`61.46`** | **MB / Segundo** |

---

## 🔬 2. DESGLOSE METROLÓGICO POR MICRO-OPERACIÓN FORENSE

1. **Cálculo Criptográfico SHA-256 (Inmutabilidad):** Promedio de `385.88 ms` por archivo.
2. **Inspección Raster de Tablas `/XObject` (pdfimages):** Promedio de `16.66 ms` por archivo.
3. **Escaneo de Cabecera Binaria y Deltas XREF:** Promedio de `0.48 ms` por archivo.

---

## 📋 3. MUESTRA DE LAS PRIMERAS 10 ACTAS PROCESADAS

| Archivo | Tamaño (KB) | Hash SHA-256 (Truncado) | Hash (ms) | Raster (ms) | Binario (ms) | **Total (ms)** | Imgs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AGE_XXX_07_142_XXX_XX_XX_XXX_2246.pdf` | 14267.29 | `2c2c1eb1210e6ffe...` | 56.956 | 13.599 | 1.762 | **72.346** | 9 |
| `AGE_XXX_15_163_XXX_XX_XX_XXX_2497.pdf` | 15387.99 | `b48b5ff538d6375f...` | 262.554 | 17.872 | 0.802 | **281.372** | 9 |
| `AGE_XXX_29_112_XXX_XX_XX_XXX_2941.pdf` | 23857.98 | `f2d7583f81d98261...` | 106.145 | 16.033 | 0.759 | **122.973** | 13 |
| `AGE_XXX_29_115_XXX_XX_XX_XXX_2942.pdf` | 19469.04 | `e41d7bcce587e840...` | 89.428 | 17.832 | 0.663 | **107.947** | 12 |
| `AGE_XXX_29_118_XXX_XX_XX_XXX_2943.pdf` | 16934.6 | `6a84edcc192ae73a...` | 78.131 | 17.548 | 0.446 | **96.148** | 11 |
| `AGE_XXX_29_121_XXX_XX_XX_XXX_2944.pdf` | 38457.2 | `f33b89c557d72759...` | 186.664 | 18.231 | 0.468 | **205.385** | 23 |
| `AGE_XXX_29_124_XXX_XX_XX_XXX_2945.pdf` | 23497.98 | `5349ccd0cd65ca6d...` | 113.818 | 18.071 | 0.499 | **132.414** | 14 |
| `AGE_XXX_29_127_XXX_XX_XX_XXX_2946.pdf` | 20529.78 | `e7a1df6014d777da...` | 132.412 | 22.962 | 0.815 | **156.222** | 12 |
| `AGE_XXX_31_XXX_XXX_XX_XX_XXX_1020.pdf` | 179598.28 | `71f301a9ee86a2b4...` | 2917.946 | 71.672 | 0.503 | **2990.167** | 756 |
| `AGE_XXX_31_004_XXX_XX_XX_XXX_2948.pdf` | 33091.99 | `e689b1d442dfab79...` | 168.892 | 19.588 | 0.99 | **189.499** | 19 |
| `AGE_XXX_31_010_XXX_XX_XX_XXX_2950.pdf` | 6142.49 | `951493130b61ae89...` | 30.29 | 138.5 | 0.769 | **169.595** | 0 |
| `AGE_XXX_31_013_XXX_XX_XX_XXX_2951.pdf` | 21695.55 | `f6b2665407c8f0d9...` | 117.613 | 20.29 | 0.532 | **138.462** | 14 |
| `AGE_XXX_31_016_XXX_XX_XX_XXX_2952.pdf` | 40493.45 | `c71d5283bdae2e33...` | 214.538 | 19.154 | 0.492 | **234.21** | 22 |
| `AGE_XXX_31_019_XXX_XX_XX_XXX_2953.pdf` | 41945.71 | `fd9d94e73b64018d...` | 214.21 | 20.959 | 0.511 | **235.704** | 49 |
| `AGE_XXX_31_022_XXX_XX_XX_XXX_2954.pdf` | 8415.95 | `44e29b2801da6f2f...` | 43.251 | 18.576 | 0.498 | **62.348** | 6 |

---

## 🏛️ 4. BALANCE METROLÓGICO CONSOLIDADO DEL ACERVO TOTAL (AL DÍA DE HOY)

| Cuadrante / Repositorio | Total Archivos | Volumen en Bytes | Volumen (GiB) |
| :--- | :---: | :---: | :---: |
| **Bóveda Externa (`D A T A1`)** (Comisiones, E-24/26, AGE, E-14 Claveros) | **515.961** | `698.480.876.935` | **650,51 GiB** |
| **Bóveda Local (`Desktop`)** (Preconteo 123k actas, Expediente FGN 571, Takeout) | **210.699** | `70.706.134.801` | **65,85 GiB** |
| **Motor Forense (`BaBaYaga-Core`)** (Scripts, XREF, Benford, SQLite) | **2.726** | `1.331.553.998` | **1,24 GiB** |
| **Repositorio Institucional (`AnZaCa-Rep`)** (Expedientes, Memoriales, v1.0-v3.0) | **7.178** | `1.792.243.558` | **1,67 GiB** |
| **TOTAL METROLÓGICO DIRECTO ACTIVO** | **`736.564`** | **`772.310.809.292`** | **`719,27 GiB`** |
*(Acervo global histórico consolidado >777.869 archivos bajo sello SHA-256).*

