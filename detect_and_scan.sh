#!/bin/bash

TARGET="$1"
NUCLEI_TEMPLATES_DIR="nuclei-templates"

if [ -z "$TARGET" ]; then
  echo "Usage: $0 <target>"
  exit 1
fi

echo "Running technology detection..."
RAW_OUTPUT=$(nuclei -t "${NUCLEI_TEMPLATES_DIR}/technologies/tech-detect.yaml" -u "$TARGET" -json)
echo "Raw Output:"
echo "$RAW_OUTPUT"
echo

DETECTED_TECH=$(echo "$RAW_OUTPUT" | grep -oP '(?<="matcher-name":")[^"]+' || true)
echo "Detected Technologies:"
echo "$DETECTED_TECH"
echo

if [ -n "$DETECTED_TECH" ]; then
  echo "Running templates for $DETECTED_TECH:"
  nuclei -t "${NUCLEI_TEMPLATES_DIR}" -u "$TARGET" -tags "$DETECTED_TECH"
else
  echo "No technology detected. Running all templates:"
  nuclei -t "${NUCLEI_TEMPLATES_DIR}" -u "$TARGET"
fi

