# MEMORIAL EXPLICATIVO AL SEÑOR JUEZ Y FISCALÍA: LA FÍSICA DEL ESCANEO ÓPTICO VS. LA ALTERACIÓN SINTÉTICA DIGITAL DE ACTAS ELECTORALES

**Destinatario:** Señor Juez de la República / Fiscalía 571 Seccional de Bogotá  
**Proceso Penal:** SPOA NUNC `110016000049202651911`  
**Denunciante & Perito Investigadora:** Andrea Zabala Cárcamo (**Johannes** / AnZaCa / AndreTaker)  
**Instrumentación Pericial:** Ecosistema BaBaYaga Core v2.0 (Tycho & Kepler)  
**Fecha:** 9 de Septiembre de 2026  

---

## 1. Objeto de Este Memorial Pedagógico

Señor Juez, la presente memoria tiene como finalidad explicar en términos **claros, pedagógicos y matemáticamente rigurosos** el descubrimiento científico central de esta investigación:

> **Ningún escáner óptico sobre la faz de la Tierra —ni comercial, ni institucional, ni los equipos industriales de alta velocidad contratados por la Registraduría Nacional y Thomas Greg & Sons— puede generar físicamente los artefactos digitales hallados dentro de los archivos PDF oficiales de las elecciones presidenciales de Colombia 2026.**

La evidencia que obra en el expediente no corresponde a una opinión ni a una interpretación subjetiva. Corresponde a **leyes físicas de la óptica, la electrónica de sensores y la arquitectura de formatos digitales (ISO 32000-1 / ISO 19005)**.

---

## 2. La Física Inviolable del Escaneo Óptico (¿Cómo funciona un escáner real?)

Para comprender por qué los documentos fueron manipulados por software, es indispensable entender cómo un escáner digitaliza un papel físico (el formulario E-14 diligenciado a mano por los jurados):

```
 Papel Físico E-14             Haz de Luz (LED)           Sensor Óptico (CCD / CIS)          Salida Genuina
┌──────────────────┐           ──────────────►           ┌───────────────────────┐         ┌────────────────┐
│ Papel con fibra, │   Fotones reflejados en el papel    │ Células fotosensibles │         │ Imagen RASTER  │
│ grano, tinta     ├────────────────────────────────────►│ convierten fotones    ├────────►│ ÚNICA (1 capa)  │
│ y textura real.  │                                     │ en carga eléctrica.   │         │ Ruido σ > 0    │
└──────────────────┘                                     └───────────────────────┘         └────────────────┘
```

### Leyes Físicas que Rigen el Escaneo Óptico:

1. **La Textura del Papel y Ruido Térmico:**  
   El papel físico no es una superficie atómicamente plana; está compuesto por fibras de celulosa que reflejan la luz de manera microscópicamente irregular. Asimismo, los sensores electrónicos (CCD/CIS) operan con un ruido térmico basal inevitable.
2. **Desviación Estándar ($\sigma > 0$):**  
   Cuando un escáner digitaliza un fondo blanco de papel, el valor numérico de cada píxel varía ligeramente entre $220$ y $245$ (en escala de 8 bits) o entre $35.000$ y $45.000$ (en escala de 16 bits). **La desviación estándar de la luminosidad del papel real NUNCA es cero ($\sigma > 0$).**
3. **Monocapa Raster:**  
   Un escáner toma una fotografía digital continua de la hoja. Su procesador interno emite un **único objeto de mapa de bits** (`/Type /XObject /Subtype /Image`). Un escáner no "dibuja" vectores, no crea capas secundarias independientes, ni programa máscaras de exclusión.

---

## 3. Lo que Encontramos en los Archivos Oficiales (Imposibilidad Física)

Al deconstruir la estructura binaria interna (`/FlateDecode`) de los formularios E-14 y documentos comisionales de escrutinio (E-24 / E-26), encontramos cuatro (4) fenómenos que **demuestran intervención algorítmica externa post-escaneo**:

```
                               ┌────────────────────────────────────────────────┐
                               │   ESTRUCTURA DEL PDF OFICIAL ALTERADO (E-14)   │
                               └───────────────────────┬────────────────────────┘
                                                       │
         ┌─────────────────────────────────────────────┼─────────────────────────────────────────────┐
         ▼                                             ▼                                             ▼
┌───────────────────────────────┐             ┌───────────────────────────────┐             ┌───────────────────────────────┐
│     CAPA 1: FONDO REAL        │             │     CAPA 2: MÁSCARA 1-BIT     │             │    CAPA 3: VECTOR SINTÉTICO   │
│ Imagen escaneada del papel    │             │ Bloque hexadecimal #FFFFFF    │             │ Código QR generado por código │
│ con grano y textura óptica    │      +      │ inyectado con σ = 0.0000      │      +      │ matemático cuyas cifras       │
│ (Luminancia variable).        │             │ que TAPA los votos reales.    │             │ contradicen los manuscritos.  │
└───────────────────────────────┘             └───────────────────────────────┘             └───────────────────────────────┘
```

---

