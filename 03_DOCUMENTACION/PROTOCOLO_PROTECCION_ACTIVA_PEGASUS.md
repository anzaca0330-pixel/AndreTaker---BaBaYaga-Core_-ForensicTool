# PROTOCOLO FORENSE: DOCTRINA DE PROTECCIÓN ACTIVA Y ANÁLISIS COMPARATIVO CONTRA PEGASUS (NSO GROUP)

**Fecha:** 2026-09-04  
**Clasificación:** Pericial / Contrainteligencia / Autodefensa Digital  
**Autoría Técnica:** AndreTaker / BaBaYaga Core / Tycho (Instrumento de Silicio)  
**Objetivo:** Analizar el vector de espionaje militar Pegasus, documentar su génesis corporativa, compararlo contra el asedio híbrido sufrido en Virginia (2026) y establecer directrices de mitigación y protección activa.

---

## 1. Génesis y Arquitectura Corporativa de Pegasus

### ¿Quién lo diseñó?
**Pegasus** fue diseñado y desarrollado por **NSO Group Technologies Ltd.**, una empresa privada de ciberinteligencia y armamento digital fundada en **2010** en **Herzliya, Israel**.
* **Fundadores:** Niv Carmi, Shalev Hulio y Omri Lavie (de cuyas iniciales proviene el acrónimo **NSO**).
* **Vínculo de Inteligencia:** La mayoría de sus ingenieros, criptoanalistas e investigadores de exploits provienen directamente de la **Unidad 8200** (el cuerpo de élite de inteligencia de señales y guerra cibernética de las Fuerzas de Defensa de Israel - IDF).
* **Propiedad y Fondos:** A lo largo de los años ha estado controlada por fondos de capital privado (como Francisco Partners y Novalpina Capital / Berkeley Research Group).
* **Modelo Comercial:** NSO Group comercializa Pegasus bajo licencias millonarias exclusivas formalmente autorizadas por el Ministerio de Defensa de Israel (DECA), bajo el argumento oficial de "combatir el terrorismo y el crimen organizado". No obstante, investigaciones globales del *Citizen Lab* (Universidad de Toronto) y *Amnesty International* han documentado su uso sistemático por parte de regímenes y aparatos de seguridad para espiar a periodistas, fiscales, defensores de derechos humanos y opositores políticos (incluidos escándalos en México, España, Arabia Saudita y Colombia con la compra encubierta a través de la Dirección de Inteligencia Policial - DIPOL).

---

## 2. Anatomía Técnica de Pegasus

1. **Infección Zero-Click / Zero-Day:**
   * No requiere que la víctima pulse ningún enlace ni abra ningún archivo sospechoso.
   * Explota vulnerabilidades de día cero (*Zero-Days*) en librerías de renderizado gráfico de iMessage (`FORCEDENTRY`), WebKit, WhatsApp o llamadas de voz manipuladas a nivel de memoria (`heap spray`).
2. **Capacidades Operativas:**
   * Control total del kernel de iOS y Android.
   * Activación remota y silenciosa del micrófono y la cámara en tiempo real.
   * Extracción de mensajes cifrados (Signal, WhatsApp, Telegram) antes de ser encriptados en pantalla.
   * Registro del GPS milimétrico y extracción de contraseñas, historial y llaveros de seguridad (`keychains`).
3. **Firma Doctrinal:**
   * **Invisibilidad Absoluta:** Su código está diseñado para autoeliminarse si detecta entornos de depuración o análisis forense. El operador busca que la víctima viva en total ignorancia de la vigilancia durante meses o años.

---

## 3. Matriz Comparativa Forense: Pegasus vs. El Asedio Sufrido (Virginia 2026)

| Dimensión Pericial | **Pegasus (NSO Group)** | **El Asedio Sufrido por AnZaCa (Virginia 2026)** |
| :--- | :--- | :--- |
| **Objetivo Estratégico** | **Espionaje Pasivo:** Recolección silenciosa de información de inteligencia. | **Hostigamiento Activo y Silenciamiento:** Neutralizar una auditoría electoral en curso e intimidar a la investigadora. |
| **Comportamiento de Red** | Exfiltración de datos mediante ráfagas imperceptibles; el router jamás se congela ni colapsa. | **Interferencia Agresiva / DoS:** Caída forzada del router residencial, bloqueo de DNS y saturación deliberada de la conexión doméstica. |
| **Detección de Acceso** | No genera alertas ni deja rastro evidente en consolas de usuario convencionales. | Conexiones anómalas en `SubscriberInfo.html` (Google Takeout) y sesiones concurrentes desde hosts en la nube. |
| **Perfil del Interlocutor** | Ataque centrado exclusivamente en dispositivos individuales sin distinción de entorno. | **Ataque Selectivo y Asimétrico:** Dirigido contra Andrea (autora del peritaje en español); Chris, ajeno al idioma, no fue objetivo técnico directo. |
| **Vector Físico** | **INEXISTENTE.** Es un arma digital confinada a la memoria del smartphone. | **PRESENTE Y CRÍTICO:** Vigilancia domiciliaria y **sabotaje físico directo al vehículo familiar** (documentado por el Sheriff). |

---

## 4. El Salto Crítico: La Ruptura del Dominio Digital

La mayor revelación de este dictamen comparativo radica en la superación del paradigma Pegasus:
* Pegasus es un fantasma que vive en el silicio; **quien atacó a la analista en Virginia pisó el asfalto.**
* No se limitaron a observar el tráfico de red: ejecutaron una operación física sobre el medio de transporte familiar (el automóvil), obligando a la intervención presencial de las autoridades locales (`incident report-6-29-26.pdf` del Sheriff de Virginia) y a la apertura de expediente formal con la aseguradora privada.
* En términos de derecho internacional y protección de refugiados, esto demuestra que **la amenaza no era un software espía estándar que se neutraliza cambiando de teléfono**, sino una persecución física personalizada sin alternativa de seguridad interna en territorio estadounidense.

---

## 5. Medidas de Protección Activa y Autodefensa

Para contrarrestar vectores avanzados de vigilancia de grado militar y espionaje gubernamental, se establecen las siguientes directrices permanentes:

1. **Modo Aislamiento Estricto (Lockdown Mode):**
   * Desactivación de previsualización de adjuntos, bloqueo de fuentes web complejas y neutralización de conexiones remotas directas en dispositivos móviles.
2. **Reinicio Cíclico Diario:**
   * La mayoría de los implantes modernos no persistentes en memoria RAM (para evitar detección forense de disco) son desalojados mediante el apagado forzado y reinicio regular del terminal.
3. **Evasión de Correlación de Señal:**
   * Prohibición absoluta de vincular números de teléfono personales o tarjetas bancarias a los canales de trabajo de la bóveda.
   * Uso exclusivo de **Brave** con escudos al máximo y túneles verificados bajo el estándar **Mullvad VPN**.
4. **Protección Perimetral y Físico-Digital:**
   * La seguridad digital es inútil si el perímetro físico está expuesto. Vigilancia constante del entorno físico, verificación visual de cerraduras y vehículos, y alerta temprana coordinada.
