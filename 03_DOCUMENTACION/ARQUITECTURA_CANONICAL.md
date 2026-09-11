# 🛡️ Arquitectura Táctica Soberana: Canonical & MicroCloud

Este documento define la infraestructura base del sistema **BabaYaga Core**, diseñada para operar bajo los principios de *Zero Trust*, aislamiento criptográfico y soberanía tecnológica total.

## 1. Fundamentos de la Infraestructura Soberana

No dependemos de nubes públicas corporativas. La infraestructura está diseñada para ser hospedada localmente o en clústeres privados controlados por la resistencia.
- **Base Operativa (OS):** Ubuntu Server (LTS).
- **Orquestación y Despliegue:** Canonical MicroCloud.
- **Topología:** Air-Gapped (Aislamiento de red) con sincronización criptográfica asíncrona.

## 2. La Cadena de Confianza Open Source (Chain of Trust)

Para evitar que "el virus se pasee como perro por su casa", implementamos la cadena de confianza de Canonical:
1. **Procedencia estricta:** Todos los paquetes, dependencias de Python y contenedores deben provenir de repositorios firmados por Canonical (Sovereign Open Source).
2. **Inmutabilidad:** Los entornos de análisis forense (como los contenedores de extracción PDF) se despliegan de forma inmutable. Una vez que termina el análisis, el contenedor se destruye, previniendo persistencia de malware.
3. **Validación Criptográfica:** Cada binario y script ejecutado pasa por validación SHA-256 contra un manifiesto local blindado antes de su ejecución.

## 3. Despliegue del Motor LLM Local

La "IA Offline" de BabaYaga Core correrá encapsulada dentro de la infraestructura MicroCloud:
- **Aislamiento:** El modelo LLM (Llama 3 / Mistral / DeepSeek) se ejecuta en un nodo sin acceso a internet público.
- **Ingesta de Datos:** La evidencia se pasa al nodo LLM a través de una tubería unidireccional y se encripta en reposo. Ningún dato de entrada entrena al modelo base, garantizando confidencialidad extrema (secreto empresarial/legal).

## 4. Módulo de Memoria Persistente Anti-Amnesia (VectorDB / RAG)

Para solucionar de raíz la "amnesia" (pérdida de contexto / compaction drift) inherente a los LLMs, BabaYaga Core no dependerá exclusivamente de la memoria de sesión.
- **Base de Datos Vectorial (VectorDB):** Implementación de una base de datos vectorial local (ej. ChromaDB o Milvus) dentro de la red MicroCloud.
- **RAG (Retrieval-Augmented Generation):** Cada expediente, acta, dictamen y NOIP introducido al sistema se vectoriza e indexa permanentemente. Antes de que el LLM procese una orden, busca en esta base de datos inmutable, garantizando que **ningún detalle legal o técnico se pierda**, independientemente de la longitud de la sesión o los reinicios del sistema.

---

## 📝 Cuestionario Táctico para el Webinar (29 de Sept.)
*Preguntas diseñadas por Tycho y Kepler para validar con los expertos de Canonical durante la sesión "Introduction to MicroCloud".*

1. **Aislamiento Físico (Air-Gapped):** "Nuestro laboratorio forense requiere operar en entornos 100% desconectados de internet para proteger evidencia clasificada. ¿Qué grado de dependencia tiene MicroCloud de los servicios externos de Canonical (como servidores DNS o validación de licencias) para iniciar y mantener un clúster local operativo?"
2. **Chain of Trust en Entornos Hostiles:** "En un escenario donde el hardware puede ser decomisado, ¿cómo nos ayuda MicroCloud a garantizar la inmutabilidad y el cifrado de volumen completo (FDE) integrado con TPM 2.0?"
3. **Modelos LLM y GPU Passthrough:** "Vamos a correr motores LLM locales para análisis documental masivo (BabaYaga Core). ¿Qué tan maduro está el soporte de LXD/MicroCloud para pasar aceleradoras GPU/NPU directamente a los contenedores aislados de inferencia?"
4. **Soberanía y Telemetría:** "¿Existe algún tipo de telemetría dura, logs o *call-home* que MicroCloud envíe a los servidores de Canonical y que deba ser bloqueado por nuestro firewall perimetral (pfSense) para garantizar opacidad total?"