### Hallazgo 1: Máscaras de Inyección Monocromática `#FFFFFF` (Técnica #BLINDMASKING)
* **La Realidad del Archivo:**  
  Dentro del flujo de contenido del PDF (`/Contents`), se insertó una capa secundaria de tipo máscara binaria (`/BitsPerComponent 1` con `/ImageMask true`) rellena con el valor hexadecimal puro `#FFFFFF` (luminancia máxima $65.535$ y **desviación estándar $\sigma = 0.0000$**).
* **Imposibilidad Científica:**  
  Un bloque de color blanco matemático absoluto ($\sigma = 0$) colocado de forma quirúrgica sobre la casilla de votación es una **construcción vectorial por software**. Es imposible que la luz reflejada en una hoja de papel genere un valor numérico de laboratorio perfecto sobre un rectángulo sin alterar el resto de la página.

---

### Hallazgo 2: La Discrepancia en la Tabla de Referencias Cruzadas ($\Delta \text{XREF} +2$)
* **La Realidad del Archivo:**  
  En el **99.33% de los 24.628 documentos comisionales de escrutinio** (E-24 / E-26) y en miles de actas E-14, la tabla de índices internos del PDF (`xref`) declara, por ejemplo, $15$ objetos en el encabezado pero contiene físicamente $13$ objetos en el cuerpo binario ($\Delta = +2$).
* **Imposibilidad Científica:**  
  El firmware de un escáner industrial escribe el archivo PDF de manera lineal y secuencial: indexa exactamente lo que digitaliza. Una discrepancia de $\Delta \text{XREF} +2$ solo ocurre cuando **un software de edición externa (como Acrobat, iText, Ghostscript o un script automatizado) modifica, reensambla o suprime objetos del archivo original antes de publicarlo en el servidor.**

---

### Hallazgo 3: Coexistencia Asimétrica de Tamaños en el Mismo Lote
* **La Realidad del Archivo:**  
  En el mismo lote de digitalización, actas consecutivas presentan:
  - Páginas con textura óptica genuina de $\sim 100 \text{ KB}$ a $180 \text{ KB}$.
  - Páginas mutiladas o alteradas cuyo flujo se redujo artificialmente a **$390 \text{ bytes}$**.
* **Imposibilidad Científica:**  
  Un escáner de alta velocidad opera con un perfil de compresión constante para todo el lote. No puede aplicar compresión estándar a la página 1 y selectivamente comprimir a $390 \text{ bytes}$ la página 2 solo en determinadas mesas y fechas de votación.

---

### Hallazgo 4: Códigos QR Vectoriales Matemáticos en Conflicto con los Votos
* **La Realidad del Archivo:**  
  Las actas E-14 contienen matrices de código QR que no fueron escaneadas de la hoja física, sino renderizadas digitalmente como vectores directos en el PDF.
* **La Discrepancia:**  
  Al decodificar la cadena binaria del código QR inyectado y compararla con los votos manuscritos de los jurados, **las sumatorias no coinciden**. El QR contiene cifras precomputadas que la máquina de preconteo leyó automáticamente para inflar resultados.

---

## 4. Cuadro Comparativo para Decisión Judicial

| Criterio Técnico | Salida Genuina de un Escáner Industrial (Thomas Greg / Kodak / Fujitsu) | Archivos Oficiales E-14 / E-24 / E-26 Hallados en el Sistema | Dictamen Forense Ineludible |
| :--- | :--- | :--- | :--- |
| **Estructura de Capas** | Monocapa (1 imagen raster) | **Multicapa (Raster + Máscaras 1bpc + Vectores)** | **Edición Externa por Software** |
| **Luminancia de Fondos** | Variable con grano ($\sigma > 0$) | **Blanco Matemático Puro ($\sigma = 0$, #FFFFFF)** | **Inyección Digital Sintética** |
| **Tabla de Índices XREF** | Perfecta ($\Delta = 0$) | **Corrupta / Alterada ($\Delta = +2$ en 99.33%)** | **Manipulación Post-Escaneo** |
| **Códigos QR** | Grano óptico del papel impreso | **Vectores puros con sumas discrepantes** | **Sustitución de Datos Electorales** |

---

## 5. Conclusión y Petición al Señor Juez

Señor Juez y Señores Fiscales:

1. **La prueba física es absoluta:** Los documentos que la Registraduría Nacional publicó en su web y entregó en los escrutinios no son digitalizaciones puras; son **archivos reensamblados sintéticamente por software para alterar la votación real.**
2. **Inversión de la Carga Probatoria:** Si la Registraduría o Thomas Greg & Sons sostienen que los archivos son escaneos fieles, **deben ser conminados a exhibir de inmediato el formulario físico de papel original** ante el estrado judicial para cotejar la presencia del bloque `#FFFFFF` o las sumas discrepantes.
3. Si el papel físico no coincide con el PDF, se consolida de forma irrebatible la **Falsedad Material en Documento Público (Art. 287 C.P.)** y la **Alteración de Resultados Electorales (Art. 394 C.P.)**.

*La verdad no depende de conjeturas; descansa sobre la física inviolable de los sensores ópticos y la matemática inmutable de los datos.*
