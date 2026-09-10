"""
sanear_historial_ordenes.py — Enmascarador de Secretos para GitHub Push Protection
Redacta tokens y credenciales del archivo HISTORIAL_DE_ORDENES.md
"""

import os
import re

def main():
    target_file = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/03_DOCUMENTACION/HISTORIAL_DE_ORDENES.md"
    if not os.path.exists(target_file):
        print(f"❌ Archivo no encontrado: {target_file}")
        return

    with open(target_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Redactar GitHub PATs
    pat_ghp = r"gh" + r"p_[A-Za-z0-9_]{30,}"
    pat_pat = r"github_" + r"pat_[A-Za-z0-9_]{30,}"
    content_clean = re.sub(pat_ghp, "[REDACTED_GITHUB_TOKEN]", content)
    content_clean = re.sub(pat_pat, "[REDACTED_GITHUB_TOKEN]", content_clean)

    # Redactar GCP API Keys
    pat_aiza = r"AIza" + r"Sy[A-Za-z0-9_\-]{30,}"
    pat_aq = r"AQ\." + r"[A-Za-z0-9_\-]{20,}"
    content_clean = re.sub(pat_aiza, "[REDACTED_GCP_API_KEY]", content_clean)
    content_clean = re.sub(pat_aq, "[REDACTED_GCP_API_KEY]", content_clean)

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content_clean)

    # Buscar y sanitizar en todos los md de 03_DOCUMENTACION
    doc_dir = "/home/andrea-zabala-c/AndreTaker---AnZaCa-Rep/03_DOCUMENTACION"
    for root, _, files in os.walk(doc_dir):
        for file in files:
            if file.endswith(".md"):
                fp = os.path.join(root, file)
                try:
                    with open(fp, "r", encoding="utf-8", errors="ignore") as f_in:
                        fc = f_in.read()
                    fc_clean = re.sub(pat_aiza, "[REDACTED_GCP_API_KEY]", fc)
                    fc_clean = re.sub(pat_aq, "[REDACTED_GCP_API_KEY]", fc_clean)
                    fc_clean = re.sub(pat_ghp, "[REDACTED_GITHUB_TOKEN]", fc_clean)
                    if fc != fc_clean:
                        with open(fp, "w", encoding="utf-8") as f_out:
                            f_out.write(fc_clean)
                        print(f"✅ Sanitizado: {file}")
                except Exception:
                    pass

    print("✅ Secretos redactados y sanitizados exitosamente en HISTORIAL_DE_ORDENES.md y documentación.")

if __name__ == "__main__":
    main()
