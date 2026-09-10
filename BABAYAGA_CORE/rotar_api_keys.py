#!/usr/bin/env python3
"""
rotar_api_keys.py — Módulo de Rotación y Actualización de API Keys (Google AI Studio)
Permite actualizar de forma segura las claves API en .env y probar la conexión.
"""

import os
import sys
import re

ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')

def actualizar_api_key(nueva_clave: str, slot: int = 1):
    if not os.path.exists(ENV_PATH):
        print(f"❌ No se encontró el archivo .env en: {ENV_PATH}")
        return False

    with open(ENV_PATH, 'r', encoding='utf-8') as f:
        contenido = f.read()

    target_key = f"GEMINI_API_KEY_{slot}"
    if target_key in contenido:
        contenido_nuevo = re.sub(rf"{target_key}\s*=\s*.*", f"{target_key} = {nueva_clave.strip()}", contenido)
    else:
        contenido_nuevo = contenido.rstrip() + f"\n{target_key} = {nueva_clave.strip()}\n"

    with open(ENV_PATH, 'w', encoding='utf-8') as f:
        f.write(contenido_nuevo)

    print(f"✅ {target_key} actualizada exitosamente en .env (Slot {slot}).")
    return True

def probar_api_key(clave: str):
    print("🔍 Probando conectividad con Google AI Studio API...")
    try:
        import urllib.request
        import json

        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={clave.strip()}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                modelos = len(data.get('models', []))
                print(f"✨ ¡Conexión exitosa! Google AI Studio respondió correctamente ({modelos} modelos disponibles).")
                return True
    except Exception as e:
        print(f"⚠️ Error al probar la clave API: {e}")
        return False

def main():
    print("=" * 65)
    print("🔑 BABAYAGA CORE — ROTADOR SEGURO DE API KEYS (GOOGLE AI STUDIO)")
    print("=" * 65)

    if len(sys.argv) > 1:
        nueva_key = sys.argv[1].strip()
        slot = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    else:
        print("\nPara actualizar la clave API de Google AI Studio:")
        print("1. Genera una nueva clave en: https://aistudio.google.com/app/apikey")
        nueva_key = input("\n👉 Pega la nueva API Key aquí: ").strip()
        slot_input = input("👉 Elige el Slot [1, 2 o 3 para GEMINI_API_KEY_1/2/3] (por defecto 1): ").strip()
        slot = int(slot_input) if slot_input in ['1', '2', '3'] else 1

    if not nueva_key:
        print("❌ Operación cancelada: La clave ingresada está vacía.")
        return

    if probar_api_key(nueva_key):
        actualizar_api_key(nueva_key, slot)
        print("\n🎉 Proceso completado. La nueva API Key está lista para ser usada por AndreTaker y Tycho.")
    else:
        confirmar = input("\n⚠️ La clave no respondió correctamente en la prueba. ¿Deseas guardarla de todos modos? (s/n): ").strip().lower()
        if confirmar == 's':
            actualizar_api_key(nueva_key, slot)

if __name__ == '__main__':
    main()
