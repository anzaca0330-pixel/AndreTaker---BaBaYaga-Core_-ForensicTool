# 🧬 MAPEO SECUENCIAL Y GENEALOGÍA DE CLUSTERS DE CÓDIGOS QR CLONADOS
### Caso Fiscalía General de la Nación — SPOA: `110016000049202651911`
**Entidad Investigadora:** AndreTaker / BaBaYaga Core Forensic Unit (Johannes & Tycho)  
**Fecha de Emisión:** 2026-09-09  
**Archivo Fuente:** `MATRIZ_SECUENCIAS_QR_CLONADOS.csv`  

---

## 🌌 1. RESUMEN DEL MAPEO DETERMINISTA

A través del análisis sistemático de decodificación óptica y cruce de cadenas alfanuméricas base64 de los códigos QR incrustados en los formularios E-14, se ha identificado la existencia de **291 clusters de clonación artificial**.

Cada cluster representa una **misma cadena criptográfica o identificador vectorial duplicado entre múltiples actas y puestos de votación**, rompiendo el principio de unicidad electoral.

---

## 📊 2. TOPOLOGÍA DE LOS PRINCIPALES CLUSTERS DE CLONACIÓN

| Cluster | Cadena QR (Firma Base64 Truncada) | Repeticiones | Secuencia de Replicación / Mesas Afectadas |
| :---: | :--- | :---: | :--- |
| **CLUSTER_001** | `x7zgUrMhb7GTkUcjnzOMrDWVoBr6Bqm+fyzt9ua5...` | **4** | Mesa 81 (V-1), Mesa 81 (V-0), Mesa 81 (V-2), Mesa 81 Estructura |
| **CLUSTER_002** | `LMTS530rCcaX8gjtp/wYIGalhJr7Yvd7o/oae5rQ...` | **3** | Mesa 06 (Copia 1), Mesa 06 (Copia 2), Mesa 06 Estructura |
| **CLUSTER_003** | `ux3QZ9E2QuqvL6dkGX43uCpMqoo6AImyuOL5CY3q...` | **2** | Consulado Ext (00) Mesa 001 $\rightarrow$ IE Julio Restrepo Mesa 1 |
| **CLUSTER_004** | `K0rujer49yfQnFSyYsL2NQqp20hj7GG7HEwhJ5u/...` | **2** | Consulado Ext (00) Mesa 002 $\rightarrow$ IE Julio Restrepo Mesa 2 |
| **CLUSTER_005** | `2PC+jxQ9diATzwmhEQ6JahQ/1ocOjzHgRV9XFSAS...` | **2** | Consulado Ext (00) Mesa 003 $\rightarrow$ IE Julio Restrepo Mesa 3 |
| **CLUSTER_006** | `d5X1mvgub4pP79Fv0c7gd+jwu51nF244Oc6pNlTy...` | **2** | Consulado Ext (00) Mesa 004 $\rightarrow$ IE Julio Restrepo Mesa 4 |
| **CLUSTER_007** | `wGo8lXljOA9JSu0anQfDljCQTE/+9kDEw69NzKr/...` | **2** | Consulado Ext (00) Mesa 005 $\rightarrow$ IE Julio Restrepo Mesa 5 |
| **CLUSTER_008** | `HtuW6LpNDbRv8/nAPsuQHFm5/rCUhbvlq3J2QMLU...` | **2** | Consulado Ext (00) Mesa 006 $\rightarrow$ IE Julio Restrepo Mesa 6 |

---

## 🔬 3. PATRÓN DE CLONACIÓN IDENTIFICADO (LA "SECUENCIA EN CASCADA")

El rastreo secuencial demuestra que la clonación sigue dos patrones algorítmicos bien definidos:

1. **Replicación Intra-Puesto (Múltiples Versiones de la Misma Mesa):**
   * El software inyecta el mismo código QR en sucesivas versiones (`v1`, `v2`, `estructura`) generadas con segundos de diferencia, a pesar de que los votos consignados en el PDF sufren alteraciones.
2. **Replicación Inter-Puesto (Salto Cruzado Exterior $\leftrightarrow$ Nacional):**
   * El código QR generado para puestos consulares en el exterior fue reinyectado de manera idéntica en puestos nacionales (e.g. *Consulado Exterior $\rightarrow$ Puesto IE Julio Restrepo*), evidenciando la reutilización de secuencias sintéticas precompiladas.

---

## 📁 4. UBICACIÓN DE LA MATRIZ CRUDA Y RESPALDO

* **Matriz CSV de Secuencias Completas:**  
  [MATRIZ_SECUENCIAS_QR_CLONADOS.csv](file:///home/andrea-zabala-c/Desktop/PAQUETE_CSVS_Y_HASHES_SHA256_DRIVE/03_MATRICES_BABAYAGA_Y_CONSULADOS/MATRIZ_SECUENCIAS_QR_CLONADOS.csv)
