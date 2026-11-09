#!/usr/bin/env bash
set -euo pipefail
echo "=== $(date -Is) ==="
echo "--- rocm-smi ---"
if command -v rocm-smi >/dev/null; then
  rocm-smi
else
  echo "(missing)"
fi
echo "--- rocminfo (head) ---"
if command -v rocminfo >/dev/null; then
  rocminfo | head -n 80
else
  echo "(missing)"
fi
