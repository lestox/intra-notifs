#!/bin/bash

source .env

curl -s -i -X POST https://auth.etna-alternance.net/identity \
  -H "Content-Type: application/json" \
  -A "curl/8.13.0" \
  -d "{\"login\": \"$LOGIN\", \"password\": \"$PASSWORD\"}" \
  | grep -i set-cookie | grep authenticator | sed -E 's/.*authenticator="?([^";]+).*/authenticator=\1/' > .auth.env
