#!/usr/bin/env bash
set -euo pipefail
trap 'echo "[ERROR] Falló en línea $LINENO" >&2' ERR

mkdir -p reports

# TODO: HTTP — guarda headers y explica código en 2–3 líneas al final del archivo
{
  echo "== curl -I example.com =="
  curl -Is https://example.com | sed '/^\r$/d'
  echo
  echo "Explicación: Código HTTP 200 significa que al solicitud fue exitosa. El servidor responde con el contenido solicitado."
} > reports/http.txt

# TODO: DNS — muestra A/AAAA/MX y comenta TTL
{
  echo "== A ==";    dig A example.com +noall +answer
  echo "== AAAA =="; dig AAAA example.com +noall +answer
  echo "== MX ==";   dig MX example.com +noall +answer
  echo
  echo "Nota: Un TTL alto hay menos consultas y eficiencia en caché, pero cambios tardan más en propagarse en toda la red. En un TTL bajo hay cambios rápidos pero más consultas y carga en servidores."
} > reports/dns.txt

# TODO: TLS — registra versión TLS
{
  echo "== TLS via curl -Iv =="
  curl -Iv https://example.com 2>&1 | sed -n '1,20p'
} > reports/tls.txt

# TODO: Puertos locales — lista y comenta riesgos
{
  echo "== ss -tuln =="
  ss -tuln || true
  echo
  echo "Riesgos (editar): Puertos abiertos innecesarios pueden exponer servicios vulnerables a ataques como escaneo, expolit DDoS, etc por lo que conviene cerrarlos o limitar acceso con firewalls."
} > reports/sockets.txt

echo "Reportes generados en ./reports"
