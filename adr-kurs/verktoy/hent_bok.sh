#!/usr/bin/env bash
# Henter ADR/RID 2025 fra DSB og lager tekst med sideskift (\f), én side per PDF-side.
# Bruk: bash adr-kurs/verktoy/hent_bok.sh [mappe]   (standard: $ADR_BOK eller /tmp/adr-bok)
set -euo pipefail
DIR="${1:-${ADR_BOK:-/tmp/adr-bok}}"
URL="https://www.dsb.no/siteassets/rapporter-og-publikasjoner/veileder/adrrid-2025.pdf"
mkdir -p "$DIR"
if [ ! -s "$DIR/adrrid-2025.pdf" ]; then
  curl -sSfL "$URL" -o "$DIR/adrrid-2025.pdf"
fi
if [ ! -s "$DIR/adr.txt" ]; then
  pdftotext -q -raw "$DIR/adrrid-2025.pdf" "$DIR/adr.txt"
fi
echo "$DIR/adr.txt"
