# ACTA DE CADENA DE CUSTODIA Y CUARENTENA FORENSE (ISO/IEC 27037:2012)
## EVIDENCIA DIGITAL: REGISTRO DE ARRANQUE Y TABLA DE PARTICIONES (JULIO 2026)

**Referencia de Caso:** Medida Cautelar CIDH `IACHR-0000113728`  
**Identificador de Evidencia:** `EVD-FIRMWARE-20260715-1421`  
**Estado Procesal:** En Cuarentena e Inmutable (Solo Lectura)  
**Custodio Principal:** Andrea Zabala Cárcamo (AnZaCa)  
**Asistente Forense:** Tycho & BaBaYaga Core  
**Fecha de Entrada a Cuarentena:** 2 de Septiembre de 2026 (18:16 EDT)  

---

### 1. FICHA TÉCNICA DEL ARTEFACTO

* **Nombre del Archivo:** `backup_20260715_1421.zip`
* **Tamaño Físico:** `421.673 Bytes` (Comprimido) / `3.451.822 Bytes` (24 elementos expandidos).
* **Firma Criptográfica SHA-256:**
  ```text
  ba3d8cd94424d68282240b506ef411a48c18f3b857fd90112fac9d0d85b4dd1f
  ```
* **Medio Físico de Extracción Original:** Partición de rescate NVMe SSD (`/dev/nvme0n1p4`, UUID `cf0d3b16-a0d4-4869-a918-228c96229e08`).
* **Marcas de Tiempo Certificadas (*Timestamps*):**
  * **Creación en Sistema (*Birth*):** `2026-07-15 17:23:39.204352438 -04:00`
  * **Última Modificación (*Modify*):** `2026-07-15 17:23:39.272349829 -04:00`
  * **Sesiones Internas de Boot-Repair:** `2026-07-15 09:24:39` y `2026-07-15 14:21:51`.

---

### 2. RELEVANCIA JURÍDICO-FORENSE Y CONTEXTO HISTÓRICO

Este paquete constituye prueba documental y material inmutable de:
1. **Estancia y Fechas de Rescate:** Certifica pericialmente las maniobras de recuperación del equipo de cómputo durante la estancia de emergencia en Ciudad de México (residencia de la Embajada de Colombia) en fecha **15 de julio de 2026**.
2. **Registro de Inyecciones de Firmware:** En la bitácora `boot-repair.log` queda constancia fehaciente de las entradas de secuestro remoto y alteración de arranque presentes antes de su mitigación:
   * `Boot0021* LENOVO CLOUD Uri(https://download.lenovo.com/pccbbs/cdeploy/efi/boot.efi)`
   * `Boot0015  ThinkShield secure wipe`
   * `Boot0018  MEBx Hot Key`
   * `Boot0020* PXE BOOT`
3. **Imágenes de Particionado y MBR:** Resguarda el estado exacto del sector maestro de arranque (`current_mbr.img`) y de la tabla de particiones GPT (`partition_table.dmp`).

---

### 3. PROTOCOLO DE CUARENTENA Y PRESERVACIÓN MULTISOPORTE

En cumplimiento de la norma **ISO/IEC 27037 (Principios de Adquisición y Preservación Digital)** y de la regla de autodefensa distribuida:
1. **Permisos de Inmutabilidad:** El archivo ha sido sellado con atributos de solo lectura (`chmod 444`).
2. **Copia Espejo de Respaldo Externa:**
   * Almacenamiento local: `01_EVIDENCIA/SESION_04_CUARENTENA_FIRMWARE_Y_ARRANQUE/`
   * Almacenamiento externo físico: `/media/andrea-zabala-c/BACKUP/01_EVIDENCIA/SESION_04_CUARENTENA_FIRMWARE_Y_ARRANQUE/`
3. **Verificación de Hash Periódica:** Cada transferencia fue contrastada contra su hash original `ba3d8cd9...` garantizando cero alteraciones.
