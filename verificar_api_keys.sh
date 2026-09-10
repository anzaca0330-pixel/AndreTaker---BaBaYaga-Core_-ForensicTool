#!/usr/bin/env bash
# ==============================================================================
# BABAYAGA CORE — SCRIPT BASH DE DIAGNÓSTICO Y ROTACIÓN DE API KEYS (GEMINI API)
# Diseñado para: Johannes (Andrea Zabala Cárcamo / AnZaCa)
# ==============================================================================

set -eo pipefail

ENV_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/BABAYAGA_CORE/.env"

COLOR_CYAN='\033[0;36m'
COLOR_GREEN='\033[0;32m'
COLOR_RED='\033[0;31m'
COLOR_YELLOW='\033[1;33m'
COLOR_RESET='\033[0m'

echo -e "${COLOR_CYAN}======================================================================${COLOR_RESET}"
echo -e "${COLOR_CYAN} 🔑 DIAGNÓSTICO METROLÓGICO DE API KEYS — BABAYAGA CORE & TYCHO      ${COLOR_RESET}"
echo -e "${COLOR_CYAN}======================================================================${COLOR_RESET}"

if [ ! -f "$ENV_FILE" ]; then
    echo -e "${COLOR_RED}❌ Error: No se encontró el archivo de entorno en: $ENV_FILE${COLOR_RESET}"
    exit 1
fi

probar_clave() {
    local slot="$1"
    local raw_key="$2"
    local key
    key=$(echo "$raw_key" | tr -d '[:space:]')

    if [ -z "$key" ]; then
        echo -e "${COLOR_YELLOW}[Slot $slot] Vacío / No configurado.${COLOR_RESET}"
        return
    fi

    # Máscara de seguridad para no exponer la clave completa en pantalla
    local key_len=${#key}
    local masked_key
    if [ "$key_len" -gt 12 ]; then
        masked_key="${key:0:6}...${key: -6}"
    else
        masked_key="***"
    fi

    echo -ne "🔍 Verificando Slot $slot (${masked_key})... "

    local response
    local http_code
    response=$(curl -s -w "\n%{http_code}" --max-time 8 "https://generativelanguage.googleapis.com/v1beta/models?key=${key}" 2>/dev/null || true)
    
    http_code=$(echo "$response" | tail -n1)
    local body
    body=$(echo "$response" | sed '$d')

    if [ "$http_code" = "200" ]; then
        local num_models
        num_models=$(echo "$body" | grep -o '"name": "models/' | wc -l || echo "OK")
        echo -e "${COLOR_GREEN}✅ ACTIVA Y OPERATIVA (200 OK — Modelos disponibles: $num_models)${COLOR_RESET}"
    elif [ "$http_code" = "400" ] || [ "$http_code" = "403" ]; then
        echo -e "${COLOR_RED}❌ FALLÓ (HTTP $http_code — Clave inválida, revocada o sin cuota)${COLOR_RESET}"
    elif [ -z "$http_code" ] || [ "$http_code" = "000" ]; then
        echo -e "${COLOR_YELLOW}⚠️ SIN CONEXIÓN (Tiempo de espera agotado o bloqueo de red)${COLOR_RESET}"
    else
        echo -e "${COLOR_YELLOW}⚠️ RESPUESTA INESPERADA (HTTP $http_code)${COLOR_RESET}"
    fi
}

# 1. Leer las 3 claves del .env
KEY1=$(grep "^GEMINI_API_KEY_1" "$ENV_FILE" | cut -d '=' -f2- | tr -d ' ' || true)
KEY2=$(grep "^GEMINI_API_KEY_2" "$ENV_FILE" | cut -d '=' -f2- | tr -d ' ' || true)
KEY3=$(grep "^GEMINI_API_KEY_3" "$ENV_FILE" | cut -d '=' -f2- | tr -d ' ' || true)

echo -e "\n📋 Estado actual de los 3 Slots en .env:"
probar_clave "1 (GEMINI_API_KEY_1)" "$KEY1"
probar_clave "2 (GEMINI_API_KEY_2)" "$KEY2"
probar_clave "3 (GEMINI_API_KEY_3)" "$KEY3"

echo -e "\n${COLOR_CYAN}----------------------------------------------------------------------${COLOR_RESET}"
echo -e "💡 Para rotar o actualizar una clave de inmediato:"
echo -e "   python3 BABAYAGA_CORE/rotar_api_keys.py <NUEVA_CLAVE> <SLOT_1_2_o_3>"
echo -e "${COLOR_CYAN}======================================================================${COLOR_RESET}\n"
